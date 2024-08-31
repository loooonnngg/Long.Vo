#tas 1
list_of_seasons = ("winter","spring","summer","fall")
season_number = int(input("enter number of a month: "))
if season_number in (12, 1, 2):
    season = list_of_seasons[0]
elif season_number in (3, 4, 5):
    season = list_of_seasons[1]
elif season_number in (6, 7, 8):
    season = list_of_seasons[2]
elif season_number in (9, 10, 11):
    season = list_of_seasons[3]
else:
    season = "Invalid month number"
print(f"The month number {season_number} is {season}")

#task 2
list_of_names= set()
while True:
    name = input("Enter a name: ")
    if name == "":
        break
    elif name in list_of_names:
        print("Existing name")
    else:
        print("new name")
        list_of_names.add(name)
for name in list_of_names:
    print(name)

#task 3
airport_list={}
command = input("type 'add' to add a new airport, 'view' to find an airport or 'quit' to quit the program: ")
while command != 'quit':
    if command == 'add':
        airport_name = input("enter airport name: ")
        airport_ICAO = input("enter airport ICAO code: ").upper()
        airport_list[airport_ICAO] = airport_name
    elif command == 'view':
        airport_view = input("enter airport ICAO code: ").upper()
        if airport_view in airport_list:
            print(f"The airport with {airport_view} code is airport {airport_list[airport_view]}")
        else:
            print("airport not found")
    else:
        print("invalid command")
    command = input("type 'add' to add a new airport, 'view' to find an airport or 'quit' to quit the program: ")