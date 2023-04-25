list=[-3,5,7,-8,10,-12,0]
positive =0
neg =0
even=0
odd=0
for i in list:
    if i>0:
        positive+=i
    elif i<0:
        neg+=i
    elif i%2==0:
        even+=i
    else: odd+=i
print("Postive is ",positive)
print("Negative is ",neg)
print("Even number is ",even)
print("Odd is ",odd)