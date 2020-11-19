from CMobject import CMobject
from function_library import function_library

class FuncObj(CMobject):
    """Creates a CMobject for forward automatic differentiation
    based on an elementary function:
    FuncObj(string, arg)

    INPUTS
    ======
    string : an elementary function out of the following list:
        
        'sin'
        'cos'
        'tan'
        'exp'
        'ln' or 'log'
        
    arg : a CMobject for automatic differentiation
    
    RETURNS
    =======
    *note* x is a CMobject in the cases below
    
    'sin' --> CMobject(val = np.sin(x), der = -np.cos(x))
    'cos' --> CMobject(val = np.cos(x), der = np.sin(x))
    'tan' --> CMobject(val = np.tan(x), der = (np.cos(x))**(-2))
    'exp' --> CMobject(val = np.exp(x), der = np.exp(x))
    'ln' or 'log' --> CMobject(val = np.log(x), der = x**(-1))

    EXAMPLES
    ========
    >>> x = CMobject(1.0)
    >>> f = FuncObj('sin',x)
    >>> f.val
    0.8414709848078965
    >>> f.der
    0.5403023058681398
    """
    
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
