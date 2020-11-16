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
    def __init__(self, val, der = 1.0):
        try:       
            self.val = float(val)
            self.der = float(der)
        except ValueError:
            print('ValueError: val and der must be real numbers.')
    
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

    # generalized version of f(x)^g(x) from 
    # https://math.stackexchange.com/questions/1588166/derivative-of-functions-of-the-form-fxgx
    # h(x) = f(x)^g(x)
    # h'(x) = (f(x)^g(x))*(g'(x)*ln(f(x))+(g(x)*f'(x))/f(x))
    def __pow__(self, other):  
    
        try:
            return CMobject(self.val**other.val, (self.val**other.val)*(other.der*np.log(np.abs(self.val))+(other.val*self.der)/self.val)) 
        except AttributeError:
            other = CMobject(other, 0) #derivative of a constant is zero
            return CMobject(self.val**other.val, (self.val**other.val)*(other.der*np.log(np.abs(self.val))+(other.val*self.der)/self.val))
               
        
    def __rpow__(self,other):
    
        try:
            return CMobject(other.val**self.val, (other.val**self.val)*(self.der*np.log(np.abs(other.val))+(self.val*other.der)/other.val)) 
        except AttributeError:
            other = CMobject(other, 0) #derivative of a constant is zero
            return CMobject(other.val**self.val, (other.val**self.val)*(self.der*np.log(np.abs(other.val))+(self.val*other.der)/other.val))