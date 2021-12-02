#7)Sum of first 10 odd numbers
num=20
sum=0;
for i in range(1,num+1):
    if(not(i%2)==0):
        sum +=i;
print("\nSum of odd numbers from 1 to",num,"is:",sum)
