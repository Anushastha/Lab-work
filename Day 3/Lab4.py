#4)Given three integers, print the smallest one. (Three integers should be user input)
a=int(input("Enter the first number= "))
b=int(input("Enter the second number= "))
c=int(input("Enter the third number= "))
if a<=b and a<=c:
    print((a),"is the smallest.")
elif b<=a and b<=c:
    print((b),"is the smallest.")
else:
    print((c),"is the smallest.")
