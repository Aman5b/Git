# Write a recursive function that takes a string and reverse the string.

def rev_string(str):
    if len(str) == 1:
        return str
    else:
        return str[len(str)-1] + rev_string(str[:len(str)-1])
    
str = input()
print(rev_string(str))





# def reverse_function(strg):
#     if len(strg)==1:
#         return strg
#     else:
#         return strg[len(strg)-1] + reverse_function(strg[:len(strg)-1])

# strg = input()
# print(reverse_function(strg))
