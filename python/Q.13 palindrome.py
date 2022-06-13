'''
A string is entered through the keyboard, Write a recursive 
function that check whether the string is a palindrome or not.
'''

def palindrome(strng):
    if len(strng) == 1:
        return True
    else:
        if strng[0] == strng[-1]:
            return palindrome(strng[1:-1])
        else:
            return False
strng = input("Enter a string : ")
print(palindrome(strng))
