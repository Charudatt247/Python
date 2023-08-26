n=int(input("Enter any number : "))
b = 0
for i in range (2,n-1):
    if (n%i==0):
        b=1
        break
if (b==0):
    print("number is prime number")
else:
    print("number is not prime number")