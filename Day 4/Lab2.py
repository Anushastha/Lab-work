#2)Write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.

a=int(input("Enter the first number= "))
b=int(input("Enter the second number= "))
c=int(input("Enter the third number= "))
if a==b or b==c or c==a or a==b==c:
    print("The sum is 0")
else:
    sum=a+b+c
    print("The sum of the given integers is",(sum) )




