def printnum(n):
    num=1
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(end=" ")
        n=n-i 
        for j in range(1,i+1):
            print(num,end=' ')
            num=num+1
            if(num>=10):
                num=1
                        
        print('\n')  
                  
n=5
print(printnum(n))            