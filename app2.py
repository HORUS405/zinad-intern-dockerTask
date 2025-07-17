from flask import Flask,jsonify
import  requests

app = Flask(__name__)


APP1_URL = "http://app1:5000/receive"


@app.route('/')
def index():
    return '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGQ4bXMycGthb29wODlpZXp6MzYxMnF4eGEwMjlidDA2d2piY2RzMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fvA1ieS8rEV8Y/giphy.gif">\n<h1>Welcome to app2!</h1>\n<a href="/ping">Ping app1</a>'

@app.route('/ping')
def ping():
    response = requests.get(APP1_URL)
    if response.status_code == 200:
        return jsonify({'message': 'app2: Ping', 'app1_response': response.json()})
    return jsonify({'message': 'app2: Hello from app2!'})

@app.route('/receive', methods=['GET'])
def receive():
    return jsonify({'message': 'app2: Pong'}), 200



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)