edad = int(input('Ingrese la edad: '))

if edad in range(0, 10) :
    print('Pertenece a la categoria pre infantil')
elif edad in range(10, 15) :
    print('Pertenece a la categoria infantil')
elif edad in range(15, 18) :
    print('Pertenece a la categoria juvenil')
elif edad in range(18, 21) :
    print('Pertenece a la categoria sub 20')
elif edad in range(21, 80) :
    print('Pertenece a la categoria profesional')
else : 
    print('Edad invalida')
