from flask import Flask, render_template, request
import requests
from application import app, db
from application.models import Prize

@app.route('/', methods=['GET', 'POST'])
def index():

    letters = requests.get("http://service2:5001/letters")
    numbers = requests.get('http://service3:5002/number')
    ticket = letters.text+str(numbers.text)
    
    prize = requests.post('http://service4:5003/prize', data=ticket)

    return render_template('index.html', letters=letters.text, numbers=numbers.text, ticket=ticket, prize=prize.text)