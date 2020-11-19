import numpy as np
import pytest
from function_library import function_library
from CMobject import CMobject
from FuncObj import FuncObj


def test_basic_operation():
    x = CMobject(-3.)
    f = x**3+2*x
    assert (f.val,f.der) == (-33, 29)

def difficult_derivative_case():    
    x1 = CMobject(1.0)

    ## the following is a test case for: sin(tan(x)) + 2^(cos(x)) + sin(x)^tan(x)^exp(x) - (cos(x))^2, seeded at x = 1. Try it in autograd, it works.
    test_func1 = FuncObj('sin', FuncObj('tan', x1)) + 2**(FuncObj('cos', x1)) + FuncObj('sin', x1)**(FuncObj('tan', x1))**(FuncObj('exp', x1)) - FuncObj('cos', x1)**2
    print("test_func1 val, der: {}, {}".format(test_func1.val, test_func1.der))