import numpy as np

class CMobject(): 
    """Creates a forward automatic differentiation class
    
    ATTRIBUTES
    ==========
    val : the value of the object
    der : the derivative of the object, default seed = 1.0
    
    EXAMPLES
    ========
    >>> x = CMobject(4)
    >>> x.val
    4
    >>> x.der
    1
    """
    #Constructor sets value and derivative
    def __init__(self, val, der = 1.0): #TODO not a valid entry (int/float)
            self.val = val
            self.der = der
    
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
        
    #TODO - DOUBLE CHECK POWER RULES esp. for similar to x^(2x+1) case

    def __pow__(self, other):
        
        if self.der == 0: # if constant, follow exponent rules d/dx[a] = x'*ln(a)*a^x
            try:
                return CMobject(self.val**other.val, other.der*np.log(self.val)*(self.val**other.val))
            except AttributeError:
                other = CMobject(other, 0) #derivative of a constant is zero
                return CMobject(self.val**other.val, other.der*np.log(self.val)*(self.val**other.val))

        elif type(other) == int or type(other) == float: # if constant, follow power rules d/dx[x^a] = x'*a*x^(a-1)
            try:
                return CMobject(self.val**other.val, other.val*self.der*(self.val**(other.val - 1)))
            except AttributeError:
                other = CMobject(other, 0) #derivative of a constant is zero
                return CMobject(self.val**other.val, other.val*self.der*(self.val**(other.val - 1)))
        #TODO - ADD COMPLICATED CASE X^X or variety e.g. (2x)^(2x) OR x^(2x+1)
    
    # TODO ADD REVERSE POWER
    def __rpow__(self,other):
        pass