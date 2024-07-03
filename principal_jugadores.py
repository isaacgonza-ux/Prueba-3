import jugadores as py

eleccion = 0 
while eleccion != 4:
    flag = True
    while flag == True:
        try:
            print("="*50)
            print("Bienvenido a registrarte jugador")
            print("="*50)
            eleccion = int(input("1.-Registrar puntajes del torneo \n2.- Lista todos los puntajes \n3.- Imprimir \n4.- Salir del programa \n--> "))
            if eleccion < 1 or eleccion > 4:
                print("Fuera de rango")
        except:
            print("Solo números")
        else:
            flag = False

    if eleccion == 1:
        print("="*60)
        py.registrar_puntajes()

    elif eleccion == 2:
        print("="*60)
        py.listar_puntajes()

    elif eleccion == 3:
        print("="*60)
        py.imprimir()

    elif eleccion == 4:
        print("="*60)
        print("Salindo.....................")
