import random
#task 1
number_of_dices = int(input("how many dices do you want to role?: "))
sum_of_dice = 0
for rolls in range(number_of_dices):
    dice_number = random.randint(1, 6)
    print(dice_number)
    sum_of_dice += dice_number
print("the sum of the total of dices are: ", sum_of_dice)

#task 2
number_list = []
while True:
    number_input = input("Enter a number: ")
    if number_input == "":
        break
    else:
        number_list.append(int(number_input))
number_list.sort(reverse=True)
print("the five highest number u entered are: ",number_list[:5])

#task 3
user_input = int(input("Enter a number: "))
not_prime = 0
for i in range(2,user_input):
    if user_input%i == 0:
        not_prime = user_input
        break
if user_input == not_prime:
    print("The number is not prime")
else:
    print("The number is prime")

#task 4
cities_list = []
for i in range(1,6):
    city_input = input("Enter a city: ")
    cities_list.append(city_input)
for city_input in cities_list:
    print(city_input)