import CMobject
import numpy as np
def function_library(function_list):
    for i in function_list:
        if i == 'sin' or i == 'SIN':
            return CMobject(np.sin(x.val), np.cos(x.val)*x.der)
        elif i == 'cos' or i == 'COS':
            return CMobject(np.cos(x.val), -1*np.sin(x.val)*x.der)
        elif i == 'tan' or i == 'TAN':
            return CMobject(np.tan(x.val), np.arccos(x.val)*x.der)
        elif i == 'e**x':
            return CMobject(np.exp(x.val), np.exp(x.val)*x.der)
        elif i == 'sqrt' :
            return CMobject(np.sqrt(x.val), x.der/(2*np.sqrt(x.val))
        elif i == 'log10':
            return CMobject(np.log10(x.val), (1/x.val)




