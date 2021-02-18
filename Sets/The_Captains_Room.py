input()

s=list(map(int,input().split()))

s1=set()
s2=set()

for i in s:
    if not i in s1:
        s1.add(i)
    else:
        s2.add(i)
print((s1-s2).pop())

