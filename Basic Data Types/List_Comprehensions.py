if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    f1= [x,y,z]

    f2=list()
    f2.extend([[i,j,k] for i in range(f1[0]+1)
                        for j in range(f1[1]+1)
                        for k in range(f1[2]+1)])

    f3=list()
    f3.extend(x for x in f2 if x[0]+x[1]+x[2]!=n)

    print(f3)

