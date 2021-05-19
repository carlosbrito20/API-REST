from flask import Flask, jsonify

app = Flask(__name__)

from list_poke import list_poke
from name_poke import name_poke

#función para obtener la visualización del JSON de forma local en la ruta http://localhost:4000/list_poke
@app.route('/lis_poke')
def getListPoke():
    return jsonify({'lis_poke': list_poke})


##función para obtener la visualización del JSON de forma local en la ruta http://localhost:4000/nombre
@app.route('/nombre')
def getNamePoke():
    return jsonify({'nombre': name_poke})

if __name__ == '__main__':
    app.run(debug=True, port=4000)