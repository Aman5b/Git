# Write a recursive function that takes a number as an input and returns the factorial of that number.

def fact(n):
    if n==1 or n==0:
        return n
    else:
        return n*fact(n-1)
    
n = int(input("N = "))
print(fact(n))