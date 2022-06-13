'''
Write a recusrive function to compuyte the product of two positive integres 
using addition and subtration only.
'''

def product(num1, num2, value):
    if num2==0:
        return value
    else:
        num2 -= 1
        value += num1 
        return product(num1, num2, value)

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
value = 0
print(product(num1, num2, value))