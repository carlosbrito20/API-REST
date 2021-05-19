# API-REST

Desarrollo de dos procesos en python.
1- Uso de Flask para levantar dos json.
2- Proceso que consume la API de pokemon.


## Información
Proceso 1:
  Para levantar dos json con el uso de Flask tenemos el proceso llamado app.py que levanta los json que se encuentran dentro de los archivos list_poke.py y name_poke.py.

Proceso 2:
Luego tenemos el proceso main.py el cual consume la API de pokemon https://pokeapi.co/api/v2/pokemon/. 
El mismo está divido dos partes:
  Parte 1. Listar nombres de pokemones de 20 en 20 por offset. siempre y cuando el usuario desee seguir listando.
  Parte 2. Dado el nombre de un pokemon mostrar el mismo por pantalla.

## Visualización de los procesos.
Proceso 1:

Proceso 2:

## Ejecución
Para ejecutar se deben instalar las librerias de python 
--> Ejecutar en visual studio code
--> pip install requests
--> pip install Flask

##Codigo proceso 1
from flask import Flask, jsonify

app = Flask(__name__)

from list_poke import list_poke
from name_poke import name_poke

#función para obtener la visualización del JSON de forma local en la ruta http://localhost:4000/list_poke
@app.route('/lis_poke')
def getListPoke():
    # return jsonify(products)
    return jsonify({'lis_poke': list_poke})


#función para obtener la visualización del JSON de forma local en la ruta http://localhost:4000/nombre
@app.route('/nombre')
def getNamePoke():
    # return jsonify(products)
    return jsonify({'nombre': name_poke})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    
##-----------------------------------------------------------------------------

##Codigo proceso 2
import requests

def get_poke(url='https://pokeapi.co/api/v2/pokemon-form/', offset=0):
    var = {'offset' : offset} if offset else {}

    resp = requests.get(url, params=var)
    
    if resp.status_code == 200:
        carga = resp.json()
        results = carga.get('results', [])
        
        if results:

                for poke in results:
                    nombre_b = poke['name']
                    
                    print("-", nombre_b)
                                            
                fin = input("-- Presione 0 para salir, 1 para continuar listando: ")
                if fin == "1":
                    print("Se listan 20 pokemones adicionales")
                    cant=offset+20
                    cant= cant+20
                    print("Total pokemones listados hasta el momento", cant)
                    
                    get_poke(offset=offset+20)
                elif fin == "0":
                    print("¡Hasta pronto!")
                    exit
                else: print("Valor errado") 
                
###########################################################################################

def main ():
    nombre = input("-- Introduzca el nombre del pokemon: ")
    print("Se muestra pokemon buscado")
    url_completa = url_name + nombre
    data =  get_poke_name(url_completa)
    
    if data:
        tipo = [types['type']['name'] for types in data['types']]
        print(data['name'])
    else: print("No hay data")
    
def get_poke_name(url_v=""):
    resp = requests.get(url_v)
    if resp.status_code == 200:
        data = resp.json()
       # print(resp.json())

        return data 

###########################################################################################
                                            
if __name__ == '__main__':
     
    proc = input("-- Presione 1 para listar pokemones, 2 para buscar por nombre, otro valor para salir del programa: ")
    
    if proc  == "1":
        #url = 'https://pokeapi.co/api/v2/pokemon-form/'
        print("Se muestra listado de 20 pokemones")
        get_poke()

    elif proc  == "2":
        url_name='https://pokeapi.co/api/v2/pokemon/'
        main()

    else: 
        print("Has elegido salir del programa")
        exit

## Test view
Insert here an image of the preview if your project has one. The image can be into the project, you have to indicate the route and look like this.

![](/preview.jpg)
