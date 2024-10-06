def CheckDivisibility(number):
    if 100<=number<=999:
        if number%9==0:
            print(f"Number {number} is divisible by 9")
        else:
            print(f"Number {number} is not divisible by 9")


n=int(input())
CheckDivisibility(n)