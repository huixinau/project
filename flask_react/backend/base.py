from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def test():
    return "Server is working!"

@app.route('/profile', methods=['GET'])
def profile():
    return jsonify({
        "name": "John Doe",
        "about": "Software developer"
    })

if __name__ == '__main__':
    app.run(debug=True,host='http://127.0.0.1/', port=5001)
