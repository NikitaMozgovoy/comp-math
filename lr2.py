import math
a=0
b=math.pi/2
c=0
d=math.pi/4
print('Пределы интегрирования по x: 0, пи/2')
print('Пределы интегрирования по y: 0, пи/4')
print('Введите число разбиений nx, ny')
nx, ny = (int(input()) for _ in range(2))
hx=(b-a)/nx
hy=(d-c)/ny
print('Шаг по x равен ', hx)
print('Шаг по y равен ', hy)
sx=0
x=a
while x<=(b-hx):
    sy=0
    y=c
    while y<=(d-hy):
        sy+=abs(math.sin(x+y))
        y+=hy
    print('sy = ', sy)
    Iy=hy * sy
    print('Iny = ', Iy)
    sx+=Iy
    x+=hx
print("sx = ", sx)
Ix=hx*sx
print("Inx = ", Ix)
