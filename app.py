from flask import Flask,jsonify,request,make_response
from pymongo import MongoClient
from flask_cors import cross_origin,CORS
from DoctorDAO import *
from bson.json_util import dumps


client = MongoClient('mongodb+srv://healthiq23:kOPWhHdNV2BQZGTb@cluster0.byiiwlz.mongodb.net/HealthIQ?retryWrites=true&w=majority')  # Remplacez l'URL par l'URL de votre base de données

# Sélectionnez la base de données
db = client['HealthIQ']

app = Flask(__name__)
CORS(app, origins=['http://localhost:4200'], methods=["OPTIONS", "POST", "GET"])


#cors=CORS(app, resources={r'/*': {'origins': 'http://localhost:4200'}})
@app.route('/')
#@cross_origin(origins=['http://localhost:4200'],methods=["POST"])
def helloCors():
    return "salam"
@app.route('/getallEvents', methods=['POST'])
@cross_origin(origins=['http://localhost:4200'])
def get_users():
  
   try:
    if request.method == 'POST':
        _build_cors_preflight_response()
        data = request.get_json('id')
        print(f"ID reçu depuis Angular : {data}")
        
        DocDAO = DoctorDAO()
        result = DocDAO.get(data)
        return result
   
   except Exception as e:
        print(f"Erreur : {e}")
        return jsonify({"error": str(e)}), 500

#To build a CORS
def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

if __name__ == '__main__':
 
    app.run(debug=True)


