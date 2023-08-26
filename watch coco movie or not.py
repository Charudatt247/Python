name, age = input("Enter your name and age : ").split(",")
age = int(age)
print(f"your name is {name}\nyour age is {age}")
if age>=10 and (name[0]=='a' or name[0]=='A'):
    print("you can watch coco")
else:
    print("you cannot watch coco")

# user_name =input("Enter your name : ")
# user_age =int(input("Enter your age : "))
# if user_age>=10 and (user_name[0]=='a' or user_name[0]=='A'):
#     print("You can watch coco")
# else:
#     print("you cannot watch coco")