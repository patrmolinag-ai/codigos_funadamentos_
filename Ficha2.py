Ficha = {
    "nombre": input("escribe tu nombre"),
    "telefono": "912345678",
    "gmail": "patr.molinag@duocuc.cl",
    "edad": "19",
}
while True:
    print("---Menu---- ")
    print("1 ver ficha ")
    print("2 Editar dato ")
    print("3 Salir ")
    
    opc =int(input("Elija una opcion "))
    if opc == "1":
       print(Ficha)
    elif opc == 2:
     remplazo = input("Que datos desea actualizar")
     if remplazo in Ficha:
      nuevo = input("Ingrese el nuevo dato ")
      Ficha[remplazo] = nuevo
      print("Dato actualizado ")
    
     
    elif opc == 3:
     print("Saliste del progama ")
    break





  