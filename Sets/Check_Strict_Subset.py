x=set(map(int,input().split()))
a=True
for _ in range(int(input())):
    y=(set(map(int,input().split())))
    if not(y.issubset(x) and x!=y):
        a=False
print(a)

