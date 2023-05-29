import math
def menu():
    type=int(input('Выберите тип решаемой задачи: \n\t1 - Численное интегрирование\n'))
    if type==1:
        method=int(input('Выберите численный метод: \n\t1 - Метод прямоугольников левых частей \n\t2 - Метод прямоугольников правых частей\
        \n\t3 - Метод трапеций \n\t4 - Метод парабол\n'))
        if not method in range(1,5):
            print("Нет такого метода!")
        else:
            algorithm=int(input('Выберите алгоритм: \n\t1 - С постоянным шагом \n\t2 - С переменным шагом\n'))
            if algorithm==1:
                a=float(input('Введите нижний предел интегрирования\n'))
                b=float(input('Введите верхний предел интегрирования\n'))
                n=int(input('Введите количество разбиений\n'))
                method_call(method, algorithm, n, a, b)
            elif algorithm==2:
                a=float(input('Введите нижний предел интегрирования\n'))
                b=float(input('Введите верхний предел интегрирования\n'))
                n=int(input('Введите количество разбиений\n'))
                method_call(method, algorithm, n, a, b)
            else:
                print("Нет такого алгоритма!")
    else:
        print("Нет такого типа!")


def method_call(method, algorithm, n, a, b):
    if method==1 and algorithm==1:
        left_rectangle_const(n,a,b)
    elif method==1 and algorithm==2:
        left_rectangle_var(n,a,b)
    elif method==2 and algorithm==1:
        right_rectangle_const(n,a,b)
    elif method==3 and algorithm==1:
        trapeze_const(n,a,b)
    elif method==4 and algorithm==1:
        parabola_const(n,a,b)


def left_rectangle_const(n,a,b):
    h=(b-a)/n
    x=a
    s=0
    while (x<=(b-h)):
        s+=(math.sqrt(0.6*x+1.5))/(2*x+math.sqrt(x**2+3))
        x+=h
    print('Значение интеграла функции равно ' + str(h*s)[:8:])
    print('Шаг равен '+str(h))


def left_rectangle_var(n,a,b):
    e=10**(-6)
    h=(b-a)/n
    In = 0
    I2n = 0
    r = 1

    while (r > e):
        S2 = 0
        x = a
        while (x <= (b - h)):
            S2 += (math.sqrt(0.6*x+1.5))/(2*x+math.sqrt(x**2+3))
            x += h
        I2n = h * S2
        r = abs(I2n - In)
        In = I2n
        h = h / 2
    print("Значение интеграла: " + str(I2n))
    print("Шаг равен "+ str(h+h))


def right_rectangle_const(n,a,b):
    h=(b-a)/n
    x=a+h
    s=0
    while x<=b:
        s+=math.sqrt(0.6*x+1.5)/(2*x+math.sqrt(x**2+3))
        x+=h
    print('Значение интеграла функции равно ' + str(h*s)[:8:])
    print('Шаг равен '+str(h))


def trapeze_const(n,a,b):
    h=(b-a)/n
    x=a+h
    s=0
    while x<=(b-h):
        s+=math.sqrt(0.6*x+1.5)/(2*x+math.sqrt(x**2+3))
        x+=h
    f_a_b=math.sqrt(0.6*a+1.5)/(2*a+math.sqrt(a**2+3))+math.sqrt(0.6*b+1.5)/(2*b+math.sqrt(b**2+3))
    print('Значение интеграла функции равно ' + str(h*(f_a_b/2+s))[:8:])
    print('Шаг равен '+str(h))


def parabola_const(n,a,b):
    h=(b-a)/(2*n)
    x=a+h
    s1=0
    s2=0
    while x<=(b-h):
        s1+=math.sqrt(0.6*x+1.5)/(2*x+math.sqrt(x**2+3))
        x+=2*h
    x=a+2*h
    while x<=(b-2*h):
        s2+=math.sqrt(0.6*x+1.5)/(2*x+math.sqrt(x**2+3))
        x+=2*h
    f_a_b=math.sqrt(0.6*a+1.5)/(2*a+math.sqrt(a**2+3))+math.sqrt(0.6*b+1.5)/(2*b+math.sqrt(b**2+3))
    print('Значение интеграла функции равно ' + str((h/3)*(s1*4+s2*2+f_a_b))[:8:])
    print('Шаг равен '+str(h))


menu()