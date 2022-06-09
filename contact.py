from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'Name': 'Raju',
        'Contact': '9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': 'Rahul',
        'Contact': '9876543222', 
        'done': False
    }
]


@app.route("/")
def hello():
    return "hello"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
 
    contact = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['Name'],
        'description': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(contact)
    return jsonify({
        "status":"success",
        "message": "contact added succesfully!"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    })
 
 

if (__name__ == "__main__"):
    app.run(debug = True)