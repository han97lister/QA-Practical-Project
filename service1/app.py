from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    #service2
    letters = requests.get("http://localhost:5001/letters")

    #service3
    numbers = requests.get('http://service3:5002/numbers')

        #special_num = requests.get('http://service3:/special')

    #service4
    prize =
    

    return render_template('index', letters=letters.text)


if __name__='__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')