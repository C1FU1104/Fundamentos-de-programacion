import os
usuario = "51743"
contrasena = 34715
usuarioEntrada = ""
contrasenaEntrada = 0
nueva_contrasena = 0
sumaCaptcha = "743 + 4"
resultadoSuma = "747"
coordenada1 =[]
coordenada2 =[]
coordenada3 =[]
resultadoSumaEntrada = ""
lista_opciones = ['Cambiar contraseña', 'Ingresar coordenadas actuales', 'Ubicar zona wifi más cercana', 'Guardar archivo con ubicación cercana', 'Actualizar registros de zonas wifi desde archivo', 'Elegir opción de menú favorita','Cerrar sesión']
var_prob = 0
cont = 0
limite = 2
opcion_favorita = 0

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def almacenar_coordenadas():
    global coordenada1
    global coordenada2
    global coordenada3
    coordenada1.insert(0 ,input('Ingrese la latitud de la coordenada 1: '))
    if (not coordenada1[0]) == False:
        if 2.548 <= float(coordenada1[0]) <= 2.766:
            coordenada1.insert(1, input('Ingrese la longitud de la coordenada 1: '))
            if (not coordenada1[1]) == False:
                if  -76.879 <= float(coordenada1[1]) <= -76.493:
                    coordenada2.insert(0, input('Ingrese la latitud de la coordenada 2: '))
                    if (not coordenada2[0]) == False :
                        if 2.548 <= float(coordenada2[0]) <= 2.766:
                            coordenada2.insert(1, input('Ingrese la longitud de la coordenada 2: '))
                            if (not coordenada2[1]) == False :
                                if -76.879 <= float(coordenada2[1]) <= -76.493:
                                    coordenada3.insert(0, input('Ingrese la latitud de la coordenada 3: '))
                                    if (not coordenada3[0]) == False :
                                        if 2.548 <= float(coordenada3[0]) <= 2.766:
                                            coordenada3.insert(1, input('Ingrese la longitud de la coordenada 3: '))
                                            if (not coordenada3[0]) == False :
                                                if -76.879 <= float(coordenada3[1]) <= -76.493:
                                                    menu()
                                                else:
                                                    print('Error coordenada')
                                            else:
                                                print('Error')
                                        else:
                                            print('Error coordenada')
                                    else:
                                        print('Error')
                                else: 
                                    print('Error coordenada')
                            else:
                                print('Error')                             
                        else:
                            print('Error coordenada')
                    else:
                         print('Error')
                else:
                    print('Error coordenada')
            else:
                print('Error')
        else:
            print('Error coordenada')
    else:
        print('Error')                        
                        
def cambiar_coordenadas():
    print("Coordenadas [latitud, longitud] 1 : ['" + str(coordenada1[0]) + "'], ['" + str(coordenada1[1]) +"']")
    print("Coordenadas [latitud, longitud] 2 : ['" + str(coordenada2[0]) + "'], ['" + str(coordenada2[1])+"']")
    print("Coordenadas [latitud, longitud] 3 : ['" + str(coordenada3[0]) + "'], ['" + str(coordenada3[1])+"']")
    if float(coordenada1[0]) > float(coordenada2[0]) > float(coordenada3[0]) :
        print('Coordenada 1 ubicada más al norte')
    elif float(coordenada2[0]) > float(coordenada3[0]):
        print('Coordenada 2 ubicada más al norte')
    else:
        print('Coordenada 3 ubicada más al norte')
    latitud_promedio = round(((float(coordenada1[0]) + float(coordenada2[0]) + float(coordenada3[0]))/3),3)
    longitudud_promedio = round(((float(coordenada1[1]) + float(coordenada2[1]) + float(coordenada3[1]))/3),3)   
    print("Coordenadas ['" +  str(latitud_promedio) + "'], ['" + str(longitudud_promedio) + "'] " +'promedio de todos los puntos')
    print('Presione 1,2 ó 3 para actualizar la respectiva coordenada.')
    print('Presione 0 para regresar al menú')
    seleccion = input()
    if seleccion == '1':
        coordenada1.insert(0 ,input('Ingrese la latitud de la coordenada trabajo: '))
        if (not coordenada1[0]) == False :
            coordenada1.insert(1, input('Ingrese la longitud de la coordenada trabajo: '))
            if (not coordenada1[1]) == False :
                if 2.548 <= float(coordenada1[0]) <= 2.766 and  -76.879 <= float(coordenada1[1]) <= -76.493:
                    menu()
                else:
                    print('Error coordenada')
            else:
                print('Error')
        else:
            print('Error')    
    elif seleccion == '2':
        coordenada2.insert(0 ,input('Ingrese la latitud de la coordenada casa: '))
        if (not coordenada2[0]) == False :
            coordenada2.insert(1, input('Ingrese la longitud de la coordenada casa: '))
            if (not coordenada2[1]) == False :
                if 2.548 <= float(coordenada2[0]) <= 2.766 and  -76.879 <= float(coordenada2[1]) <= -76.493:
                    menu()
                else:
                    print('Error coordenada')
            else:
                print('Error')
        else:
            print('Error')    
    elif seleccion == '3':
        coordenada3.insert(0 ,input('Ingrese la latitud de la coordenada parque: '))
        if (not coordenada3[0]) == False :
            coordenada3.insert(1, input('Ingrese la longitud de la coordenada parque: '))
            if (not coordenada3[1]) == False :
                if 2.548 <= float(coordenada3[0]) <= 2.766 and  -76.879 <= float(coordenada3[1]) <= -76.493:
                    menu()
                else:
                    print('Error coordenada')
            else:
                print('Error')
        else:
            print('Error')    
    elif seleccion == '0':
        menu()
    else:
        print('“Error actualización')

