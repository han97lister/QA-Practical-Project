from flask import Flask, request, Response
import random
    
app = Flask(__name__)

@app.route('/letters', methods=['GET'])
def letters():

    uppercase = ["ABC", "DEF", "GHI", "JKL", "MNO"]
    return  Response(random.choice(uppercase), mimetype="text/plain")
        
    #change implement
    #lowercase = ["xyz"]

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)    