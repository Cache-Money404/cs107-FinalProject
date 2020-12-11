from CMGradobject import CMGobject as cmg
import CMfunc_grad as cm
import numpy as np

## just a proof of concept file that will show the user how to define a vector valued function as defined on that piazza post.
## We don't have to change anything about the original autodiff class as it exists now, we just need a way to combine them in a friendly way


class CMV():
    def __init__(self, f_list):
        self.val = np.array([f_list[0].val])
        self.jac = np.array([ f_list[0].grad ])
        for func in f_list[1:]:
            self.val = np.append(self.val, func.val)
            self.jac = np.vstack((self.jac, [func.grad]))
    def __add__(self, other):
        if isinstance(other, CMV):
            assert other.val.shape[0] == self.val.shape[0]
            assert other.jac.shape[1] == self.jac.shape[1]
            val_out = self.val + other.val
            jac_out = self.jac + other.jac
            return_list = []
            for i, val in enumerate(val_out):
                return_list.append(cmg(val, jac_out[i]))
            return CMV(return_list)
        elif isinstance(other, CMGobject):
            assert other.grad.shape[0] == self.jac.shape[1]
            val_out = self.val + other.val
            jac_out = np.add(self.jac, other.grad)
            return_list = []
            for i, val in enumerate(val_out):
                return_list.append(cmg(val, jac_out[i]))
            return CMV(return_list)
        else:
            print("get it together mate")
            raise ValueError

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, CMV):
            assert other.val.shape[0] == self.val.shape[0]
            assert other.jac.shape[1] == self.jac.shape[1]
            val_out = self.val - other.val
            jac_out = self.jac - other.jac
            return_list = []
            for i, val in enumerate(val_out):
                return_list.append(cmg(val, jac_out[i]))
            return CMV(return_list)
        elif isinstance(other, CMGobject):
            assert other.grad.shape[0] == self.jac.shape[1]
            val_out = self.val + other.val
            jac_out = np.add(self.jac, -1*other.grad)
            return_list = []
            for i, val in enumerate(val_out):
                return_list.append(cmg(val, jac_out[i]))
            return CMV(return_list)
        else:
            print("get it together mate")
            raise ValueError

    def __rsub__(self, other):
        return self.__sub__(other)

    def __repr__(self):
        return f'CMVobject(val = {self.val}, \n jacobian = {self.jac})'

#
## making a vector valued function f: R^4 -> R^3
x1 = cmg(1, np.array([1, 0, 0, 0]))
x2 = cmg(2, np.array([0, 1, 0, 0]))
x3 = cmg(3, np.array([0, 0, 1, 0]))
x4 = cmg(4, np.array([0, 0, 0, 1]))

print(cm.log(x3))
print(3*x4*x3)

print(cm.log(x3) - 3*(x4*x3))

F1_list = [cm.cos(x1 - 2*x2), cm.log(x3) - 3*x4*x3, x2**2, (x1 + x2)/(x3 - x4)  ]
F2_list = [2*x3 + cm.cos(x1 - 2*x2), 3*x4 - x3, x2**x4, 1/(x3 - x4)  ]

F1 = CMV(F1_list)
F2 = CMV(F2_list)

F3 = F1 + F2
print(F3)

F4 = F1 - F2
print(F4)
