from Doctor import Doctor
from flask import Flask,jsonify
from pymongo import MongoClient
from bson.json_util import dumps

class DoctorDAO:
    def __init__(self):
        self.mongo=client = MongoClient('mongodb+srv://healthiq23:kOPWhHdNV2BQZGTb@cluster0.byiiwlz.mongodb.net/HealthIQ?retryWrites=true&w=majority')  # Remplacez l'URL par l'URL de votre base de données

        self.db = client['HealthIQ']

    def get(self,id):
     try:
        # Récupérer tous les documents de la collection "Events" avec id_doc égal à 1
        events_collection = self.db['Event']
        filter_condition = {'ID_doc': f"{id}"}
        cursor = events_collection.find(filter_condition)
        
        # Convertir le curseur en une liste Python et utiliser dumps pour sérialiser en JSON
        json_result = dumps(list(cursor))

        return json_result
     except Exception as e:
        print(f"Erreur : {e}")
        return jsonify({"error": str(e)}), 500