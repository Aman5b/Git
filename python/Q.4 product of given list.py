# Write a recursive function that takes a list of numbers as an input and returns the product of all the numbers in the list.

def list_product(n):
    len_list = len(n)
    if len_list == 1:  #here the length is 1
        return n[0]    # whereas len(1) == index(0)
    else:
        return n[len_list-1] * list_product(n[:len_list-1])   # using recurssive function using slicing method
# last element * reverse list elements(recursive)

n = list(map(int, input().split( )))
print(list(n))
print(list_product(n))