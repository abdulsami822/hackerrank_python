def sortSecond(val): 
    return val[1]  


n=int(input())

p=list()

q=list()

for i in range(n):
    name=input()
    score=float(input())
    q=[]
    q.extend([[name,score]])
    
    p.extend(q)


p.sort(key=sortSecond , reverse=True)






for i in range(n-1,-1,-1):
    
    if p[i][1]!=p[i-1][1]:
        sec_low_grade=p[i-1][1]
        break

final_list=list()

for i in range(0,n):
    if p[i][1]==sec_low_grade:
        final_list.extend([p[i][0]])    

final_list.sort()

for i in final_list:
    print(i)   
    
    
    

