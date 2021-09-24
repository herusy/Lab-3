from math import sqrt
print('Введіть а,b,c для квадратного рівняння ax2+bx+c=0')
a = float(input())
b = float(input())
c = float(input())
d = b**2-4*a*c
if d>0:    
    x1 = ((-b) - sqrt(d))/(2*a)
    x2 = ((-b) + sqrt(d))/(2*a) 
if d>0:
    if x1>x2:
        print(x2)
        print(x1)
    else:
        print(x1)
        print(x2)
elif d==0:
    print((-b)/(2*a))
elif d<0:
    print('Коренів немає')
