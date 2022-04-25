a = int(input())
for _ in range(a):
    a,b,c,d=map(int , input().split())
    if a-b == b-c:
        e = (b-a)+d
    else:
        e = (b//a)*d
    print(a,b,c,d,e)