#5)A school decided to replace the desks in three classrooms. Each desk sits two students.Given the number of
#students in each class, print the smallest possible number of desks that can be purchased.The program should
#read three integers: the number of students in each of the three classes, a, b and c respectively.Suppose In
#the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group
#has 21 students, so they can get by with no fewer than 11 desks. 11 desks are also enough for the third group of
#22 students. So, we need 32 desks in total.

a=int(input("Enter the number of students in the first class= "))
A=a//2
print("You'll need at least",(A),"desks for the first class.")
b=int(input("Enter the number of students in the second class= "))
B=b//2
print("You'll need at least",(B),"desks for the second class.")
c=int(input("Enter the number of students in the third class= "))
C=c//2
print("You'll need at least",(C),"desks for the third class.")
remaining_chairsA=a%2
print("remaining chairs in class A",(remaining_chairsA))
remaining_chairsB=b%2
print("remaining chairs in class B",(remaining_chairsB))
remaining_chairsC=c%2
print("remaining chairs in class C",(remaining_chairsC))