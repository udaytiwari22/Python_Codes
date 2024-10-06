def firstindex(a,x):
    l=len(a)
    if l==0:
        return -1
    if (a[0]==x):
        return 0
    smallerlist=a[1:]
    smallerlistoutput=firstindex(smallerlist,x)

    if(smallerlistoutput==-1):
        return -1
    else:
        return smallerlistoutput + 1

l=[]
print('Enter the number of inputs')
n=int(input())
l= list(map(int,input().split()))
z=firstindex(l,4)
print(z)

