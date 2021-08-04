import json
from flask import Flask, request, Response
from pymongo import MongoClient
from flask_cors import CORS
import pymongo
import pandas as pd
from bson import json_util
import json
from helper import convert
from sklearn.cluster import KMeans
import numpy as np

app = Flask(__name__)
mongo_uri= 'mongodb+srv://admin:password1234@firstcluster.neuly.mongodb.net/zodiacal?retryWrites=true&w=majority'
CORS(app)

client = MongoClient(mongo_uri)
db = client.zodiacal.nuevosdatos

# Agrega Datos a Mongo
@app.route('/newData', methods=['POST'])
def add_data():
    caracter = request.json['caracter']
    caracteristica = request.json['caracteristica']
    debilidad = request.json['debilidad']
    relacionesAmorosas = request.json['relacionesAmorosas']
    signoZodiacal = request.json['signoZodiacal']
    edad = request.json['edad']
    genero = request.json['genero']

    if (caracter and caracteristica and debilidad and relacionesAmorosas and signoZodiacal and genero and edad):
        db.insert_one(request.json)
        response = {
            'message' : 'Se agrego correctamente',
            'ok': 'true'
        }
        return response
    else:
        return {'message':'Necesitas llenar todos los datos', "ok": "false"}

# Obtiene todos los datos de mongo y los envía como respuesta
@app.route('/getData', methods=['GET'])
def get_data():
    data = db.find({})
    response = json_util.dumps(data)
    return response

# Genera un array con los ejes de X y Y, posteriormente se envían como respuestas en un array
@app.route('/obtenerPuntos', methods=['POST'])
def obtenerPuntos():
    x = []
    y = []
    data = json.loads(json_util.dumps(db.find()))
    columnx= request.json['x']
    columny= request.json['y']
    random= request.json['random']
    for f in data:
        if(columnx != 'edad'):
            x.append(convert(f[columnx], random))
        else:
            x.append(f[columnx])
        
        if(columny != 'edad'):
            y.append(convert(f[columnx], random))
        else:
            y.append(f[columnx])
    Data = {'x': x, 'y': y}
    return Data

# Crea los clusters solicitados de acuerdo a los datos que ya se tienen
@app.route('/obtenerClusters', methods=['POST'])
def aplicarKmeans():
    data = request.json['data']
    clusters = request.json['clusters']
    lista = []

    df = pd.DataFrame(data, columns=['x', 'y'])
    kmeans = KMeans(n_clusters=int(clusters)).fit(df)
    centroid = kmeans.cluster_centers_
    a = np.uint32(centroid)
    a_list = list(a)
    for f in a_list:
        lista.append({"x": int(f[0]), "y": int(f[1])})

    return json_util.dumps(lista)

if __name__ == "__main__":
    app.run(debug=True)