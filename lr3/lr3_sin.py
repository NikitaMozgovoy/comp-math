n=10
e=6*10**(-9)
x=0.5
a=[1, 1.000000002, 1, -0.166666589, 1, 0.008333075, 1, -0.000198107, 1, 0.000002608]
c= 0
p=1
for k in range(1, n):
    if k%2==0:
        pass
    else:
        p=x**k
        u=p * a[k]
        print(u)
        c+=u
        if abs(u)<=e:
            print("c = %f" %c)
            print("K = %f" %k)
            break
        print("Требуемая точность не достигнута")