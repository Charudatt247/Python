subject_1 = float (input ("Enter marks for Subject_1 : "))
subject_2 = float (input ("Enter marks for Subject_2 : "))
subject_3 = float (input ("Enter marks for Subject_3 : "))
subject_4 = float (input ("Enter marks for Subject_4 : "))
subject_5 = float (input ("Enter marks for Subject_5 : "))

total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5

percentage = (total / 500.0) * 100

if percentage >= 90:
    grade = 'A'
elif percentage >= 80 and percentage < 90:
    grade = 'B'
elif percentage >= 70 and percentage < 80:
    grade = 'C'
elif percentage >= 60 and percentage < 70:
    grade = 'D'
elif percentage >= 40 and percentage < 60:
    grade = 'E'
else:
    grade = 'F'

print ("\nThe Total marks is:   ", total, "/ 500.00")
print ("\nThe Percentage is:    ", percentage, "%")
print ("\nThe Grade is:         ", grade)