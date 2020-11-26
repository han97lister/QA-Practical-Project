from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    #service2
    uppercase_request = requests.get('http://service2:5001/upper')
    uppercase = upletters_request.json()['uppercase']

    lowercase_request = requests.get('http://service2:5001/lower', json={"uppercase": uppercase})
    lowercase = lowercase_request.json()['lowercase']

    #service3
    six_digit_request = requests.get('http://service3:5002/six')
    six_digit = six_digit_request.json()['six_digit']

    special_num = requests.get('http://service3:/special')

    #service4
    prize1 =
    prize2 =
    prize3 =

    return render_template('index', uppercase=uppercase, lowercase=lowercase, six_digit=six_digit, special_num=special_num)



if __name__='__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')