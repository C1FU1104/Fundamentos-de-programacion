usuario = "51743"
contrasena = "34715"
usuarioInt = ""
contrasenaInt = ""
capDato1 = "743"
capDato2 = "4"
sumaInt = ""
suma = "747"
var1 = 1
var2 = 2
var3 = 3
var4 = 4
var5 = 5
seleccion = 0

def menu():   


    def menu_inicial ():
        print('1 Opcion ' + str(var1))
        print('2 Opcion ' + str(var2))
        print('3 Opcion ' + str(var3))
        print('4 Opcion ' + str(var4))
        print('5 Opcion ' + str(var5))
        print('6 Cambiar')
        print('7 Cerrar')
        global seleccion
        seleccion = int(input('Seleccione una opción: ')) 
        if seleccion == 6:
            cambiar_menu()
        elif seleccion == 7 :
            print('Hasta pronto')
        else:
            print('Selección incorrecta')
            print('')
            menu_inicial()


    def cambiar_menu ():
        global var1
        global var2
        global var3
        global var4
        global var5

        seleccion = int(input('Seleccione una un favorito: '))

        if seleccion == 1:
            menu_inicial()
        elif seleccion == 2:        
            varprov = var1
            var1 = var2
            var2 = varprov
            menu_inicial()
        elif seleccion == 3:
            varprov = var1
            var1 = var3
            var3 = varprov
            menu_inicial()
        elif seleccion == 4:
            varprov = var1
            var1 = var4
            var4 = varprov
            menu_inicial()
        elif seleccion == 5:
            varprov = var1
            var1 = var5
            var5 = varprov
            menu_inicial()
        else:
            print('Opcion incorrecta')
            print('')
            menu_inicial()

    menu_inicial()

print ("Bienvenido al sistema de ubicación para zonas públicas WIFI")
print ("Ingrese el usuario:")
usuarioInt = input ()
if (usuario == usuarioInt):
    print ("Ingrese la contraseña:")
    contrasenaInt = input()
    if (contrasena == contrasenaInt):
        print (f"Cual es el valor de la suma? {capDato1} + {capDato2}") 
        sumaInt =input()           
        if (sumaInt == suma):
            print("Sesión iniciada")
            menu()
        else:
            print("Error")
    else:  
        print("Error")  
else:
    print("Error")
