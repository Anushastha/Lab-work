#4)N students take K apples and distribute them among each other evenly. The remaining
#(the individual) part remains in the basket. How many apples will each single student
#get? How many apples will remain in the basket? The program reads the numbers N and K.
#It should print the two answers for the questions above.

N=int(input("Enter the number of students= "))
K=int(input("Enter the number of apples taken by them= "))
a=N//K
print("They distributed",(a),"apples equally among them")
b=N%K
print("There were",(b),"apples remaining in the basket")


