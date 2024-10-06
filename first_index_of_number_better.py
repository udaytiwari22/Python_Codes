def first_indexB(a,x,si):
    l=len(a)   
    if(si==l):
        return -1
    if(a[si]==x):
        return si
    smaller_indexB_output= first_indexB(a,x,si+1)
    return smaller_indexB_output 
l=[]
n=int(input())
l=list(map(int, input().split()))
print(first_indexB(l,5,0))