#2)WAP which accepts marks of four subjects and display total marks, percentage and grade.
# Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less
# than 40% –> fail.
a=int(input("Enter the marks of nepali= "))
b=int(input("Enter the marks of mathematics= "))
c=int(input("Enter the marks of accountancy= "))
d=int(input("Enter the marks of economics= "))
total_marks_obtained= a+b+c+d
percentage= ((total_marks_obtained/400)*100)
print("Total percentage obtained=",percentage)
if percentage>70:
   print("Grade=Distinction")
elif percentage>60:
    print("Grade=First")
elif percentage>40:
    print("Grade=Pass")
else:
    print("Grade=Fail")


