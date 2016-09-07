import json

from flask import Flask, request, jsonify

app = Flask(__name__)
users = []


@app.route('/user', methods=['GET'])
def list_users():
    return jsonify(users)


@app.route('/user', methods=['POST'])
def create_user():
    user = json.loads(request.data.decode("utf-8"))
    users.append(user)
    return jsonify(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