def cambio_contrasena():
    global nueva_contrasena
    global contrasenaEntrada
    global contrasena    
    
    contrasenaEntrada = input('Ingrese la contaseña actual: ')
    if int(contrasenaEntrada) == contrasena:
        nueva_contrasena = int(input('Ingrese la nueva contraseña: '))
        if nueva_contrasena != contrasena:
            contrasena = nueva_contrasena
            menu()
        else:
            print('Error')
    else:
        print('Error')


def adivinanzas() :
    global opcion_favorita
    print("Para continuar responda las siguientes adivinanzas")
    print("Soy el doble de 2, y la mitad del 8")
    print("Ingrese su respuesta")
    respuestAdivinanza = int(input ())
    if (respuestAdivinanza == 4) :
        print("Soy la mitad de 6, y el triple de 1")
        print("Ingrese su respuesta")
        respuestAdivinanza = int(input())
        if (respuestAdivinanza == 3) :
            clear()
            var_prob = lista_opciones[0]
            lista_opciones[0] = lista_opciones[opcion_favorita - 1]
            lista_opciones[opcion_favorita - 1] = var_prob
            menu()
        else :
            print("Error")
            menu()
    else :
        print("Error")
        menu()    
def menu() :   
    global opcion_favorita 
    global cont
    global limite
    print ("1. " + lista_opciones[0])
    print ("2. " + lista_opciones[1])
    print ("3. " + lista_opciones[2])
    print ("4. " + lista_opciones[3])
    print ("5. " + lista_opciones[4])
    print ("6. " + lista_opciones[5])
    print ("7. " + lista_opciones[6])
    opcion_seleccionada = int(input ('Elija una opción: '))    
    if(lista_opciones[opcion_seleccionada-1] == 'Cambiar contraseña'):
        cambio_contrasena()
    elif(lista_opciones[opcion_seleccionada-1] == 'Ingresar coordenadas actuales'):
        if (not coordenada3) == False:
            cambiar_coordenadas()
        else:
            almacenar_coordenadas()
    elif(lista_opciones[opcion_seleccionada-1] == 'Ubicar zona wifi más cercana'):
        print('Usted ha elegido la opción Ubicar zona wifi más cercana')
    elif(lista_opciones[opcion_seleccionada-1] == 'Guardar archivo con ubicación cercana'):
        print('Usted ha elegido la opción Guardar archivo con ubicación cercana')
    elif(lista_opciones[opcion_seleccionada-1] == 'Actualizar registros de zonas wifi desde archivo'):
        print('Usted ha elegido la opción Actualizar registros de zonas wifi desde archivo')
    elif(lista_opciones[opcion_seleccionada-1] == 'Elegir opción de menú favorita'):
        print('Seleccione opción favorita')
        opcion_favorita = int(input ())
        if opcion_favorita < 6 : 
            adivinanzas()
        else :
            print('Error')
    elif(lista_opciones[opcion_seleccionada-1] == 'Cerrar sesión'):
        print("Hasta pronto")
    else :
        while cont < limite :
            print('Error')
            cont = cont + 1
            menu()
        print("Error")
        
print ("Bienvenido al sistema de ubicación para zonas públicas WIFI")
print ("Ingrese su usuario:")
usuarioEntrada = input ()
if (usuarioEntrada == usuario) : 
    contrasenaEntrada = int(input ('Ingrese su contraseña: '))
    if (contrasenaEntrada == contrasena) :
        print ("Para completar el inicio de sesion escriba el resultado de la siguiente suma")
        print (sumaCaptcha)
        resultadoSumaEntrada = input ()
        if (resultadoSumaEntrada == resultadoSuma) :
            print ("Sesión iniciada")
            menu()                 
        else :
            print ("Error")    
    else : 
        print ("Error")    
else : 
    print ("Error")