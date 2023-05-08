from flask import jsonify, request
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URL'] ='mongodb://localhost:27017/flask mongodb'
mongo = PyMongo(app)

roles ={

    "admin": ["select", "insert", "update", "delete", "login"],
    "user": ["select", "insert", "update"]
}
def has_permission(headers, required_permission):

    authorization_header = headers.get("Authorization")
    if not authorization_header:
        return false
    required_role =authorization_header.strip().lower()
    allowed_permission = roles[required_role]

    return required_permission in allowed_permission


@app.route("/select/<name>", methods=["GET"])
def select(name):
    if has_permission(request.headers, "select"):
        collection = mongo.db.flaskbmongod
        result = collection.find_one({"name": name})
        resp = jsonify(result)
        return resp

    return jsonify({"message": "unauthorized"}), 401


@app.route("/insert/", methods=["POST"])
def insert():
    if not has_permission(request.headers, "insert"):
        return jsonify({"message": "unauthorized"}), 401

    collection = mongo.db.flaskmongodb
    firstname = request.json["name"]
    password = request.json["password"]
    result = collection.insert_one({"name": firstname, "password": password})
    output = {"name": request.json["name"], "password": request.json["password"], "message": "success"}


@app.route("/update/<name>", methods=["PUT"])
def update(name):
    if not has_permission(request.headers, "update"):
        return jsonify({"message": "unauthorized"}), 401

    collection = mongo.db.flaskbmongod
    firstname = request.json["name"]
    password = request.jsano["password"]
    output ={"name": request.json["name"], "password": request.json["password"], "message": "success"}
    return jsonify({"result": output})

@app.route("/login/<password>", methods=["GET"])

def login(password):
    if not has_permission(request.headers, "login"):
        return jsonify({"message": "unauthorized"}), 401

    collection = mongo.db.flaskbmongod
    firstname = request.json["name"]
    password = request.jsano["password"]
    output ={"name": request.json["name"], "password":request.json["password"], "message": "success"}
    return jsonify({"result": output})
    if result:
        if result["password"] == password:
            output = {"message": "login successfuly"}
            return jsonify(output)
        else:
            output = {"message": "enter a valid password"}
            return jsonify(output)
    else:
        output ={"message": "user is not found"}
        return jsonify(output)

@app.route("/delete/<name>", methods=["DELETE"])

def delete(name):
    if not has_permission(request.headers, "delete"):
        return jsonify({"message": "unauthorized"}), 401

    collection = mongo.db.flaskbmongod
    result = collection.delete_one({"name": name})


    output = {"message": "DELETED"}
    return jsonify({"result": output})

if __name__ == "__main__" :
    app.debug = True
    app.run()


