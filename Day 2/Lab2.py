#2)find BMI of a person where take mass and height as input from the user
#BMI=mass in kg / (height in m)2
mass=int(input("enter the mass:"))
height=int(input("enter the height:"))
BMI=mass/(height*height)
print("the BMI of the person is {} kg\m\u00b2.".format(BMI))

