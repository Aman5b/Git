
'''
Prime factors of the number
'''

def prime_factors(num,i):
    if num>=i:
        if num % i == 0:
            print(i, end=",")
            num = num // i
        else:
            i+=1
        prime_factors(num,i)

num = int(input("N = "))
i = 2
prime_factors(num,i)