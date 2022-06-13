'''
Write a recursive function that reverse_the_list_of_numbers that it receives.
'''
def reverse(strng):
    if len(strng)==0:
        return []
    else:
        return [strng[len(strng)-1]] + reverse(strng[:-1])

# strng = [1,2,3,4,5]
strng = list(input().split())
print(list(strng))
print("The reversed list is : ")
print(reverse(strng))