import math
def f(x0,e):
    r=1
    i=0
    while r>e:
        x1=x0-(3**(x0-1)-4-x0)/(math.log(3)*3**(x0-1)-1)
        r=abs(x0-x1)
        x0=x1
        i+=1
    print('Количество итераций равно ' + str(i))
    return (x1) 

a=-10
b=10
print('Корень уравнения при левом конце интервала изоляции как начальном корне равен ' + str(f(a, 0.000001)))
print('Корень уравнения при правом конце интервала изоляции как начальном корне равен ' + str(f(b, 0.000001)))
