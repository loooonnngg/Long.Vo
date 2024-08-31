import random
#task 1
def dice_roll():
    rolling = random.randint(1, 6)
    return rolling
rolls_result = dice_roll()
while rolls_result != 6:
    print(rolls_result)
    rolls_result = dice_roll()
print(rolls_result)

#task 2
def dice_roll_custom(num_sides):
    rolling = random.randint(1, num_sides)
    return rolling
num_of_sides = int(input("Enter number of sides: "))
rolls_result = dice_roll_custom(num_of_sides)
while rolls_result != num_of_sides:
    print(rolls_result)
    rolls_result = dice_roll_custom(num_of_sides)
print(rolls_result)

#task 3
def gallons_to_liters(gallons):
    liters = gallons*3.785
    return liters
input_gallons = int(input("Enter number of gallons: "))
print("the amount of liters is", gallons_to_liters(input_gallons))

#task 4
def sum_of_numbers(list_of_numbers):
    number_sum=0
    for number in list_of_numbers:
        number_sum+=number
    return number_sum
number_list = []
while True:
    number=input("Enter a number: ")
    if number == "":
        break
    else:
        number_list.append(int(number))
print(sum_of_numbers(number_list))

#task 5
def remove_odd(number_list):
    odd_removed_list = []
    for number in number_list:
        if number % 2 == 0:
            odd_removed_list.append(number)
        else:
            continue
    return odd_removed_list
number_list_first = []
while True:
    number=input("Enter a number: ")
    if number == "":
        break
    else:
        number_list_first.append(int(number))
print(remove_odd(number_list_first))
print(number_list_first)

#task 6
def price_per_pizza(price, diameter):
    price_per_square_meter = price/diameter**2
    return price_per_square_meter
first_price = int(input("Enter first pizza price: "))
first_diameter = int(input("Enter first pizza diameter: "))
second_price = int(input("Enter second pizza price: "))
second_diameter = int(input("Enter second pizza diameter: "))
first_value_for_money = price_per_pizza(first_price, first_diameter)
second_value_for_money = price_per_pizza(second_price, second_diameter)
if first_value_for_money > second_value_for_money:
    print("first pizza provide more value")
else:
    print("second pizza provide more value")