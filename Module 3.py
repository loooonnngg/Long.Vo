#task 1
zander = int(input("what is the length of the zander in centimeter: "))
if zander <= 42:
    print(f"release the fish back into the lake, the zander was {42 - zander} centimeters below the size limit")
else:
    print("you caught a fish")
#task 2
cabin_class = str(input("what is your cabin class?: "))
if cabin_class == "LUX":
    print("Your cabin is LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("your cabin is A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("your cabin is B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("your cabin is C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class")
#task 3
gender = str(input("Are you male or female?: "))
hemoglobin = int(input("enter your hemoglobin value: "))
if gender == "male":
    if hemoglobin < 117:
        print("you have low hemoglobin")
    elif 117 <= hemoglobin < 155:
        print("you have normal hemoglobin")
    else:
        print("you have high hemoglobin")
elif gender == "female":
    if hemoglobin < 134:
        print("you have low hemoglobin")
    elif 134 <= hemoglobin < 167:
        print("you have normal hemoglobin")
    else:
        print("you have high hemoglobin")
else:
    print("wrong input")
#task 4
year = int(input("enter a year: "))
if (year%100 == 0 and year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print("your year is a leap year")
else:
    print("your year is not leap year")