
jugadores = []
tipos = ["principiante","intermedio","avanzado"]





def registrar_puntajes():
    juegos = ["Valorant","Fifa","Fornite"]
    id = input("Ingresa tu id: ").lower()
    while len(id) == 0:
        print("No ingresaste datos")
        id = input("Ingresa tu id: ").lower()
    
    nombre = input("Ingresa tu nombre: ").lower()
    while len(nombre)== 0:
        print("No ingresaste datos ")
        nombre = input("Ingresa tu nombre: ").lower()
    
    apellido = input("Ingresa tu apellido: ").lower()
    while len(apellido) == 0:
        print("No ingresaste datos ")
        apellido = input("Ingresa tu apellido: ").lower()
    print(f"Ingresa uno de estos jugos {juegos}")
    
    juego = input("Ingresa tu juego: ").lower()
    while len(juego) == 0:
        print("No ingresaste datos ")
        juego = input("Ingresa tu juego: ").lower()
    
    
    flag = True
    while flag == True:
        try:
            puntaje = int(input("Ingresa tu puntaje: "))
            if puntaje == None:
                print("Debes ingresar datos")
        except:
            print("Solo números")
        else:
                flag = False
                if puntaje <= 5000:
                    tipo = "principiante"

                elif puntaje <= 10000:
                    tipo = "intermedio"
                else:
                    tipo = "avanzado"
    jugador = {
            "ID": id,
            "Nombre":nombre,
            "Apellido": apellido,
            "Juego": juego,
            "Puntaje": puntaje,
            "Tipo": tipo
             }
    jugadores.append(jugador)
    print("Registro exitoso")



def listar_puntajes():
    if len(jugadores) == 0:
        print("No hay puntajes gurdados")
    else: 
        for i in range(len(jugadores)):
            print(f"Datos de los jugadores: {i+1} {jugadores[i]}")



def imprimir():
    if len(jugadores) == 0:
        print("No hay puntajes para imprimir")

    else:
        
        try:
            rango = input("Ingresa un rango \nPrincipiante \nIntermedio \nAvanzado \n--> ").lower()
            for rango in range(len(jugadores)):
                if rango in jugadores:
                    file = open("jugador.txt","w") 
                    file.write(rango)
                    file.close()
                    print("Guardado exitosamente")
        except Exception as error:
            print("Error al guardar",error)





                