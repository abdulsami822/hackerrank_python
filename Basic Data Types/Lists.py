def insert(b,lis):
    lis.insert(b[0],b[1])

def prin(b,lis):
    print(lis)
def remov(b,lis):
    lis.remove(b[0])
def appen(b,lis):
    lis.append(b[0])
def sor(b,lis):
    lis.sort()
def po(b,lis):
    lis.pop()
def revers(b,lis):
    lis.reverse()

def optioner(a,b,lis):
    switcher={
        'insert':insert,
        'print':prin,
        'remove':remov,
        'append':appen,
        'sort':sor,
        'pop':po,
        'reverse':revers    
        }
    fun=switcher.get(a,'nikall')
    fun(b,lis)

n=int(input())
lis=[]
for _ in range(0,n):
    a,*b=input().split()
    b=list(map(int,b))
    optioner(a,b,lis)

