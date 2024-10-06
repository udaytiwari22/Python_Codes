import sys
sys.setrecursionlimit(2000)


def fact(n):
    if(n==0):
        return 1
    n= n * fact(n-1)
    return n
n=int(input())
print(fact(n))
