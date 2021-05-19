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
#---------------------------------------------------------------------------------------------

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
        return data 

#LLAMADADO DE FUNCIONES
                                            
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
    

        
