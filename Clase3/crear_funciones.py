def sumar_numeros(num1, num2):
    print('La suma del numero 1 y el numero 2 es. '+ str(num1+num2))

def calcular_doble(numero:int):
    print('El doble de la suma de todos los numeros es: ' + str(numero*2))
    
def calcular_total(num1:float, num2:float, num3:float) -> float:
    total_calculo = num1 + num2 +num3
    return total_calculo

def calcular_promedio(suma):
    print('El promedio es: '+ str(suma/3))
    
numero_1 = float(input('Escriba el primer numero: '))
numero_2 = float(input('Escriba el segundo numero: '))
numero_3 = float(input('Escriba el tercer numero: '))

print('')
print('')

sumar_numeros(numero_1, numero_2)
calcular_doble((numero_1+numero_2+numero_3))
print('La suma total es: ' +str(calcular_total(numero_1, numero_2, numero_3)))
calcular_promedio((numero_1+numero_2+numero_3))
