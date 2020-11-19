import CMobject
from CMobject import CMobject
from function_library import function_library

class FuncObj(CMobject):
    #Constructor sets value and derivative
    def __init__(self, string, arg):
        val_out, deriv_out = function_library(string)
        try:
            self.val = val_out(arg.val)
            self.der = deriv_out(arg.val)*arg.der
        except AttributeError:
            const = CMobject(arg, der=0)
            self.val = val_out(const.val)
            self.der = deriv_out(const.val)*const.der
