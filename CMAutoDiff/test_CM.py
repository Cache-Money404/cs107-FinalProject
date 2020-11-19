import pytest
import sys, os.path
AD_dir = os.path.abspath(os.path.dirname(__file__)) # needed so pytest works correctly
sys.path.append(AD_dir) # needed so pytest works correctly

import numpy as np
from function_library import function_library
from CMobject import CMobject
from FuncObj import FuncObj

# tests for CMobject

def test_mul_operation():
    x = CMobject(-3.)
    f = x**3+2*x
    assert (f.val,f.der) == (-33, 29)
    
def test_add_sub_operations():
    x = CMobject(1)
    f = x + 2 + x - 1 - x
    assert (f.val,f.der) == (2.0, 1.0)
    
def test_div_operations():
    x = CMobject(1)
    f = x/(3*x + 1) - x/5 + 5/x
    assert (f.val,f.der) == (5.05, -5.1375)
    
def test_pow_operations():
    x = CMobject(1)
    f = x**2 + 2**x
    assert (f.val,f.der) == (3.0, 3.386294361119891)
    
def test_difficult_derivative_case():    
    x1 = CMobject(1.0)
    
    ## the following is a test case for: sin(tan(x)) + 2^(cos(x)) + sin(x)^tan(x)^exp(x) - (cos(x))^2, seeded at x = 1. Try it in autograd, it works.
    test_func1 = FuncObj('sin', FuncObj('tan', x1)) + 2**(FuncObj('cos', x1)) + FuncObj('sin', x1)**(FuncObj('tan', x1))**(FuncObj('exp', x1)) - FuncObj('cos', x1)**2
    print("test_func1 val, der: {}, {}".format(test_func1.val, test_func1.der))
    assert (test_func1.val,test_func1.der) == ( 2.724678163898656, -1.0139897786023675)
    
def test_value_error():
    with pytest.raises(ValueError):
        CMobject(1, 'fake')
    

if __name__ == "__main__":
    print("Here")