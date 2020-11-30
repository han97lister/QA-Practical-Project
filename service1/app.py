from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    letters = requests.get("http://localhost:5001/letters")
    numbers = requests.get('http://localhost:5002/number')
    ticket = letters.text+str(numbers.text)
    
    prize = requests.post('http://localhost:5003/prize', data=ticket)

    return render_template('index.html', ticket=ticket, prize=prize.text)

if __name__=='__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')