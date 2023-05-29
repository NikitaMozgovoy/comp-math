import math
def f(x):
    return (3**(x-1)-4-x)
def dichotomy(a, b, e):
    x = (a + b) / 2
    if ( (f(a) * f(x)) < 0):
        if (abs(x - a) <= e ):
            return x
        return dichotomy(a, x, e)

    if ( (f(x) * f(b)) < 0):
        if (abs(b - x) <= e ):
            return x
        return dichotomy(x, b, e)

    if ( f(a) == 0 ):
        return a
    elif ( f(b) == 0 ):
        return b
    else: 
        return x
    
a=-10
b=10
e=10**(-6)    
print(dichotomy(a, b, e))