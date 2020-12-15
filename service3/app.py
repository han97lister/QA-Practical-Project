from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/number', methods=['GET'])
def get_number():

    #num = ["13579", "24680", "48582", "09672", "34167"]
    num = ["1", "2", "3", "4"]
    number = random.choices(num)

    return Response(number, mimetype="text/plain")

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)

