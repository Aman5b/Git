'''
Python program to find the power of a number using recursion
Given a number N and power P. 
The task is to write a Python program to find the power of a number using recursion.
'''

def power(n,p):
    if p==0:
        return 1
    elif n==0:
        return 0
    else:
        return n * power(n,p-1)

n = int(input("N = "))
p = int(input("P = "))
print(power(n,p))