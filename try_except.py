try:
    n=input('Enter the Numerator :')
    num=int(n)
    n=input('Enter the Denominator :')
    den=int(n)
    value=num/den
    print(value)
except ValueError:
    print("Numerator and Demoninator should be an Integer")    