import numpy as np
from CMAutoDiff.CMGradobject import CMGobject as cmg
import CMAutoDiff.CMfunc_grad as cm
import matplotlib.pyplot as plt

def cart2pol(cart_vec): # converts position coordinates
    pol_vec = np.zeros(np.shape(cart_vec) )
    for i, vec in enumerate(cart_vec):
        r = np.linalg.norm(vec)
        if vec[0] == 0:
            theta = np.pi/2 + np.pi*(0**( 1 + np.sign(vec[1])))
        else:
            theta = np.arctan(vec[1]/vec[0]) + np.pi*(0**( 1 + np.sign(vec[0])))

        pol_vec[i][0] = r
        pol_vec[i][1] = theta
    return pol_vec

def pol2cart(pol_vec): # converts position coordinates
    cart_vec = np.zeros(np.shape(pol_vec) )
    for i, vec in enumerate(pol_vec):
        cart_vec[i][0] = vec[0]*np.cos(vec[1])
        cart_vec[i][1] = vec[0]*np.sin(vec[1])
    return cart_vec

def pol2cart_grad(grad_vec_pol, pos_vec_pol):
    grad_vec_cart = np.zeros(np.shape(grad_vec_pol))
    pos_vec_cart = pol2cart(pos_vec_pol)
    for i, vec in enumerate(grad_vec_pol):
        grad_vec_cart[i][0] = vec[0]*np.cos(pos_vec_pol[i][1]) + vec[1]*np.cos((np.pi/2) + pos_vec_pol[i][1])/pos_vec_pol[i][0]
        grad_vec_cart[i][1] = vec[0]*np.sin(pos_vec_pol[i][1]) + vec[1]*np.sin((np.pi/2) + pos_vec_pol[i][1])/pos_vec_pol[i][0]
    return grad_vec_cart

class Flow():
    def __init__(self, key, inputs):
        self._strength = inputs[0]
        self._key = key
    def rule_out_points(self, cart_coords: np.array):
        return cart_coords
    def compute_points(self, cart_coords: np.array):
        self._points = cart2pol(cart_coords)
    def compute_flow(self):
        raise NotImplementedError


class uniform(Flow):
    def compute_flow(self):
        f_all = []
        for pos in self._points:
            r = cmg(pos[0], np.array([1., 0.]))
            theta = cmg(pos[1], np.array([0., 1.]))
            f_all.append(self._strength*r*cm.cos(theta))
        return f_all
    def __repr__(self):
        return repr(self._key + ': a uniform flow of strength {}'.format(self._strength) )

class source(Flow):
    def __init__(self, key, inputs):
        self._strength = inputs[0]
        self._pos = np.array([inputs[1], inputs[2]])
        self._key = key
        self.b = 1  ## for now
    def rule_out_points(self, cart_coords: np.array):
        return_points = np.array([0, 0])
        for pos in cart_coords:
            if not (pos[0] == self._pos[0] and pos[1] == self._pos[1]):
                return_points = np.vstack((return_points, [pos]))
        return return_points[1:]

    def compute_points(self, cart_coords: np.array):
        self._points = cart2pol(np.subtract(cart_coords, self._pos))
    def compute_flow(self): ## assumes, for now, unitary b
        f_all = []
        for pos in self._points:
            r = cmg(pos[0], np.array([1., 0.]))
            theta = cmg(pos[1], np.array([0., 1.]))
            f_all.append((self._strength/(2*np.pi*self.b))*cm.log(r))
        self.CMGs = f_all
        return self.CMGs

    def __repr__(self):
        return repr(self._key + ': a source of strength {} at (x, y) = {}'.format(self._strength, self._pos ) )

class sink(source):
    def __init__(self, key, inputs):
        self._strength = -inputs[0]
        self._pos = np.array([inputs[1], inputs[2]])
        self._key = key
        self.b = 1  ## for now
    def __repr__(self):
        return repr(self._key + ': a sink of strength {} at (x, y) = {}'.format(self._strength, self._pos ) )

