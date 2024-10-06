def maximumWindow(arr,k):
    ans=[]
    n=len(arr)
    for i in range(0,n-k+1):
        maximum=arr[i]
        for j in range(i,i+k):
            maximum=max(maximum,arr[j])
        ans.append(maximum)
    return ans 
    
arr=list(map(int,input().split()))
k=int(input())
print(maximumWindow(arr,k))