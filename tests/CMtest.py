import pytest
import sys, os.path
AD_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/CMAutoDiff/')
sys.path.append(AD_dir)

import CMobject

#from ...CMAutoDiff.CMobject import CMobject


def test_basic_operation():
    x = CMobject(-3.)
    f = x**3+2*x
    assert (f.val,f.der) == (-33, 29)

