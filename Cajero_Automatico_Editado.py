usuarioRBP = "Nelson"
passwordRBP = "Nelson23"
saldo = 5000
transacciones = []

def validarUsuario(u, p):
    if u == usuarioRBP and p == passwordRBP:
        return True
    return False

def login():
    print("Bienvenido")
    usuario = input("Digite el usuario: ")
    password = input("Digite la contraseña: ")
    return validarUsuario(usuario, password)

def retirar(valor):
    global saldo
    if valor > saldo:
        return False, saldo
    saldo -= valor
    transacciones.append(f"Retiro: -{valor}")
    return True, saldo

def depositar(valor):
    global saldo
    saldo += valor
    transacciones.append(f"Depósito: +{valor}")
    return True, saldo

def mostrarTransacciones():
    print("Historial de Transacciones:")
    for t in transacciones:
        print(t)

def ejecutar():
    if not login():
        print("Usuario o clave incorrectos, intente otra vez.")
        return
    
    while True:
        print("¿Qué operación desea realizar?")
        print("|Depositar - Ingrese -> 1 |Retirar - Ingrese -> 2 |Mostrar Historial - Ingrese -> 3 |Salir - Ingrese -> 4|")
        opcion = int(input(": "))
        
        if opcion == 1:
            valor = int(input("Digite el valor a depositar: " ))
            ok, nuevo_saldo = depositar(valor)
        elif opcion == 2:
            valor = int(input("Ingrese el valor a retirar: "))
            ok, nuevo_saldo = retirar(valor)
        elif opcion == 3:
            mostrarTransacciones()
        elif opcion == 4:
            print("Saliendo del programa. ¡¡GRACIAS POR ELEGIRNOS!!")
            break
        else:
            print("Opción no válida")
        
        if ok:
            print("Acción realizada correctamente, saldo:", nuevo_saldo)
        else:
            print("No se realizó la acción, saldo:", nuevo_saldo)

ejecutar()
