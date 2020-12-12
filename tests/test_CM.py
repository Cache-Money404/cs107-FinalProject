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
from io import StringIO
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import numpy as np

from CMAutoDiff.CMGradobject import CMGobject as CMG
from CMAutoDiff.CMGradobject import CMvector as CMV
import CMAutoDiff.CMfunc as CMfunc
import CMAutoDiff.CMflow as CMflow
import CMAutoDiff.ui as UI


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
    assert np.array_equal(np.round(f.grad, 12), np.round(np.array([0.07065082485316432, 0.]), 12) ) ## relaxing to floating point precision
    # (np.tanh(2), np.cosh(2)**(-2))
    #print('passed hyperbolic tangent (and therefore sinh and cosh)')


def test_difficult_derivative_case():
    x1 = CMG(1.0)

#     ## the following is a test case for: sin(tan(x)) + 2^(cos(x)) + sin(x)^tan(x)^exp(x) - (cos(x))^2, seeded at x = 1. Try it in autograd, it works.
    test_func1 = CMfunc.sin(CMfunc.tan(x1)) + 2**(CMfunc.cos(x1)) + CMfunc.sin(x1)**CMfunc.tan(x1)**CMfunc.exp(x1) - CMfunc.cos(x1)**2
    print("test_func1 val, der: {}, {}".format(test_func1.val, test_func1.grad))
    assert (np.round(test_func1.val, 8),np.round(test_func1.grad, 8)) == ( np.round(2.7246781638986564, 8), np.round(-1.0139897786023675, 8))
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

def test_CMV_init():
    x1 = CMG(1, np.array([1, 0, 0, 0]))
    x2 = CMG(2, np.array([0, 1, 0, 0]))
    x3 = CMG(3, np.array([0, 0, 1, 0]))
    x4 = CMG(4, np.array([0, 0, 0, 1]))
    
    F1_list = [CMfunc.cos(x1 - 2*x2), CMfunc.log(x3) - 3*x4*x3, x2**2, (x1 + x2)/(x3 - x4)  ]
    F1 = CMV(F1_list)
    assert F1.__repr__() == 'CMvector(val = [ -0.9899925  -34.90138771   4.          -3.        ], \n jacobian = [[  0.14112001  -0.28224002   0.           0.        ]\n [  0.           0.         -11.66666667  -9.        ]\n [  0.           4.           0.           0.        ]\n [ -1.          -1.          -3.           3.        ]])'
    assert np.array_equal(F1.val, np.array([ -0.9899924966004454, -34.90138771133189,   4.,  -3.]))

def test_CMV_add_sub():
    x1 = CMG(1, np.array([1, 0, 0, 0]))
    x2 = CMG(2, np.array([0, 1, 0, 0]))
    x3 = CMG(3, np.array([0, 0, 1, 0]))
    x4 = CMG(4, np.array([0, 0, 0, 1]))

    x5 = CMG(1, np.array([1,0]))
    x6 = CMG(2, np.array([0,1]))


    F1_list = [CMfunc.cos(x1 - 2*x2), CMfunc.log(x3) - 3*x4*x3, x2**2, (x1 + x2)/(x3 - x4)  ]
    F2_list = [2*x3 + CMfunc.cos(x1 - 2*x2), 3*x4 - x3, x2**x4, 1/(x3 - x4)  ]
    F1 = CMV(F1_list)
    F2 = CMV(F2_list)
    F3 = F1 + F2
    F4 = F2 + F1
    F5 = F2 - F1 - F1
    F6 = CMV([x5*x6, x6])
    F7 = F6 + x5
    F8 = F6 - x6

    assert np.array_equal(F3.val, np.array([ 4.02001500679911, -25.901387711331893,  20.,  -4.]))
    assert np.array_equal(F3.jac, np.array([[  0.2822400161197344,  -0.5644800322394689,   2.        ,   0.        ],
       [  0.        ,   0.        , -12.666666666666666,  -6.        ],
       [  0.        ,  36.        ,   0.        ,  11.090354888959125],
       [ -1.        ,  -1.        ,  -4.        ,   4.        ]]))
    assert np.array_equal(F4.val, np.array([ 4.02001500679911, -25.901387711331893,  20.,  -4.]))
    assert np.array_equal(F4.jac, np.array([[  0.2822400161197344,  -0.5644800322394689,   2.        ,   0.        ],
       [  0.        ,   0.        , -12.666666666666666,  -6.        ],
       [  0.        ,  36.        ,   0.        ,  11.090354888959125],
       [ -1.        ,  -1.        ,  -4.        ,   4.        ]]))
    assert np.array_equal(F5.val, np.array([6.989992496600445, 78.80277542266379, 8., 5. ]))
    assert np.array_equal(F5.jac, np.array([[-0.1411200080598672,  0.2822400161197344,  2.        ,  0.        ],
       [ 0.        ,  0.        , 22.333333333333332, 21.        ],
       [ 0.        , 24.        ,  0.        , 11.090354888959125],
       [ 2.        ,  2.        ,  5.        , -5.        ]]))
    assert np.array_equal(F7.val, np.array([3.,3.]))
    assert np.array_equal(F7.jac, np.array([[3., 1.],
       [1., 1.]]))

    assert np.array_equal(F8.val, np.array([4.,4.]))
    assert np.array_equal(F8.jac, np.array([[2., 0.],
       [0., 0.]]))

