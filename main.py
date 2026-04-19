from flask import Flask, request, jsonify
import bd
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")

@app.route('/api/recursos', methods = ['GET'])
def obtener_todo():
    return jsonify(bd.datos), 200

@app.route('/api/recursos/<int:id>', methods=['GET'])
def obtener_id(id):
    if id not in bd.datos:
        return jsonify({"error": "no se encontro"}), 404
    return jsonify(bd.datos[id]), 200

@app.route('/api/recursos', methods=['POST'])
def crear():

    if not request.is_json:
        return jsonify({"error": "cuerpo no JSON"}), 400

    data = request.get_json()

    data["id"] = bd.contador_id
    bd.datos[bd.contador_id] = data
    bd.contador_id += 1

    return jsonify(data), 201

@app.route('/api/recursos/<int:id>', methods = ['PUT'])
def actualizar(id):
    if id not in bd.datos:
        return jsonify({"error": "no eciste"}), 404
    
    if not request.json:
        return jsonify({"error": "no es JSON"}), 400
    
    bd.datos[id].update(request.json)
    return jsonify(bd.datos[id]), 200

@app.route('/api/recursos/<int:id>', methods=['DELETE'])
def eliminar(id):
    if id not in bd.datos:
        return jsonify({"error": "no existe"}), 404
    
    del bd.datos[id]
    return jsonify({"mensaje": "eliminado"}), 200

@app.route('/api/animals', methods=['GET'])
def get_animals():

    name = request.args.get("name", "lion")

    url = f"https://api.api-ninjas.com/v1/animals?name={name}"

    headers = {
        "X-Api-Key": API_KEY.strip()
    }

    response = requests.get(url, headers=headers)

    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(debug=True)