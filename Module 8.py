import mysql.connector
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'long30112006',
    database = 'flight_game',
    collation = 'utf8mb4_general_ci',
    autocommit = True
    )
#Task 1
ICAOCode = input("Input your ICAO code: ")


cursor = connection.cursor()
cursor.execute(f"select name, iso_country from airport where ident = '{ICAOCode}'")
answer = cursor.fetchall()
print(f"The air port with ICAO code: {ICAOCode} is {answer[0][0]} located in {answer[0][1]}")

#Task 2
area_code=input("Input your area code: ")

cursor = connection.cursor()
cursor.execute(f"select name, type from airport where iso_country = '{area_code}' order by type")
answer_2 = cursor.fetchall()
print(f"list of air port in {area_code} are")
for row in answer_2:
    print(f"{row[0]}, type {row[1]}")

#task 3
def get_airport_location():
    ICAOCode = input("Input your ICAO code: ")
    cursor = connection.cursor()
    sql = f"select latitude_deg, longitude_deg from airport where ident ='{ICAOCode}'"
    cursor.execute(sql)
    output = cursor.fetchall()
    airport_coordinates = output[0][0], output[0][1]
    return airport_coordinates
from geopy import distance
first_airport = get_airport_location()
second_airport = get_airport_location()
print(f"distance between two airports is {distance.distance(first_airport, second_airport).kilometers} kilometer")