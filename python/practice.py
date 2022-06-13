# for _ in range(int(input())):
#     x,y,a = map(int, input().split())
#     if a>=x and a<y:
#         print("YES")
#     else:
#         print("NO")
    
# for _ in range(int(input())):
#     x,y = map(int, input().split())
#     if (x+y)%2 == 0:
#         print("YES")
#     else:
#         print("NO")

# for _ in range(int(input())):
#     x,y = map(int, input().split())
#     a = abs(x-y)
#     b = abs(x-y)
#     if x==0 or y == 0 or x%3==0 or y%3==0:
#         print(0)
#     elif a%3==0 and x!=0 and y!=0:
#         print(1)
#     else:
#         print(2)

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     x = 0
#     if n%2!=0:
#         print(-1)
#     else:
#         if sum(a) != 0:
#             if sum(a) < 0:
#                 print(abs(sum(a)//2))
#                 # print(x)
#             else:
#                 print(sum(a)//2)
#                 # x += sum(a)
#                 # print(x)
#         else:
#             print(0)

# for _ in range(int(input())):
#     x,y = map(int, input().split())
#     if x>=y:
#         print(x-y)
#     else:
#         print(0)

# for _ in range(int(input())):
#     n,x = map(int, input().split())
#     if n<=6:
#         print(x)
#     elif n//6==0:
#         print((n)*x)
#     elif n%6==0:
#         print((n//6)*x)
#     else:
#         print(((n//6)+1)*x)

# for _ in range(int(input())):
#     a,b = map(int, input().split())
#     if a==b:
#         print("YES")
#     elif a>b:
#         print("NO")
#     else:
#         if a%2==0 and b%2==0:
#             print("YES")
#         elif a%2==0 and b%2!=0:
#             if b == a+1:
#                 print("YES")
#             else:
#                 print("NO")
#         elif a%2!=0 and b%2==0:
#             print("YES")
#         else:
#             print("NO")

# for _ in range(int(input())):
#     a,b = map(int, input().split())
#     diff = b - a
#     if diff == 0:
#         print("YES")
#     else:
#         if diff == 2:
#             print("NO")
#         elif diff % 3 == 0:
#             print("YES")
#         elif diff % 3 == 1:
#             print("YES")
#         else:
#             print("NO")

# for _ in range(int(input())):
#     x,y = map(int, input().split())
#     a = y*(x-1)*2
#     b = x*(x-1)
#     print(a-b)


# for _ in range(int(input())):
#     n = int(input())
#     a = input()
#     b = input()
#     A = ''
#     B = ''
#     for i in range(n):
#         if a[i]!=b[i]:
#             A += a[i]
#             B += b[i]
#     print(len("".join(set(B))))


# def fun(x,y):
#     if x==0:
#         return y
#     else:
#         return fun(x-1, x*y)
    
# print(fun(4,2))

