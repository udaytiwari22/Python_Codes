n = 7
k = n-1
for i in range(0, n):
    for z in range(0, k):
        print(end=" ")
    k = k-1
    for j in range(0, i+1):
        print('*', end="")
    print("\n")
