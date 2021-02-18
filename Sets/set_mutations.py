n=int(input())
a=set(map(int,input().split()))
for _ in range(int(input())):
    cmd,l=input().split()
    b=set(map(int,input().split()))
    eval('a.{}(b)'.format(cmd))
print(sum(a))

