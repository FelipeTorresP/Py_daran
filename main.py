import math

def obtener_digitos_pi(cantidad):
    pi_str = str(math.pi)  # Convertir π a cadena
    return pi_str[:cantidad+2]  # Se suma 2 para incluir "3."

if __name__ == '__main__':
    cantidad_digitos = int(input("Ingrese la cantidad de numeros de π que desea ver: "))
    print(f'Los primeros {cantidad_digitos} dígitos de π son: {obtener_digitos_pi(cantidad_digitos)}')
