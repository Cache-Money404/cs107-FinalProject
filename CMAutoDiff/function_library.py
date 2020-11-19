import numpy as np

def function_library(function_string):
    """Returns the result of an elementary numpy function and its derivative.

    INPUTS
    ======
    function_string : string
        an elementary function out of the following list:
        
        'sin'
        'cos'
        'tan'
        'exp'
        'ln' or 'log'

    RETURNS
    =======
    INPUT         -->   val_out , deriv_out
    
    'sin'         --> np.sin(x) , -np.cos(x))
    'cos'         --> np.cos(x) , np.sin(x))
    'tan'         --> np.tan(x), np.cos(x))**(-2)
    'exp'         --> np.exp(x), np.exp(x)
    'ln' or 'log' --> np.log(x), x**(-1)
    

    """
    
    if function_string == 'sin' or function_string == 'SIN':
        val_out = lambda x: np.sin(x)
        deriv_out = lambda x: np.cos(x)
        return val_out, deriv_out
    elif function_string == 'cos' or function_string == 'COS':
        val_out = lambda x: np.cos(x)
        deriv_out = lambda x: -np.sin(x)
        return val_out, deriv_out
    elif function_string == 'tan' or function_string == 'TAN':
        val_out = lambda x: np.tan(x)
        deriv_out = lambda x: (np.cos(x))**(-2)
        return val_out, deriv_out
    elif function_string == 'exp':
        val_out = lambda x: np.exp(x)
        deriv_out = lambda x: np.exp(x)
        return val_out, deriv_out
    elif function_string == 'ln' or function_string == 'log':
        val_out = lambda x: np.log(x)
        deriv_out = lambda x: x**(-1)
        return val_out, deriv_out