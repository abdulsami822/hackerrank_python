for _ in range(int(input())):
    x,a,y,b=(set(map(int,input().split())) for _ in range(4))
    print(a&b==a)
    

