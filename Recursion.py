def fibonacci(n):
    if n==1 or n==2:
        return 1
    x=fibonacci(n-1)
    y=fibonacci(n-2)
    output=x+y
    return output
n=int(input())
z=fibonacci(n)
print(z)

