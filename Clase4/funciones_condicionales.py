def verificar_mayor (edad1, edad2, edad3, edad4):
    mayor1=0
    mayor2=0

    if edad1 >= edad2:
       mayor1 = edad1
    else: mayor1 = edad2
    if edad3 >= edad4:
        mayor2 = edad3
    else:
        mayor2 = edad4   
    if mayor1 >= mayor2:
        print(mayor1)
    else:
        print(mayor2)


verificar_mayor(100, 48, 45, 100)
verificar_mayor(15, 80, 35, 35)
verificar_mayor(15, 58, 90, 65)
verificar_mayor(15, 15, 90, 98)
lista = [3,4,6,4,8,2,9,10,200,3,5]
print (max(lista))