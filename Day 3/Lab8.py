#8)Given a n-digit number. Find the sum of its digits.

n=int(input("Enter a number= "))
total=0
while(n>0):
    digit=n%10
    total=total+digit
    n=n//10
print("the total sum of digits is:",(total))
