from flask import Flask, request, jsonify 


app = Flask(__name__)


students_list = ['Jack','Geralt','Steven','Pesho','Tony']
courses_list = ['Python', 'Maths' , 'English']
events_list = ['Board meeting', 'Voleyball tournament', 'Football tournament']


@app.route('/students_list', methods=['GET'])
def students_list_method():
    if requst.method == 'GET':
        return jsonify(students_list) 
        
@app.route('/courses_list', methods=['GET'])
def courses_list_method():
    if requst.method == 'GET':
        return jsonify(courses_list)  

@app.route('/events_list', methods=['GET'])
def events_list_method():
    if requst.method == 'GET':
        return jsonify(event_list)   