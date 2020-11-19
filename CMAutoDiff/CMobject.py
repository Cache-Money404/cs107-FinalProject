import numpy as np

class CMobject():
    """Creates a forward automatic differentiation class:
        CMobject(val, der=1.0)

    INPUTS
    ======
    val : the value of the object
    der : the derivative of the object, default seed = 1.0
    
    RETURNS
    =======
    CMobject for forward automatic differentiation

    EXAMPLES
    ========
    >>> x = CMobject(4, 2)
    >>> x.val
    4
    >>> x.der
    2
    """
    #Constructor sets value and derivative
    def __init__(self, val, der = 1.0):
        try:
            self.val = float(val)
            self.der = float(der)
        except:
            raise ValueError('ValueError: val and der must be real numbers.')

            
    # overload methods to allow for addition of non-class values

    def __add__(self, other):
        try:
            return CMobject(self.val+other.val, self.der+other.der)
        except AttributeError:
            other = CMobject(other, 0) #derivative of a constant is zero
            return CMobject(self.val+other.val, self.der+other.der)

    def __radd__(self, other): #ensure commutativity of addition
        return self.__add__(other)

    def __mul__(self, other):
        try:
            return CMobject(self.val*other.val, self.val*other.der+other.val*self.der)
        except AttributeError:
            other = CMobject(other, 0) #derivative of a constant is zero
            return CMobject(self.val*other.val, self.val*other.der+other.val*self.der)

    def __rmul__(self, other):
        return self.__mul__(other)


    def __sub__(self,other):
        try:
            return CMobject(self.val-other.val, self.der-other.der)
        except AttributeError:
            other = CMobject(other, 0) #derivative of a constant is zero
            return CMobject(self.val-other.val, self.der-other.der)

    def __rsub__(self,other):
        try:
            return CMobject(other.val-self.val, other.der-self.der)
        except AttributeError:
            other = CMobject(other, 0) #derivative of a constant is zero
            return CMobject(other.val-self.val, other.der-self.der)

    # Quotient rule ((v*du/dx - u*dv/dx) / v^2)
    def __truediv__(self,other):
        try:
            return CMobject(self.val/other.val, (other.val*self.der - self.val*other.der)/(other.val**2))
        except AttributeError:
            other = CMobject(other, 0) #derivative of a constant is zero
            return CMobject(self.val/other.val, (other.val*self.der - self.val*other.der)/(other.val**2))

    def __rtruediv__(self,other):
        try:
            return CMobject(other.val/self.val, (self.val*other.der - other.val*self.der)/(self.val**2))
        except AttributeError:
            other = CMobject(other, 0) #derivative of a constant is zero
            return CMobject(other.val/self.val, (self.val*other.der - other.val*self.der)/(self.val**2))

    def __pow__(self, other):
        if isinstance(other, CMobject):
            return_val = (self.val)**(other.val)
            return_deriv = return_val*(other.der*(np.log(self.val)) + self.val**(-1)*(self.der)*other.val )
            return CMobject(return_val, return_deriv)
        else:
            return CMobject(self.val**other, other*(self.val)**(other-1)*self.der)
    
    def __rpow__(self, other):
        if isinstance(other, CMobject):
            return other.__pow__(self)
        else:
            return_val = (other)**(self.val)
            return_deriv = np.log(other)*(other)**(self.val)*self.der
            return CMobject(return_val, return_deriv)

    def __neg__(self):
        return CMobject(-self.val, -self.der)