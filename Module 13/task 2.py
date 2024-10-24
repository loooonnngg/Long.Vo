from flask import Flask
import mysql.connector
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'sql_password',
    database = 'flight_game',
    collation = 'utf8mb4_general_ci',
    autocommit = True
    )
app = Flask(__name__)
@app.route('/airport/<ICAO>')
def find_airport(ICAO):
    try:
        cursor = connection.cursor()
        cursor.execute(f"select name, municipality from airport where ident = '{ICAO}'")
        answer = cursor.fetchall()
        response={
            "ICAO":ICAO,"Name":answer[0][1],"Location":answer[0][0]
        }
        return response
    except IndexError:
        response={
            "message":"Invalid ICAO code"
        }
        return response
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)