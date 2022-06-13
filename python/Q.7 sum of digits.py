'''Q.1 Sum of Digits of a Number
It is used to find the sum of digits of a number using recursion.'''

def sum_of_digits(n):
    if len(n)==1:
        return int(n)
    else:
        return int(n[len(n)-1]) + sum_of_digits(n[:len(n)-1])

n = input("N = ")
print(sum_of_digits(n))

def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return (n%10) + sum_of_digits(n//10)

n = int(input("N = "))
print(sum_of_digits(n))

