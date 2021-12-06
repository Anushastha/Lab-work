#A student will not be allowed to sit in exam if his/her attendence is less than 75%
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.
a=int(input("Number of classes held? "))
b=int(input("Number of classes attended? "))
percentage_of_class_attended=((b/a)*100)
if (percentage_of_class_attended < 75):
    print("You are not allowed to sit in exams.")
else:
    print("You can sit in the exams.")
