registro_pelis = {
    "Pelicula Insana": {
        'nombre': "Pelicula Insana",
        'descripcion': "Una película extremadamente intensa y emocionante",
        'categoria': "Suspenso",
        'sala': {
            'A': ['-'] * 10,
            'B': ['-'] * 10,
            'C': ['-'] * 10,
            'D': ['-'] * 10,
            'E': ['-'] * 10,
            'F': ['-'] * 10,
            'G': ['-'] * 10,
            'H': ['-'] * 10,
            'I': ['-'] * 10,
            'J': ['-'] * 10,
            'K': ['-'] * 10,
            'L': ['-'] * 10,
            'M': ['-'] * 10,
            'N': ['-'] * 10,
            'O': ['-'] * 10
        },
        'ventas': 0,
        'asistente': 0,
        'asistente_nombre': []
    }
}

registro_boletas = []


def menu():
    print("MENÚ insano wazaaaaa 👻👽👽👽👾🤖")
    print("1. Mostrar asientos de la sala")
    print("2. Comprar entrada")
    print("3. Mostrar registro de boletas")
    print("4. Salir")


def mostrar_pantalla():
    pelicula = registro_pelis["Pelicula Insana"]
    sala = pelicula['sala']
    print("       Pantalla       ")
    print(" 1 2 3 4 5 6 7 8 9 10")
    for fila, asientos in sala.items():
        print(f"{fila} {' '.join(asientos)}")


def comprar():
    pelicula = registro_pelis["Pelicula Insana"]
    sala = pelicula['sala']
    print("Pantalla")
    print(" 1 2 3 4 5 6 7 8 9 10")
    for fila, asientos in sala.items():
        print(f"{fila} {' '.join(asientos)}")

    fila = input("Ingrese la letra que desee de la A-O: ").upper()
    if fila in sala:
        columna = int(input("Elija una columna del 1-10: "))
        if sala[fila][columna - 1] == '-':
            sala[fila][columna - 1] = 'X'
            pelicula['ventas'] += 1
            pelicula['asistente'] += 1
            nombre_asistente = input("Ingrese nombre de quien verá la función: ")
            precio = 2500
            if input("¿Es estudiante de Duoc? si es alumno DUOC presione S, si no lo es haga lo quiera mi rey 👻👻👻👻 ").lower() == "s":
                precio = precio * 0.7 
            boleta = {'nombre': nombre_asistente, 'precio': precio}
            registro_boletas.append(boleta)
            print("Entrada comprada")
            print("Boleta generada:")
            print("Nombre:", boleta['nombre'])
            print("Precio a pagar:", boleta['precio'])
        else:
            print("Asiento no disponible")
    else:
        print("Asiento no existente")


def mostrar_boletas():
    if len(registro_boletas) == 0:
        print("No hay boletas registradas")
    else:
        print("Registro de Boletas:")
        for boleta in registro_boletas:
            print("Nombre:", boleta['nombre'])
            print("Precio a pagar:", boleta['precio'])
            print("-------------------")


while True:
    menu()
    opcion = input("Ingrese una opción: ")
    if opcion == '1':
        mostrar_pantalla()
    elif opcion == '2':
        comprar()
    elif opcion == '3':
        mostrar_boletas()
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")