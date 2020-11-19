import pytest
import sys, os.path
AD_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(AD_dir)

import numpy as np
from function_library import function_library as function_library
from CMobject import CMobject as CM
from FuncObj import FuncObj as FuncObj
# import sys, os.path
# AD_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# + '/CMAutoDiff/')
# sys.path.append(AD_dir)

#import CMobject

#from ...CMAutoDiff.CMobject import CMobject

def test_basic_operation():
    x = CM(-3.)
    f = x**3+2*x
    assert (f.val,f.der) == (-33, 29)

def difficult_derivative_case():    
    x1 = CM(1.0)

    ## the following is a test case for: sin(tan(x)) + 2^(cos(x)) + sin(x)^tan(x)^exp(x) - (cos(x))^2, seeded at x = 1. Try it in autograd, it works.
    test_func1 = FuncObj('sin', FuncObj('tan', x1)) + 2**(FuncObj('cos', x1)) + FuncObj('sin', x1)**(FuncObj('tan', x1))**(FuncObj('exp', x1)) - FuncObj('cos', x1)**2
    print("test_func1 val, der: {}, {}".format(test_func1.val, test_func1.der))

if __name__ == "__main__":
    print("Here")