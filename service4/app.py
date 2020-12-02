from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/prize', methods=['GET', 'POST'])
def prize():

    ticket = request.data.decode('utf-8')

    if ticket[0] == 'G':
        prize = "Congratulations, you have won 200 pounds"
    elif ticket[-2] == '8':
        prize = "Congratulations, you have won 100 pounds"
    else:
        prize = "Nothing, please try again"
    
    
    return Response(prize, mimetype="text/plain")
    

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)         

  