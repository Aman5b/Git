# Q.1) Print 1-n without loop
 
def recurrion(n):
    if n==0:
        return 
    else:
        recurrion(n-1)
        print(n, end=" ")

n = int(input("N = "))
recurrion(n)