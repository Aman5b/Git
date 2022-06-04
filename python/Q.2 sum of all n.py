# Q.2) Write a recursive function that takes a number and returns the sum of all the numbers from zero to that number.

def sum_of_numbers(n):
    if n==0:
        return n  # doesn't return null value
    else:
        return n + sum_of_numbers(n-1)  # number + number-1 is the key (IMPPPPPP)

n = int(input())
print(sum_of_numbers(n))  # order is important