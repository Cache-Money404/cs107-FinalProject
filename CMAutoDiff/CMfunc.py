import numpy as np
from CMobject import CMobject

# trig functions

def sin(x):
    try:
        val = np.sin(x.val) 
        der = np.cos(x.val)*x.der
        y = CMobject(val,der)
        return y
    except AttributeError:
        return np.sin(x) # if x is a constant
    
def cos(x):
    try:
        val = np.cos(x.val)
        der = -np.sin(x.val)*x.der
        y = CMobject(val,der)
        return y
    except AttributeError:
        return np.cos(x)
    

def tan(x):
    try:
        val = np.tan(x.val)
        der = ((np.cos(x.val))**(-2))*x.der
        y = CMobject(val,der)
        return y
    except AttributeError:
        return np.tan(x)
   
    
# inverse trig functions
    
def arcsin(x):
    try:
        val = np.arcsin(x.val) 
        der = ((1-x.val**2)**(-0.5))*x.der
        y = CMobject(val,der)
        return y
    except AttributeError:
        return np.arcsin(x) # if x is a constant
    
def arccos(x):
    try:
        val = np.arccos(x.val) 
        der = -((1-x.val**2)**(-0.5))*x.der
        y = CMobject(val,der)
        return y
    except AttributeError:
        return np.arccos(x)
    
def arctan(x):
    try:
        val = np.arctan(x.val) 
        der = ((1+x.val**2)**(-2))*x.der
        y = CMobject(val,der)
        return y
    except AttributeError:
        return np.arctan(x) # if x is a constant
    
# exponential and logarithm functions

def exp(x):
    try:
        val = np.exp(x.val)
        der = np.exp(x.val)*x.der
        y = CMobject(val,der)
        return y
    except AttributeError:
        return np.exp(x)
    
    
def log(x, base = np.e): # handles ln(x) == log(x) because default base = np.e
    try:
        val = np.log(x.val)/np.log(base)
        der = (1/(x.val*np.log(base)))*x.der
        y = CMobject(val,der)
        return y
    except AttributeError:
        return np.log(x)/np.log(base)    
        
    
# functions defined in terms of other functions
# sinh, cosh, tanh, logistic, sqrt
    
def sinh(x): # in terms of exp(x), so exp(x) handles val and der calculations
    return (exp(x) - exp(-x))/2

def cosh(x): # in terms of exp(x), so exp(x) handles val and der calculations
    return (exp(x) + exp(-x))/2

def tanh(x): # in terms of exp(x), so exp(x) handles val and der calculations
    return sinh(x)/cosh(x)

# https://en.wikipedia.org/wiki/Logistic_function    
def logistic(x): # in terms of exp(x), so exp(x) handles val and der calculations
    return (1+exp(-x))**(-1)

def sqrt(x): # in terms of pow(x,0.5) using overloaded __pow__ function
    return x**.5