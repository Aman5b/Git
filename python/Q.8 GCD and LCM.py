# LCM of 2 numbers using recursive

def GCD(x,y):
    if x==0:
        return y
    return GCD(y%x , x)

def LCM(x,y):
    return (x/GCD(x,y)*y)

x, y = map(int, input().split())
print("GCD :", GCD(x,y))
print("LCM :", LCM(x,y))
