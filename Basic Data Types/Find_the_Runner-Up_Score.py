n=int(input())
arr=list(map(int,input().strip().split()))

arr.sort(reverse=True)

for i in range(n):
    if arr[i]!=arr[i+1]:
        print(arr[i+1])
        break
        
            
         


