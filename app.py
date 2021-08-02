from flask import Flask, request
from pymongo import MongoClient
from flask_cors import CORS
import pymongo
import pandas as pd
from bson import json_util

app = Flask(__name__)
mongo_uri= 'mongodb+srv://admin:password1234@firstcluster.neuly.mongodb.net/zodiacal?retryWrites=true&w=majority'
CORS(app)

client = MongoClient(mongo_uri)
db = client.zodiacal.nuevosdatos

@app.route('/newData', methods=['POST'])
def add_data():
    caracter = request.json['caracter']
    caracteristica = request.json['caracteristica']
    debilidad = request.json['debilidad']
    relacionesAmorosas = request.json['relacionesAmorosas']
    signoZodiacal = request.json['signoZodiacal']

    if (caracter and caracteristica and debilidad and relacionesAmorosas and signoZodiacal):
        db.insert_one(request.json)
        response = {
            'message' : 'Se agrego correctamente',
            'ok': 'true'
        }
        return response
    else:
        return {'message':'Necesitas llenar todos los datos', "ok": "false"}

@app.route('/getData', methods=['GET'])
def get_data():
    data = db.find({})
    response = json_util.dumps(data)
    return response

# datas = [data for data in db.find()]
# df_inventory = pd.DataFrame(datas)
# print(df_inventory)

if __name__ == "__main__":
    app.run(debug=True)