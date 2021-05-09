# total = 0
# n = int(input("Please enter line input : "))
# if n > 0 and n < 1000:
#     for i in range(0,n):
#         a = input()
#         if a.count('1') >= 2:
#             total = total + 1
#     print(total)
n = int(input())
total = 0
while(n>0):
    n = n - 1
    k = input()
    if k.count('1') >= 2:
        total= total + 1
print (total)