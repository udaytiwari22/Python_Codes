def binarysearch(a,x,si,ei):
    if(si>ei):
        return -1
    mid = (si+ei)//2
    if(a[mid]==x):
        return mid
    elif(a[mid]>x):
         return binarysearch(a,x,si,(mid -1))
    else:
        return binarysearch(a,x,(mid+1),ei)
    
a=[2,3,4,6,7,8,10,13,15,16,18,19,20,21]
x=10
print(binarysearch(a,x,0,len(a)-1)) 