class vortex(Flow):
    def __init__(self, key, inputs):
        self._strength = inputs[0]
        self._pos = np.array([inputs[1], inputs[2]])
        self._key = key
    def rule_out_points(self, cart_coords: np.array):
        return_points = np.array([0, 0])
        for pos in cart_coords:
            if not (pos[0] == self._pos[0] and pos[1] == self._pos[1]):
                return_points = np.vstack((return_points, [pos]))
        return return_points[1:]

    def compute_points(self, cart_coords: np.array):
        self._points = cart2pol(np.subtract(cart_coords, self._pos))
    def compute_flow(self): ## assumes, for now, unitary b
        f_all = []
        for pos in self._points:
            theta = cmg(pos[1], np.array([0., 1.]))
            f_all.append(self._strength*theta)
        self.CMGs = f_all
        return self.CMGs

    def __repr__(self):
        return repr(self._key + ': a vortex of strength {} at (x, y) = {}'.format(self._strength, self._pos ) )

def identify_flow(key_in, inputs):
    library = {
        "uniform": uniform,
        "source": source,
        "sink": sink,
        "vortex": vortex
    }
    for key in library:
        if key in key_in:
            return (library[key])(key_in, inputs)

def generate_cart_gradients(F, positions_cart):
    gradients_polar = np.array([0, 0])
    phi = np.array([])
    for points in F:
        phi = np.append(phi, points.val)
        gradients_polar = np.vstack((gradients_polar, points.grad))

    gradients_cart = pol2cart_grad(gradients_polar[1:], cart2pol(positions_cart))
    return gradients_cart, phi

def main():
    incr = 25
    test_x_cartesian = np.linspace(-1, 1, incr)
    test_y_cartesian = np.linspace(-1, 1, incr)
    xv, yv = np.meshgrid(test_x_cartesian, test_y_cartesian)
    test_points_cartesian = np.vstack((xv.flatten(), yv.flatten() )).T

    print(xv)
    print(yv)

    dict_in = {
        "uniform1": [1.],
        "source1": [2., 0.5, 0.5],
        "sink1": [2., -0.5, -0.5],
        "vortex1": [3., 0., 0.],
    }
    flow_list = []

    for i, key in enumerate(dict_in):
        flow_list.append(identify_flow(key, dict_in[key]))
        test_points_cartesian = flow_list[i].rule_out_points(test_points_cartesian)


    print("computing flow gradients for the following potential flow solutions:")
    flow = flow_list[0]
    flow.compute_points(test_points_cartesian)
    F = flow.compute_flow()
    for flow in flow_list[1:]:
        print(flow)
        flow.compute_points(test_points_cartesian)
        f_it = flow.compute_flow()
        for i, CMGpoint in enumerate(f_it):
            F[i] += CMGpoint


    print("Done. Generating plots:")
    cartesian_gradients, potential = generate_cart_gradients(F, test_points_cartesian)

    print(cartesian_gradients.shape)
    print(test_points_cartesian.shape)
    print(np.max(cartesian_gradients))
    fig, (ax_l, ax_r) = plt.subplots(1,2, figsize=(8, 4))
    ax_l.quiver(test_points_cartesian.T[0], test_points_cartesian.T[1], cartesian_gradients.T[0], cartesian_gradients.T[1], scale=1000, scale_units='width')
    ax_r.quiver(test_points_cartesian.T[0], test_points_cartesian.T[1], cartesian_gradients.T[0], cartesian_gradients.T[1], scale=500, scale_units='width')
    plt.show()

if __name__ == '__main__':
    main()


# phi_uni, v_uni = uniform(test_points_cartesian, A)
# phi_doub, v_doub = doublet(test_points_cartesian, A, np.array([0.5, 0.5]))
# phi_unidub, v_unidoub = uni_and_doub(test_points_cartesian, A, A)
#
# v_uni_cart = pol2cart_grad(v_uni, cart2pol(test_points_cartesian) )
# v_doub_cart = pol2cart_grad(v_doub, cart2pol(test_points_cartesian) )
# v_unidoub_cart = pol2cart_grad(v_unidoub, cart2pol(test_points_cartesian) )
