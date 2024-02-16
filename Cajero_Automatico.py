usuarioRBP = "Nelson"
passwordRBP = "Nelson23"
saldo = 5000

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
    if valor > saldo:
        return False, saldo
    return True, saldo - valor

def depositar(valor):
    return True, saldo + valor

def accion(opcion):
    if opcion == 1:
        valor = int(input("Digite el valor a depositar: " ))
        return depositar(valor)
    if opcion == 2:
        valor = int(input("Ingrese el valor a retirar: "))
        return retirar(valor)
    return False, saldo

def ejecutar():
    if not login():
        print("Usuario o clave incorrectos, intente otra vez.")
        return
    print("Que operacion desea realizar?")
    opcion = int(input("|Depositar - Ingrese -> 1 |Retirar - Ingrese -> 2|: "))
    ok, saldo = accion(opcion)
    if not ok:
        print("No se reañizo la acción, saldo:", saldo)
    else:
        print("Acción realizada correctamente, saldo:", saldo)
ejecutar()