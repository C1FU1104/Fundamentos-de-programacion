genero = 'F'
edad = 58
semanas = 240

if genero == 'F':
    if edad >= 58:
        if semanas >= 240:
            print('Si puede pensionar')
        else: 
            print('No se puede pensionar por que le hacen falta ' + str(240-semanas) + 'semanas')
    else:
        print('No se puede pensionar por que le hacen falta ' + str(58-edad) + 'años')
elif genero == 'M':
    if edad >= 65:
        if semanas >= 240:
            print('Si puede pensionar')
        else: 
            print('No se puede pensionar por que le hacen falta ' + str(240-semanas) + 'semanas')
    else:
        print('No se puede pensionar por que le hacen falta ' + str(65-edad) + 'años')
else:
    print('Genero no valido')

    