def test_CMV_val_err():
    x5 = CMG(1, np.array([1,0]))
    x6 = CMG(2, np.array([0,1]))
    F6 = CMV([x5*x6, x6])
    with pytest.raises(ValueError):
        x5 + F6
    with pytest.raises(ValueError):
        F6 + 5
    with pytest.raises(ValueError):
        5 + F6
    with pytest.raises(ValueError):
        5 - F6
    with pytest.raises(ValueError):
        F6 - 5

############### TESTS FOR CMflow ###############

def test_CMF_cart2pol():
    polar = CMflow.cart2pol(np.array([[1, 1]]))
    assert np.array_equal(np.round(polar[0], 8), np.round(np.array([np.sqrt(2), np.pi / 4]), 8))

def test_CMF_cart2pol_zero():
    polar = CMflow.cart2pol(np.array([[0, 1]]))
    assert np.array_equal(np.round(polar[0], 8), np.round(np.array([1, np.pi / 2]), 8))

def test_CMF_pol2cart():
    cart = CMflow.pol2cart(np.array([[np.sqrt(2), np.pi / 4]]))
    assert np.array_equal(np.round(cart, 8), np.array([[1, 1]]))

def test_CMF_pol2cart_grad():
    grad = CMflow.pol2cart_grad(np.array([[2, np.pi / 3]]), np.array([[1, 0]]))
    # assert np.array_equal(np.round(grad, 8), np.round(np.array([2, ]), 8))
    # assert shape, type
    assert (grad.shape[0], grad.shape[1]) == (1, 2)

def test_CMF_flow_it():
    flow = CMflow.Flow_it(np.array([1, 1]))
    assert isinstance(flow.flow, np.ndarray)
    assert flow.max_it == 2
    assert list(iter(flow)) == [1, 1]
    assert list(iter(flow + np.array([1, 0]))) == [2, 1]

def test_CMF_flow():
    flow = CMflow.Flow('1', np.array([1, 2]))
    assert flow._key == '1'
    assert flow._strength == 1
    assert isinstance(flow.rule_out_points(np.array([[1, 0]])), np.ndarray)

def test_CMF_uniform():
    uni = CMflow.uniform('1', np.array([1, 2]))
    assert isinstance(uni.rule_out_points(np.array([[1, 0]])), np.ndarray)
    assert isinstance(uni.compute_flow(), CMflow.Flow_it)

## Questions: why at least three inputs in init ##
def test_CMF_source():
    src = CMflow.source('1', np.array([1, 2, 3]))
    assert isinstance(src.rule_out_points(np.array([[1, 0]])), np.ndarray)
    assert isinstance(src.compute_flow(), CMflow.Flow_it)

def test_CMF_sink():
    sink = CMflow.sink('1', np.array([1, 2, 3]))
    assert isinstance(sink, CMflow.sink)

def test_CMF_vortex():
    vor = CMflow.vortex('1', np.array([1, 2, 3]))
    assert isinstance(vor.rule_out_points(np.array([[1, 0]])), np.ndarray)
    assert isinstance(vor.compute_flow(), CMflow.Flow_it)

def test_CMF_doublet():
    dou = CMflow.doublet('1', np.array([1, 2, 3]))
    assert isinstance(dou.compute_flow(), CMflow.Flow_it)

def test_CMF_tornado():
    tor = CMflow.tornado('1', np.array([1, 2, 3, 4]))
    assert isinstance(tor.compute_flow(), CMflow.Flow_it)

def test_CMF_whirlpool():
    assert isinstance(CMflow.whirlpool('1', np.array([1, 2, 3, 4])), CMflow.whirlpool)

def test_CMF_identify():
    assert isinstance(CMflow.identify_flow('source', np.array([1, 2, 3])), CMflow.source)

def test_CMF_generate():
    gradients_cart, phi = CMflow.generate_cart_gradients([CMG(3, np.array([1,0]))], np.array([[1, 0]]))
    assert isinstance(gradients_cart, np.ndarray)
    assert isinstance(phi, np.ndarray)

def test_CMF_main(monkeypatch):
    #monkeypatch.setattr('sys.stdin', StringIO('-1\n1\n-1\n1\n1\n1\n13\n2\n2\n'))
    monkeypatch.setattr('sys.stdin', StringIO('-1\n1\n-1\n1\n1\n1\n8\n2\n2\n'))
    CMflow.main()

############### TESTS FOR UI ###############

def test_UI_graphdim(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('-1\n1\n-1\n1\n'))
    ui_dim = UI.graphDim()
    assert isinstance(ui_dim, list)

def test_UI_interface(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('9\n1\n1\n2\n2\n2\n2\n3\n3\n3\n3\n3\n4\n4\n4\n4\n4\n5\n5\n5\n5\n6\n6\n6\n6\n6\n7\n7\n7\n7\n7\n8\n'))
    interface = UI.Interface()
    assert isinstance(interface, dict)


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

    test_CMV_init()
    test_CMV_add_sub()
    test_CMV_val_err()
    print('..all CMvector tests run successfully!')

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

    test_CMF_cart2pol()
    test_CMF_cart2pol_zero()
    test_CMF_pol2cart()
    test_CMF_pol2cart_grad()
    test_CMF_flow_it()
    test_CMF_flow()
    test_CMF_uniform()
    test_CMF_source()
    test_CMF_sink()
    test_CMF_vortex()
    test_CMF_doublet()
    test_CMF_tornado()
    test_CMF_whirlpool()
    test_CMF_identify()
    test_CMF_generate()
    print('..all CMflow tests run successfully!')



test_all()
# if __name__ == "__main__":
#     print("Here")
#     test_all()
