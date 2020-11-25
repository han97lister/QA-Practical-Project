from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    upletters_request = requests.get('http://service2:5001/upper')
    


    return render_template('index')



if __name__='__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')