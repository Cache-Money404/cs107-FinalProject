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
    f = x + 2 + x + x + x - 1 - x - x - x
    assert (f.val,f.der) == (2.0, 1.0)

def test_radd_operation():
    x = CMobject(1)
    f = 2 + x
    assert (f.val,f.der) == (3.0, 1.0)

def test_rsub_operation():
    x = CMobject(1)
    f = 10 - x
    assert (f.val,f.der) == (9.0, -1.0)

def test_div_operations():
    x = CMobject(1)
    f = x/(3*x + 1) - x/5 + 5/x
    assert (f.val,f.der) == (5.05, -5.1375)

def test_pow_operations():
    x = CMobject(1)
    f = x**2 + 2**x + x**x**x**2**x
    assert (f.val,f.der) == (4.0, 4.386294361119891)
    
def test_rpow_operations():
    x = CMobject(3.0)
    f = x.__rpow__(x)
    assert (f.val,f.der) == (27.0, 56.66253179403897)

def test_negation():
    x = CMobject(1)
    y = -x
    assert (y.val,y.der) == (-1.0, -1.0)

def test_difficult_derivative_case():
    x1 = CMobject(1.0)

    ## the following is a test case for: sin(tan(x)) + 2^(cos(x)) + sin(x)^tan(x)^exp(x) - (cos(x))^2, seeded at x = 1. Try it in autograd, it works.
    test_func1 = FuncObj('sin', FuncObj('tan', x1)) + 2**(FuncObj('cos', x1)) + FuncObj('sin', x1)**(FuncObj('tan', x1))**(FuncObj('exp', x1)) - FuncObj('cos', x1)**2
    print("test_func1 val, der: {}, {}".format(test_func1.val, test_func1.der))
    assert (test_func1.val,test_func1.der) == ( 2.724678163898656, -1.0139897786023675)
    print(f"Difficult derivative test passed.")

def test_object_input_error():
    with pytest.raises(ValueError):
        CMobject(1, 'fake')

def test_FuncObj_constant():
    f = FuncObj('sin',2)
    assert (f.val,f.der) == (0.9092974268256817, -0.0)

def test_natural_log_function_library():
    x = CMobject(2)
    f = FuncObj('log',x)
    assert (f.val,f.der) == (0.6931471805599453, 0.5)

def test_newtons_method():
    # define newton's method to work with CMobject and FuncObj
    def newt(f,x,tol= 1e-10,max_it=100):

        for i in range(max_it):
            dx = -f(x).val/f(x).der # Update Delta x_{k}
            if np.abs(dx) < tol: # Stop iteration if solution found
                print(f"root found at: x={x.val} after {i+1} iterations.")
                print(f"Newton's Method test passed.")
                root = x.val
                return root
                break
            else:
                x += dx #update x

    # TEST CASE FOR f(x) = x^2 + ln(x) + x
    def f(x): # define function
        return x**2 + FuncObj('log',x) + x

    x = CMobject(1)
    result = newt(f,x)
    assert result == 0.4858388639605664

def test_all():
    print('Running tests...')
    print('''    (all basic tests results suppressed except difficult derivative and Newton's method)''')
    test_mul_operation()
    test_add_sub_operations()
    test_radd_operation()
    test_rsub_operation()
    test_div_operations()
    test_pow_operations()
    test_negation()
    test_object_input_error()
    test_FuncObj_constant()
    test_natural_log_function_library()
    test_difficult_derivative_case()
    test_newtons_method()
    print('...all tests run successfully!')

test_all()

#if __name__ == "__main__":
#    print("Here")
