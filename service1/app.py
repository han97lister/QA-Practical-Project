from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    letters = requests.get("http://localhost:5001/letters")
    numbers = requests.get('http://service3:5002/numbers')

    ticket = str(numbers + letters)
    
    #service4
    prize = requests.post("http://localhost:5003/prize", data=ticket.text)
    

    return render_template('index', ticket=ticket.text, prize=prize.text)


if __name__=='__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')