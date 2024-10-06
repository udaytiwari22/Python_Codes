# take input as integer convert it in the binary form then alter all bits of the binary number and return number formed as integer
# y=int(input())
# binary=bin(y)[2:]
# st=""
# for i in binary:
#     if i=='0':
#         st+='1'
#     if i=='1':
#         st+='0'
# print(int(st,2))

#Check if the sum of digits is palindrome or not if yes return 1 else return 0

# def SumofdigitIsPalindrome(num):
#     sum=0
#     temp=num
#     rev=0
#     remainder=0
#     while temp>0:
#         remainder=temp%10
#         sum+=remainder
#         temp//=10
#     temp=sum
#     while temp>0:
#         remainder=temp%10
#         rev=rev*10 +remainder
#         temp=temp//10
#     if(rev==sum):
#         return 1
#     else:
#         return 0

# #Driver Code
# n=int(input()) 
# z=SumofdigitIsPalindrome(n)
# print(z)

#Find the longest String from the given statement
# def LongestString(s):
#     count=0
#     ans=0
#     y=s.split(" ")
#     for word in y:
#         if len(word)>count:
#             count=len(word)
#             ans=word
#     return ans  
    
    
# y=input()
# print(LongestString(y))

