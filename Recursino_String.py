def replacechar(s,a,b):
    l=len(s)
    if(l==0):
        return s
    smalloutput= replacechar(s[1:],a,b)
    if(s[0]==a):
        return b + smalloutput
    else:
        s[0] + smalloutput

print("Enter the String")
s = input() 
print(replacechar(s,'c','x')) 
        