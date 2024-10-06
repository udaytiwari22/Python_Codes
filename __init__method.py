class Fraction:
    
    def __init__(self,num=0,den=1):
        if den==0:
          raise ValueError("Denominator cannot be zero")
        self.num = num
        self.den=den
    def print(self):
        if(self.num==0):
            print(0)
        elif(self.den==1):
            print(self.num)
        else:
            print(self.num,'/',self.den)
    def simplify(self):
        if(self.num==0 and self.den==1):
            return
        current= min(self.num,self.den)
        while(current>1):
            if(self.num%current== 0 and self.den % current ==0):
                break
            current-=1
        self.num=self.num//current
        self.den=self.den//current
    def addfraction(self,anotherfraction):
        newNum=self.num*anotherfraction.den + anotherfraction.num*self.den
        newDen=anotherfraction.den*self.den
        self.num=newNum
        self.den=newDen
        self.simplify()
    def multiply(self,anotherfraction):
        self.num=self.num*anotherfraction.num
        self.den*=anotherfraction.den
        self.simplify()
    
    
f= Fraction(20,30)
f1=Fraction(3,2)
# print(f.__dict__)
# f.simplify()
# f.print()      
# f.addfraction(f1)
# f.print()
f.multiply(f1)
f.print()