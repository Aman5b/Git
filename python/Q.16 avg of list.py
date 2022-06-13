'''
write a recursive function to obtain average of all numbers present in the given list
'''

def sum_list(lst, n):
    if len(lst)==1:
        return lst[0] / n
    else:
        # return lst[len(lst)-1] + sum_list(lst[:len(lst)-1])
        return (lst[len(lst)-1])/n + sum_list(lst[:len(lst)-1],n)

lst = list(map(int, input().split()))
n = len(lst)
print(sum_list(lst,n))
