def issorted_better(a,si):
    l=len(a)
    if(si==(l-1) or si==l):
        return True
    if(a[si]>a[si+1]):
        return False
    issmallerpartsorted=issorted_better(a,si+1)
    return issmallerpartsorted
l=[]
n=int(input())
li=list(map(int,input().split()))
print(li)
print(issorted_better(li,0))
       