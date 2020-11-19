import pytest
from CMAutoDiff.CMobject import CMobject

def test_basic_operation():
    x = CMobject(-3.)
    f = x**3+2*x
    assert (f.val,f.der) == (-33, 29)

