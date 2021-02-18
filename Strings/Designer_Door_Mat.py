n,m=map(int,input().split())


a='-'
b='.|.'

for i in range(1,n,2):
    upper = a*((m-(len(b)*i))//2)   +   b*(i)   +   a*((m-(len(b)*i))//2)
    print(upper)
    

print( a*((m-len('WELCOME'))//2)  +   'WELCOME'   +   a*((m-len('WELCOME'))//2))
#            print(middle)




for i in range(n-2,0,-2):
    lower = a*((m-(len(b)*i))//2)   +   b*(i)   +   a*((m-(len(b)*i))//2)
    print(lower)

