num = int(input("Enter any number"))
if num >=90:
    grade = "A+"
elif num >= 75:
    grade = "A"
elif  num >= 65:
    grade = "B+"
elif num >=45:
    grade = "B"
elif num>=33:
    grade ="C"
else:
    grade = "Fail"
print(grade)