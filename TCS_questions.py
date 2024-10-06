# gradeTotal,totalFemale=0,0
# ans=[]
# s=input()
# l=s.split(" ")
# name, age, grade, gender=l[0],int(l[1]),l[2],l[3]
# if age>20:
#     ans.append(name)
# if gender=="Female":
#     gradeTotal+=ord(grade)
#     totalFemale+=1
# avg=gradeTotal/totalFemale if totalFemale!=0 else 0
# print(*ans)
# print(avg)
def findMajorityElement(n,arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    for key,val in freq.items():
        if val>=n//2:
            print(key,end="")

n=int(input())
arr=list(map(int,input().split()))
findMajorityElement(n,arr)