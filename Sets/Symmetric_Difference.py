m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))


c=sorted(list(a-b)+list(b-a))

for i in range(len(c)):
    print(c[i])

