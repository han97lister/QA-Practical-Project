from flask import Flask, render_template, request
import requests
from application import app, db
from application.models import Prize

@app.route('/', methods=['GET'])
def index():

    letters = requests.get("http://localhost:5001/letters")
    numbers = requests.get('http://localhost:5002/number')
    ticket = letters.text+str(numbers.text)
    
    prize = requests.post('http://localhost:5003/prize', data=ticket)

    return render_template('index.html', ticket=ticket, prize=prize.text)