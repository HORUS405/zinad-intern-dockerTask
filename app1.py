from flask import Flask, jsonify
import  requests

app = Flask(__name__)


APP2_URL = "http://app2:5001/receive"

@app.route('/')
def index():
    return '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGQ4bXMycGthb29wODlpZXp6MzYxMnF4eGEwMjlidDA2d2piY2RzMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fvA1ieS8rEV8Y/giphy.gif">\n<h1>Welcome to app1!</h1>\n<a href="/ping">Ping app2</a>'

@app.route('/ping')
def ping():
    response = requests.get(APP2_URL)
    if response.status_code == 200:
        return jsonify({'message': 'app1: Ping', 'app2_response': response.json()})
    return jsonify({'message': 'app1: Hello from app1!'})

@app.route('/receive', methods=['GET'])
def receive():
    return jsonify({'message': 'app1: Pong'}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)