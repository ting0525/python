a,b,c = map(int, input().split(' '))    
if (b**2) - (4*a*c) == 0:
    n = int(-b)/(2*a)
    print("Two same roots x=%d" %(n))
elif (b**2) - (4*a*c) > 0:
    n = int(-b)/(2*a)
    m = int((b**2) - (4*a*c)) ** 0.5 / (2*a)
    x1 = int(n+m)
    x2 = int(n-m)
    print("Two different roots x1=%d , x2=%d" %(x1 , x2))
else:
    print("No real root")
