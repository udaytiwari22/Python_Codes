def last_index_better(a,x,si):
    l=len(a)
    if(si==l):
        return -1
    smallerlistoutput=last_index_better(a,x,si+1)
    if(smallerlistoutput != -1):
        return smallerlistoutput
    else:
        if(a[si]==x):
            return si
        else:
            return -1
l=list(map(int,input().split()))
print(last_index_better(l,5,0))     
    
    