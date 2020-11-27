from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/prize', methods=['GET', 'POST'])
def prize():

    letters = request.data.decode('utf-8')
    numbers = request.data.decode('utf-8')
    ticket = numbers+letters
    
    count = 0

    for num in ticket:
        if num == '7' :
            count = count + 1

        if count == 1 :
            prize == "£200"
        else :
            prize == "Nothing, please try again"

    return Response(prize, mimetype="text/plain")

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)         

print("hello")  