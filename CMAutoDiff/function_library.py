import numpy as np

def function_library(function_string):
    if function_string == 'sin(x)' or function_string == 'SIN(x)':
        val_out = lambda x: np.sin(x)
        deriv_out = lambda x: np.cos(x)
        return val_out, deriv_out
    elif function_string == 'cos(x)' or function_string == 'COS(x)':
        val_out = lambda x: np.cos(x)
        deriv_out = lambda x: -np.sin(x)
        return val_out, deriv_out
    elif function_string == 'tan(x)' or function_string == 'TAN(x)':
        val_out = lambda x: np.tan(x)
        deriv_out = lambda x: (np.cos(x))**(-2)
        return val_out, deriv_out
    elif function_string == 'exp(x)':
        val_out = lambda x: np.exp(x)
        deriv_out = lambda x: np.exp(x)
        return val_out, deriv_out
    elif function_string == 'ln(x)' or function_string == 'log(x)':
        val_out = lambda x: np.log(x)
        deriv_out = lambda x: x**(-1)
        return val_out, deriv_out
