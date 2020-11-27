from flask import Flask, Response, request
import random

app = Flask(__name__)

@app.route('/prize', methods=['GET', 'POST'])
def prizes():

    ticket = request.data.decode('utf-8')
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
     
