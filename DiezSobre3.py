def obtener_digitos_division(cantidad):
    resultado = str(10 / 3)  # Convertir el resultado de la división a cadena
    return resultado[:cantidad+2]  # Se suma 2 para incluir "3."

if __name__ == '__main__':

    cantidad_digitos = int(input("Ingrese la cantidad de dígitos de 10/3 que desea ver: "))
    print(f'Los primeros {cantidad_digitos} dígitos de 10/3 son: {obtener_digitos_division(cantidad_digitos)}')