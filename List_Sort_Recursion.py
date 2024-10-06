def issorted(a):
    l=len(a)
    if(l==0 or l==1):
        return True
    if a[0]>a[1]:
        return False
    smallerlist=a[1:]
    is_smaller_list_sorted= issorted(smallerlist)
    if(is_smaller_list_sorted):
        return True
    else:
        return False
    
l=[]
n=int(input())
# for i in range (0,n):
#     ele=int(input())
#     l.append(ele)
# print(issorted(l)) 
li=list(map(int,input().split()))
print(li)
print(issorted(li))