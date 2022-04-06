''' 
 ICSE 2017 Class 10
 Question 1a
 Name: Santoshi Gayatri
 Roll number: CS21BTECH11036
'''

'''
Question: If b is the mean proportion between a and c, show that:
(a^4 + b^2a^2 + b^4)/(b^4 + b^2c^2 + c^4) = a^2/c^2

'''

a = int(input())
c = int(input())

# x = a ** 4 +(b ** 2)*(a ** 2) + b ** 4
# y = b ** 4 +(b ** 2)*(c ** 2) + c ** 4

# Given that b is mean proportion of a and c so b^2=a*c
# we can replace b^2 with a * c

x = a ** 4 +(a * c)*(a ** 2) + (a * c) ** 2
y = (a * c) ** 2 +(a * c)*(c ** 2) + c ** 4

p = a ** 2
q = c ** 2

ratio1 = x/y
ratio2 = p/q
if ratio1 == ratio2 : print("True")
else : print("False")

# Since the output is always true, its proved that the given terms are in ratio
