
from flask import Flask,jsonify
from pymongo import MongoClient
from bson.json_util import dumps
class AdminDAO:
    def __init__(self):
        self.mongo=client = MongoClient('mongodb+srv://healthiq23:kOPWhHdNV2BQZGTb@cluster0.byiiwlz.mongodb.net/HealthIQ?retryWrites=true&w=majority')  # Remplacez l'URL par l'URL de votre base de données

        self.db = client['HealthIQ']

    ## @app.route('/get_users', methods=['GET'])
    def get_users(self):
        try:
            # Récupérer tous les documents de la collection "Users"
            users_collection = self.db['Users']
           # cursor = users_collection.find()
            filter_condition = {'role': 'ROLE_USER'}
            cursor = users_collection.find(filter_condition)
            # Convertir le curseur en une liste Python et utiliser dumps pour sérialiser en JSON
            json_result = dumps(list(cursor))

            return json_result
        except Exception as e:
            print(f"Erreur : {e}")
            return jsonify({"error": str(e)}), 500
    def get_doc(self):
        try:
            # Récupérer tous les documents de la collection "Users"
            users_collection = self.db['Users']
           # cursor = users_collection.find()
            filter_condition = {'role': 'ROLE_DOCTOR'}
            cursor = users_collection.find(filter_condition)
            # Convertir le curseur en une liste Python et utiliser dumps pour sérialiser en JSON
            json_result = dumps(list(cursor))

            return json_result
        except Exception as e:
            print(f"Erreur : {e}")
            return jsonify({"error": str(e)}), 500
    def get_allEvent(self):
        try:
            # Récupérer tous les documents de la collection "Users"
            users_collection = self.db['Event']
            cursor = users_collection.find()
            #filter_condition = {'role': 'ROLE_DOCTOR'}
            #cursor = users_collection.find(filter_condition)
            # Convertir le curseur en une liste Python et utiliser dumps pour sérialiser en JSON
            json_result = dumps(list(cursor))

            return json_result
        except Exception as e:
            print(f"Erreur : {e}")
            return jsonify({"error": str(e)}), 500
