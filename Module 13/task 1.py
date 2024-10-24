from flask import Flask
app = Flask(__name__)
@app.route('/prime_number/<number>')
def is_prime(number):
    try:
        prime=True
        for i in range(2, int(number)):
            if int(number) % i == 0:
                prime=False
                break
        response={
            "Number":number, "isPrime":prime
        }
        return response
    except ValueError:
        response={"message": "Invalid number is added"}
        return response
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)