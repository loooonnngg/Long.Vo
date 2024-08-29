import random
number = 1
while number <= 1000:
    if number%3 == 0:
        print(number)
    number +=1
#task 2
inches = float(input("Enter the inches: "))
if inches >= 0:
    centimeter = inches * 2.54
    print(centimeter)
#task 3
number = int(input("Enter the number, press enter to see the min and max number: "))
min_num = max_num = number
while number != "":
    number = int(number)
    if number < min_num:
        min_num = number
    if number > max_num:
        max_num = number
    number = input("Enter the number, press enter to see the min and max number: ")
print(min_num)
print(max_num)
#task 4
correct_number = random.randint(1, 10)
num_guess = int(input("Guess a number between 1 and 10: "))
while num_guess != correct_number:
    if num_guess < correct_number:
        print("too low")
    if num_guess > correct_number:
        print("too high")
    num_guess = int(input("Guess a number between 1 and 10: "))
print("correct")
#task 5
username_correct = "python"
password_correct = "rules"
username = input("Enter your username: ")
password = input("Enter your password: ")
attempt = 0
while attempt < 5:
    if username == username_correct and password == password_correct:
        print("welcome")
        break
    attempt += 1
    print("please try again")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if attempt == 5:
        print("access denied")
#task 6
total_points = int(input("Enter the amount of total points: "))
points = 0
points_in_circle = 0
while points < total_points:
    x_position = random.uniform(-1,1)
    y_position = random.uniform(-1,1)
    if x_position ** 2 + y_position ** 2 < 1:
        points_in_circle = points_in_circle + 1
    points += 1
pi = (4*points_in_circle)/total_points
print(f"pi approximation is {pi}")