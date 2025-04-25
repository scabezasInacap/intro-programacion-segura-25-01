# Verificar el acceso seguro

credencialUser = "123-K"
credencialPass = "seguro123"

usuario = input("Ingrese el usuario: ")
contrasena = input("Ingrese la contraseña: ")

if (usuario.lower() == credencialUser.lower() and contrasena == credencialPass):
    print("Acceso permitido")
else:
    print("Acceso denegado")
