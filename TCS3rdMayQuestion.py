def solve(arr):
    n=len(arr)
    largest,maxDiff=float('-inf'),float('-inf')
    for i in range(n):
        num=int(arr[i])
        largest=max(largest,num)
        maxDiff=max(maxDiff,largest-num)
    return maxDiff

def input_array_format():
    arr=list(map(str,input().strip("[]").split(',')))
    return arr
 
# Driver Code
# u=input_array_format()
# print(solve(u))

 
N=int(input())
n=list(map(str,input().split()))
store={}
for shoesSize in n:
    if shoesSize in store:
        store[shoesSize]+=1
    else:
        store[shoesSize]=1

pairs=0
for key,val in store.items():
    if key[-1]=='L':
        val=key[:-1]+'R'
        if val in store:
            pairs+=min(store[key], store[val])
        else:
            val=key[:-1]+'L'
            if val in store:
                pairs+=min(store[key],store[val])
                
print(pairs) 
   
        
