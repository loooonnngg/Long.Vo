import random

a = int(input("a is "))
b = int(input("b is "))
print(a,b)
c=a
a=b
b=c
print(a,b)

name = input("Enter your name: ")
print("Hello "+name+"!")

r = float(input("Enter circle radius: "))
area = 3.14 * (r ** 2)
print("area of circle is:", area)

l = float(input("Enter length: "))
w = float(input("Enter width: "))
perimeter = 2*(l+w)
rectangle_area = (l*w)
print("rectangle perimeter is:", perimeter)
print("rectangle area is:", rectangle_area)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
sums = num1+num2+num3
product = num1*num2*num3
average = sums/3
print("sum of 3 number is:", sums)
print("product of 3 number is:", product)
print("average of 3 number is:", average)

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: ")) + (talents * 20)
lots= float(input("Enter lots: ")) + (pounds * 32)
grams = (lots * 13.3)
kilograms = int(grams/1000)
gram_leftover = grams%1000
print(f"The weight in modern units: {kilograms} and {gram_leftover:.2f} grams")

code1_num1= str(random.randint(0,9))
code1_num2= str(random.randint(0,9))
code1_num3= str(random.randint(0,9))
code1= code1_num1+code1_num2+code1_num3
print(code1)

code2_num1= str(random.randint(1,6))
code2_num2= str(random.randint(1,6))
code2_num3= str(random.randint(1,6))
code2_num4= str(random.randint(1,6))
code2=code2_num1+code2_num2+code2_num3+code2_num4
print(code2)