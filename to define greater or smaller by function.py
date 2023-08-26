def greater_smaller(a,b):
    if a == b:
        return a,b
    else:
        if a > b:
            return a
        else:
            return b
num1 = int(input("enter any number : "))
num2 = int(input("enter any number : "))
bigger = greater_smaller(num1,num2)
print(f"{bigger} is biggest")

# 2nd method
# def greater(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second nuber : "))
# bigger = greater(num1,num2)
# print(f"{bigger} is greater")