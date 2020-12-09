import numpy as np
from CMGradobject import CMGobject as cmg
import CMfunc as cm
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


def uniform(test_points, A):
    test_points_pol = cart2pol(test_points)
    val_list = np.zeros((test_points.shape[0]))
    grad_list = np.zeros(test_points.shape)
    for i, vec in enumerate(test_points_pol):
        r = cmg(vec[0], np.array([1., 0.]))
        theta = cmg(vec[1], np.array([0., 1.]))
        f = A*r*cm.cos(theta)
        val_list[i] = f.val
        grad_list[i] = f.grad

    return val_list, grad_list

def doublet(test_points, A, pos_doub):
    test_points_pol = cart2pol(np.subtract(test_points, pos_doub))
    val_list = np.zeros((test_points.shape[0]), dtype='double')
    grad_list = np.zeros(test_points.shape, dtype='double')
    for i, vec in enumerate(test_points_pol):
        r = cmg(vec[0], np.array([1., 0.], dtype='double'))
        theta = cmg(vec[1], np.array([0, 1.], dtype='double'))
        f = (A/r)*cm.cos(theta)
        val_list[i] = f.val
        grad_list[i] = f.grad

    return val_list, grad_list
def uni_and_doub(test_points, A1, A2):
    test_points_pol = cart2pol(test_points)
    val_list = np.zeros((test_points.shape[0]), dtype='double')
    grad_list = np.zeros(test_points.shape, dtype='double')
    for i, vec in enumerate(test_points_pol):
        r = cmg(vec[0], np.array([1., 0.], dtype='double'))
        theta = cmg(vec[1], np.array([0, 1.], dtype='double'))
        f = (A1/(r))*cm.cos(theta) + A2*r*cm.cos(theta)
        val_list[i] = f.val
        grad_list[i] = f.grad
    return val_list, grad_list

test_x_cartesian = np.linspace(-1, 1, 10)
test_y_cartesian = np.linspace(-1, 1, 10)
xv, yv = np.meshgrid(test_x_cartesian, test_y_cartesian)
test_points_cartesian = np.vstack((xv.flatten(), yv.flatten() )).T
A = 2

phi_uni, v_uni = uniform(test_points_cartesian, A)
phi_doub, v_doub = doublet(test_points_cartesian, A, np.array([0.5, 0.5]))
phi_unidub, v_unidoub = uni_and_doub(test_points_cartesian, A, A)

v_uni_cart = pol2cart_grad(v_uni, cart2pol(test_points_cartesian) )
v_doub_cart = pol2cart_grad(v_doub, cart2pol(test_points_cartesian) )
v_unidoub_cart = pol2cart_grad(v_unidoub, cart2pol(test_points_cartesian) )

plt.quiver(xv, yv, v_unidoub_cart.T[0], v_unidoub_cart.T[1])
plt.show()
