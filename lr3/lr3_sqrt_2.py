x=float(input('Введите x: '))
y0=float(input('Введите начальный y: '))
e=float(input('Введите точность: '))
y=0
while abs((y0-y))>e:
    y=(y0/2)*(3-x*y0*y0)
    y0=y
print(f'{y}')