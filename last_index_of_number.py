def lastindex(a, x):
    l = len(a)
    if (l == 0):
        return -1
    smallerlist = a[1:]
    smallerlistoutput = lastindex(smallerlist, x)
    if (smallerlistoutput != -1):
        return smallerlistoutput + 1
    else:
        if (a[0] == x):
            return 0
        else:
            return -1


l = list(map(int, input().split()))
print(lastindex(l, 5))
