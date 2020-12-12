# import pytest
# import sys, os.path
# AD_dir = os.path.abspath(os.path.dirname(__file__)) # needed so pytest works correctly
# sys.path.append(AD_dir) # needed so pytest works correctly

# import numpy as np
# from function_library import function_library
# from CMG import CMG
# from FuncObj import FuncObj

import pytest
import sys, os.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import numpy as np

from CMAutoDiff.CMGradobject import CMGobject as CMG
import CMAutoDiff.CMfunc as CMfunc
import CMAutoDiff.CMflow as CMflow


############### TESTS FOR CMGradobject ###############

def test_repr_CMG():
    x = CMG(3, np.array([1,0]))
    assert x.__repr__() == 'CMGobject(val = 3.0, grad = [1 0])'

def test_object_input_error_CMG():
    with pytest.raises(ValueError):
        CMG('fake', np.array([0,1]))


def test_eq_CMG():
    x = CMG(3, np.array([1,0]))
    assert CMG(3, np.array([1,0])) == x
    assert CMG(4, np.array([1,0])) != x
    assert 3 != x

def test_mul_CMG():
    x = CMG(-3, np.array([1,0]))
    f = x**3+2*x
    assert f.val, f.grad == -33.0
    assert np.array_equal(f.grad,np.array([29.,  0.]))

def test_add_sub_operations_CMG():
    x = CMG(1, np.array([1,0]))
    f = x + 2 + x + x + x - 1 - x - x - x
    f2 = 2 + x
    f3 = 10 - x
    assert f.val == 2.0
    assert np.array_equal(f.grad,np.array([1., 0.]))
    assert f2.val == 3.0
    assert np.array_equal(f2.grad,np.array([1., 0.]))
    assert f3.val == 9.0
    assert np.array_equal(f3.grad,np.array([-1., 0.]))

def test_div_operations_CMG():
    x = CMG(1, np.array([1,0]))
    f = x/(3*x + 1) - x/5 + 5/x
    assert f.val == 5.05
    assert np.array_equal(f.grad,np.array([-5.1375, 0.]))

def test_pow_operations_CMG():
    x = CMG(1, np.array([1,0]))
    f = x**2 + 2**x + x**x**x**2**x
    x2 = CMG(3.0, np.array([1,0]))
    f2 = x2.__rpow__(x2)
    assert  f.val  == 4.0
    assert np.array_equal(f.grad,np.array([4.386294361119891, 0.]))
    assert f2.val == 27.0
    assert np.array_equal(f2.grad,np.array([56.66253179403897, 0.]))

def test_negation_CMG():
    x = CMG(1, np.array([0,1]))
    y = -x
    assert y.val == -1.0
    assert np.array_equal(y.grad,np.array([0, -1]))


############### TESTS FOR CMfunc ###############

def test_sin():
    x = CMG(2)
    f = CMfunc.sin(x)
    assert f.val == np.sin(2)
    assert np.array_equal(f.grad,np.array([np.cos(2)]))
    #print('passed sine test')

def test_arcsin():
    x = CMG(0.5)
    f = CMfunc.arcsin(x)
    assert (f.val,f.grad) == (np.arcsin(.5), (1-.5**2)**(-0.5))
    #print('passed arcsine test')

def test_arccos():
    x = CMG(0.5)
    f = CMfunc.arccos(x)
    assert f.val == np.arccos(.5)
    assert np.array_equal(f.grad,np.array([-(1-.5**2)**(-0.5)]))
    #print('passed arccosine test')

def test_arctan():
    x = CMG(3)
    f = CMfunc.arctan(x)
    assert f.val == np.arctan(3)
    assert np.array_equal(f.grad,np.array([(1+3**2)**(-2)]))
    #print('passed arctangent test')

def test_logistic():
    x = CMG(2,np.array([3,0]))
    f = CMfunc.logistic(x)
    assert f.val == 0.8807970779778823
    assert np.array_equal(f.grad,np.array([0.3149807562105195, -0.]))
    #print('passed logistic test')

def test_tanh():
    x = CMG(2., np.array([1.,0.], dtype=np.double ))
    f = CMfunc.tanh(x)
    assert f.val == 0.964027580075817
    assert np.array_equal(f.grad, np.array([0.0706508248531643, 0.]))
    # (np.tanh(2), np.cosh(2)**(-2))
    #print('passed hyperbolic tangent (and therefore sinh and cosh)')


def test_difficult_derivative_case():
    x1 = CMG(1.0)

#     ## the following is a test case for: sin(tan(x)) + 2^(cos(x)) + sin(x)^tan(x)^exp(x) - (cos(x))^2, seeded at x = 1. Try it in autograd, it works.
    test_func1 = CMfunc.sin(CMfunc.tan(x1)) + 2**(CMfunc.cos(x1)) + CMfunc.sin(x1)**CMfunc.tan(x1)**CMfunc.exp(x1) - CMfunc.cos(x1)**2
    print("test_func1 val, der: {}, {}".format(test_func1.val, test_func1.grad))
    assert (test_func1.val,test_func1.grad) == ( 2.724678163898656, -1.0139897786023675)
    print("Difficult derivative test passed.")


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
    x = CMG(2)
    f = CMfunc.log(x) # using natural logarithm
    number = 74088
    base = 42
    res = CMfunc.log(number,base) #using alternative base
    assert f.val== 0.6931471805599453
    assert np.array_equal(f.grad, np.array([0.5]))
    assert res == 3.0

    #print('passed log test')

def test_sqrt():
    x = CMG(2)
    f = CMfunc.sqrt(x)
    assert f.val == 2**.5
    assert np.array_equal(f.grad, np.array([0.5*(2**(-.5))]))

def test_newtons_method():
    # define newton's method to work with CMG and FuncObj
    def newt(f,x,tol= 1e-10,max_it=100):

        for i in range(max_it):
            dx = -f(x).val/f(x).grad # Update Delta x_{k}
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

    x = CMG(1)
    result = newt(f,x)
    assert result == 0.4858388639605664




############### TESTS FOR CMvector ###############











def test_all():
    print('Running tests...')
    print('''    (all basic tests results suppressed except difficult derivative and Newton's method)''')

    test_repr_CMG()
    test_object_input_error_CMG()
    test_eq_CMG()
    test_mul_CMG()
    test_add_sub_operations_CMG()
    test_div_operations_CMG()
    test_pow_operations_CMG()
    test_negation_CMG()
    print('...all CMGradobject tests run successfully!')
    test_sin()
    test_arcsin()
    test_arccos()
    test_arctan()
    test_logistic()
    test_tanh()
    test_difficult_derivative_case()
    test_CMfunc_constant()
    test_log_CMfunc()
    test_sqrt()
    test_newtons_method()
    print('..all CMfunc tests run successfully!')


test_all()

# if __name__ == "__main__":
#     print("Here")
#     test_all()
