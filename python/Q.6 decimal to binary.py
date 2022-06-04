# decimal to binary using recursion

def decimal_to_binary(n):
    if n == 0:
        return n

    else:
        r = n % 2
        print(r, end="")
        decimal_to_binary(n//2)

n = int(input())
decimal_to_binary(n)