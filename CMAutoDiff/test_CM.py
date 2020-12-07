import pytest
import sys, os.path
AD_dir = os.path.abspath(os.path.dirname(__file__)) # needed so pytest works correctly
sys.path.append(AD_dir) # needed so pytest works correctly

import numpy as np
import CMfunc
from CMobject import CMobject
#from FuncObj import FuncObj

# tests for CMobject

def test_repr():
    x = CMobject(3)
    assert x.__repr__() == 'CMobject(val = 3.0, der = 1.0)'

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
    

# tests for CMfunc
    
def test_sin():
    x = CMobject(2)
    f = CMfunc.sin(x)
    assert (f.val,f.der) == (np.sin(2), np.cos(2))
    #print('passed sine test')
    
def test_arcsin():
    x = CMobject(0.5)
    f = CMfunc.arcsin(x)
    assert (f.val,f.der) == (np.arcsin(.5), (1-.5**2)**(-0.5))
    #print('passed arcsine test')
    
def test_arccos():
    x = CMobject(0.5)
    f = CMfunc.arccos(x)
    assert (f.val,f.der) == (np.arccos(.5), -(1-.5**2)**(-0.5))
    #print('passed arccosine test')
    
def test_arctan():
    x = CMobject(3)
    f = CMfunc.arctan(x)
    assert (f.val,f.der) == (np.arctan(3), (1+3**2)**(-2))
    #print('passed arctangent test')
    
def test_logistic():
    x = CMobject(2,3)
    f = CMfunc.logistic(x)
    assert (f.val,f.der) == (0.8807970779778823, 0.3149807562105195)
    #print('passed logistic test')
    
def test_tanh():
    x = CMobject(2)
    f = CMfunc.tanh(x)
    assert (f.val,f.der) == (0.964027580075817, 0.07065082485316435)
    # (np.tanh(2), np.cosh(2)**(-2))
    #print('passed hyperbolic tangent (and therefore sinh and cosh)')

def test_difficult_derivative_case():
    x1 = CMobject(1.0)

    ## the following is a test case for: sin(tan(x)) + 2^(cos(x)) + sin(x)^tan(x)^exp(x) - (cos(x))^2, seeded at x = 1. Try it in autograd, it works.
    test_func1 = CMfunc.sin(CMfunc.tan(x1)) + 2**(CMfunc.cos(x1)) + CMfunc.sin(x1)**CMfunc.tan(x1)**CMfunc.exp(x1) - CMfunc.cos(x1)**2
    print("test_func1 val, der: {}, {}".format(test_func1.val, test_func1.der))
    assert (test_func1.val,test_func1.der) == ( 2.724678163898656, -1.0139897786023675)
    print("Difficult derivative test passed.")

def test_object_input_error():
    with pytest.raises(ValueError):
        CMobject(1, 'fake')

def test_CMfunc_constant():
    assert CMfunc.sin(2) == np.sin(2)
    assert CMfunc.cos(5) == np.cos(5)
    assert CMfunc.tan(9) == np.tan(9)
    assert CMfunc.arcsin(.5) == np.arcsin(.5)
    assert CMfunc.arccos(.4) == np.arccos(.4)
    assert CMfunc.arctan(.1) == np.arctan(.1)
    assert CMfunc.exp(3) == np.exp(3)
    assert CMfunc.log(74088,42) == np.log(74088)/np.log(42) #using alternative base
    
    print('passed constants test')

def test_log_CMfunc():
    x = CMobject(2)
    f = CMfunc.log(x) # using natural logarithm
    number = 74088
    base = 42
    res = CMfunc.log(number,base) #using alternative base
    assert (f.val,f.der) == (0.6931471805599453, 0.5)
    assert res == 3.0

def test_newtons_method():
    # define newton's method to work with CMobject and FuncObj
    def newt(f,x,tol= 1e-10,max_it=100):

        for i in range(max_it):
            dx = -f(x).val/f(x).der # Update Delta x_{k}
            if np.abs(dx) < tol: # Stop iteration if solution found
                print(f"root found at: x={x.val} after {i+1} iterations.")
                print("Newton's Method test passed.")
                root = x.val
                return root
                break
            else:
                x += dx #update x

    # TEST CASE FOR f(x) = x^2 + ln(x) + x
    def f(x): # define function
        return x**2 + CMfunc.log(x) + x

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
    test_sin()
    test_arcsin()
    test_arccos()
    test_arctan()
    test_logistic()
    test_tanh()
    test_object_input_error()
    test_CMfunc_constant()
    test_log_CMfunc()
    test_difficult_derivative_case()
    test_newtons_method()
    print('...all tests run successfully!')

test_all()

#if __name__ == "__main__":
#    print("Here")
