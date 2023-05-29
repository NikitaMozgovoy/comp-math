from math import fabs
def f(x):
    return 3**(x-1)-4-x
a = -10
b = 10
x0 = a - (f(a) - (b - a)) / (f(b) - f(a))
r = None
x = 0
e = 10 ** -6
while True:
    if (f(x0) * f(b) < 0):
        x = x0 - f(x0) / (f(b) - f(x0)) * (b - x0)
    if (f(x0) * f(a) < 0):
        x = x0 - f(x0) / (f(x0) - f(a)) * (x0 - a)
    r = fabs(x - x0)
    x0 = x
    if (r <= e):
        break
    
print("Точность: ", e)
print("Результат: ", x)


