import numpy as np

#Funciones
#--- Conversión a años romanos con digitos y agregar el BC o AC según corresponda el año en el rango ---
def romanonumero (year):
	era = ""
	roman = 0
	if year < 0:
		era = "BC"
		roman = 754 + year
	else:
		era = "AC"
		roman = 753 + year
	
	return (roman, era)

#--- Conversión de años romanos con digitos a años romanos con letras ---
def convNumRomano(roman):
	numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
	letras = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

	result = ""
	roman = roman

	while roman > 0:
		for index, numero in enumerate(numeros):
			if roman - numero >= 0 :
				roman -= numero
				result += letras[index]
				break

	return result

#--- Imprimir frase con los datos obtenidos
def imprimirFrase (roman, letras, cantidad):
	print("Límite superior es el año: ", roman, ", romano: ", letras, ", éste ocupa ", cantidad, " espacios para los caracteres.")

#--- Encontrar mayor en el rango ---
def min_space (LI_f, LS_f): 
    value = LI_f
    letras_f = ""
    cantidad = 0
    max_value = 0
    #Se genera un array con los valores del rango, uno para las letras del rango y uno para la vantidad de letras del rango
    myArray = []
    myStringArray = []
    myCountArray = []
    
    var = True
    while (var):
        myArray.append(value)							#Se agrega el valor al array de los valores
        letras_f = convNumRomano(value)			        #Se convierte el valor en letras romanas
        myStringArray.append(letras_f)					#Se agrega el valor al array de las letras
        cantidad = len(letras_f)						#Se convierte las letras romanas en su cantidad
        myCountArray.append(cantidad)					#Se agrega el valor al array de las cantidades de letas
        value+=1
        if value <= LS_f:
            var = False
    max_value = max(myCountArray)
    return max_value

#Implementacion
#Datos de los años
age1 = -1
age2 = 1

#Convertir datos en el dato de entrada
age_r1, bcac1 = romanonumero(age1)
age_r2, bcac2 = romanonumero(age2)

#Datos de entrada
print("\nDatos de entrada: ", abs(age1), bcac1, " - ", abs(age2), bcac2)

#Años en romano con dígitos
print("\nAños romanos en dígitos: ", age_r1, " - ", age_r2)

#Años en romano con letras
age_ltr1 = convNumRomano(age_r1)
age_ltr2 = convNumRomano(age_r2)

#Se cuenta la cantidad de espacios que utilizan los límites
cantidad1 = len(age_ltr1)
cantidad2 = len(age_ltr2)

#Se imprimir frase con los datos obtenidos hasta ahora
imprimirFrase (age_r1, age_ltr1, cantidad1)
imprimirFrase (age_r2, age_ltr2, cantidad2)

#Buscar el mayor valor entre las cantidades de letras dentro del rango
salida = min_space (age_r1, age_r2)

print("\nLa máxima cantidad de espacios necesarios para guardar los números de los años romanos con letras en el rango entre los años ", abs(age1), bcac1, " - ", abs(age2), bcac2, " que es ", age_r1, " - ", age_r2, " en años romanos con dígitos es: ", salida)
print("\nDato de salida: ", salida)

