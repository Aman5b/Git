'''
A list contains some negative and some positive numbers. 
Write a recursive function that sanitizes the list by replacing all the negative numbers 
with 0.
'''

def replace_neg_num(n):
    length = len(n)
    if length == 1:
        if n[0] < 0:
            return [0]
        return n

    else:
        if n[0] < 0:
            n[0] = 0
            return [n[0]] + replace_neg_num(n[1:])
        return [n[0]] + replace_neg_num(n[1:])

n = list(map(int, input().split()))
print(replace_neg_num(n))