# # Example - 1
#
# a = 0
# for i in range (1,11):
#     a += i
# print(a)
#
#
# #  Example - 2
#
# n = int(input("Enter any number : "))
# a = 0
# for i in range (1,n+1):
#     a += i
# print(a)
#
#
# #  Example - 3
#
# n = input("Enter the no. more than 1 digit : ")
# a = 0
# for i in range (0,len(n)):
#     # a = a+int(n[i])
#       a += int(n[i])
# print(a)
#
#
# #  Example - 4
#
# n = input("Enter a name : ")
# b = len(n)
# # print(b)
# a = ""
# for i in range (0,b):
#     if n[i] not in a:
#         print(f"{n[i]} : {n.count(n[i])}")
#         a += n[i]
#

 # Example - 5
for i in range (1,11):
    print(i)
    if i==5:
        break