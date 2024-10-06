# Quik Sort algorithm

# def quick_sort(array):
#     if len(array) <= 1:
#         return array

#     pivot = array[len(array) // 2]
#     less = [x for x in array if x < pivot]
#     greater = [x for x in array if x > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# a = list(map(int,input().split()))
# print(quick_sort(a))

# def merge(a1, a2, a):
#     i=0
#     j=0
#     k=0
#     while (i < len(a1) and j < len(a2)):
#         if a1[i] < a2[j]:
#             a[k] = a1[i]
#             i += 1
#             k += 1
#         else:
#             a[k] = a2[j]
#             j += 1
#             k += 1
#     while i < len(a1):
#         a[k] = a1[i]
#         k += 1
#         i += 1
#     while j < len(a2):
#         a[k] = a2[j]
#         k += 1
#         j += 1


# def merge_sort(a):
#     if len(a) == 0 or len(a) == 1:
#         return
#     mid = len(a)//2
#     a1 = a[0:mid]
#     a2 = a[mid:]
#     merge_sort(a1)
#     merge_sort(a2)
#     merge(a1, a2, a)


# a = list(map(int, input().split()))
# merge_sort(a)
# print(a)

# __init__method of class

# class Student:
#     def __init__(self, name, rollNumber):
#         self.name = name
#         self.rollnumber = rollNumber


# s1 = Student("sa", 23)
# s2 = Student("la", 24)
# print(s1.__dict__)
# print(s2.__dict__)


# class Fraction:
#     def __init__(self, num=0, den=1):
#         if den == 0:
#             den = 1
#         self.num = num
#         self.den = den

#     def print(self):
#         if self.num == 0:
#             print(0)
#         elif self.den == 1:
#             print(self.num)
#         else:
#             print(self.num, '/', self.den)

#     def simplify(self):
#         if (self.num == 0):
#             self.den=1
#             return
#         current = min(self.num, self.den)
#         while current > 1:
#             if (self.num % current == 0 and self.den % current == 0):
#                 break
#             current -= 1
#         self.num = self.num//current
#         self.den = self.den//current


# s1 = Fraction(0, 30)
# s1.simplify()
# s1.print()

class New:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
a=New('law',23)    
a._New__name='hat'
a._New__age=32     # Using the Name Mangling 
print(a._New__age)
print(a.__dict__)