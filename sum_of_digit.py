num =int(input("Enter any number "))
sum =0
while num > 0:
    digit = num %10
    sum +=digit
    num//=10
print("Sum of digits ",sum)