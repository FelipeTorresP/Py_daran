import math

def obtener_digitos_e(cantidad):
    e_str = str(math.e)  # Convertir e a cadena
    return e_str[:cantidad+2]  # Se suma 2 para incluir "2."

if __name__ == '__main__':
    cantidad_digitos = int(input("Ingrese la cantidad de dígitos de e que desea ver: "))
    print(f'Los primeros {cantidad_digitos} dígitos de e son: {obtener_digitos_e(cantidad_digitos)}')
