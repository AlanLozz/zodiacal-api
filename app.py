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
db = client.zodiacal.datos

@app.route('/newData', methods=['POST'])
def add_data():
    nombre = request.json['nombre']
    profesion = request.json['profesion']
    esExtrovertido = request.json['esExtrovertido']
    exteriorizaSentimientos = request.json['exteriorizaSentimientos']
    temorCambio = request.json['temorCambio']
    aventuraRiesgo = request.json['aventuraRiesgo']
    emocionesLunaLlena = request.json['emocionesLunaLlena']
    disfrazaSentimientos = request.json['disfrazaSentimientos']
    incomodidadReirLlorar = request.json['incomodidadReirLlorar']
    falsaFelicidad = request.json['falsaFelicidad']
    comparteSentimientosPensamientos = request.json['comparteSentimientosPensamientos']
    personaRacional = request.json['personaRacional']
    vulnerableTemorAmor = request.json['vulnerableTemorAmor']
    preocupacionPercepcion = request.json['preocupacionPercepcion']
    temoresIrracionales = request.json['temoresIrracionales']

    if (nombre and profesion and esExtrovertido and exteriorizaSentimientos and temorCambio and aventuraRiesgo and emocionesLunaLlena and disfrazaSentimientos and incomodidadReirLlorar and falsaFelicidad and comparteSentimientosPensamientos and personaRacional and vulnerableTemorAmor and preocupacionPercepcion and temoresIrracionales
    ):
        db.insert_one({
            'nombre': nombre,
            'profesion': profesion,
            'esExtrovertido': esExtrovertido,
            'exteriorizaSentimientos': exteriorizaSentimientos,
            'temorCambio': temorCambio,
            'aventuraRiesgo': aventuraRiesgo,
            'emocionesLunaLlena': emocionesLunaLlena,
            'disfrazaSentimientos': disfrazaSentimientos,
            'incomodidadReirLlorar': incomodidadReirLlorar,
            'falsaFelicidad': falsaFelicidad,
            'comparteSentimientosPensamientos': comparteSentimientosPensamientos,
            'personaRacional': personaRacional,
            'vulnerableTemorAmor': vulnerableTemorAmor,
            'preocupacionPercepcion': preocupacionPercepcion,
            'temoresIrracionales': temoresIrracionales
        })
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