#EJERCICIO 1

n = int(input("Ingresa un numero para la serie fibonnaci: ")) 
a, b = 0, 1
contador = 0

while contador < n:
    print(a, end=' ')
    a, b = b, a + b
    contador += 1

# inicializo una variable n para ingresar una cantidad de numeros para la serie fibonnaci

#inicio variables a y b en 0 y 1 respectivamente al ser los primeros numeros de la serie

#mientras que el contador que equivale a 0 sea < n, el contador controla las veces que se va ejecutar el bucles mientras que se cumpla la condicion del while

#intercambio valores de variables donde a va ser b y b va ser la suma de a+b

#contador +=1 para asignarle 1 al contador cada que sea menor que n

#print(a, end=' ') imprime a que ya se le paso el valor que tenia a+b y end es como termina el print por lo general es un salto de linea \n es este caso es un espacio para que los numeros esten seguidos 

#EJERCICIO 2

numero = int(input("Ingresa un número: "))

if numero > 1:  # Un número primo debe ser mayor que 1
    if numero == 2 or numero == 3:  # Casos especiales: 2 y 3 son primos
        print(f"El número {numero} es primo.")
    elif numero % 2 == 0 or numero % 3 == 0:  # Si es divisible por 2 o 3, no es primo
        print(f"El número {numero} no es primo.")
    elif numero % 5 == 0 and numero != 5:  # Divisible por 5 pero distinto de 5
        print(f"El número {numero} no es primo.")
    else:
        print(f"El número {numero} es primo.")  # Si pasa todas las pruebas, es primo
else:
    print(f"El número {numero} no es primo.")

# EJERCICIO 3

#creo inicialmente una lista
#empaqueto la lista
# si a es mayor que b intercambio sus valores
# si b es mayor que c intercambio sus valores
# por si acaso vuelvo a verificar la primera condicion si es necesario

n = [5,4,3] #a mayor que b [5,4,3] si entonces cambian de posiciones [4,5,3], b mayor que c [4,5,3] si entonces cambian de posiciones [4,3,5], a>b si entonces volver a verificar y cambiar posiciones [4,3,5] -->[3,4,5]  

a,b,c = n

if a>b:
    a,b = b,a
if b>c:
    b,c = c,b
if a>b:
    a,b = b,a

print(f"numeros organizados: {a},{b},{c}")

# EJERCICIO 4

cadena = "nauj"
invertida = ""

for i in range(len(cadena)-1, -1, -1): #len = 4-1 = 3 que son el numero de los indices
    invertida+=cadena[i] 

print(invertida)

# len(cadena) - 1: Calcula el indice del último caracter de la cadena  para "nauj", es 3 (porque los índices son 0, 1, 2, 3).

# range(len(cadena) - 1, -1, -1):

# El bucle comienza desde el último índice (3 en este caso) y termina antes de llegar al índice -1 (exclusivo).

# El -1 como paso indica que va hacia atrás, recorriendo en orden inverso.

# invertida += cadena[i]: en cada vuelta añade el caracter de la posición i a la nueva cadena invertida. Esto acumula los caracteres en orden inverso.

#EJERCICIO 5

numero = 0 

factorial = 1 

for i in range(1, numero + 1):   # Itera desde 1 hasta el numero (incluido) en este caso seria 1 

    factorial *= i    # Multiplica el resultado acumulado por el valor actual 

print(f"El factorial de {numero} es: {factorial}") 

#EJERCICIO 6

n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]  # creo la lista con los numeros

par = [] # creo dos listas una para los pares y otra para los impares
impar = []

for i in n:
    if i%2==0:
        par.append(i)
    else:
        impar.append(i)

print(f"numeros pares: {par} \n numeros impares: {impar}")

# uso un for para iterar la lista n
    #si al sacar el modulo de i es == 0 añado esos numeros a la lista par sino a la lista impar

#EJERCICIO 7

palabra = str(input("Ingresar una palabra o frase: ")) #introducir palabra o frase

espacios = palabra.replace(" ","").lower() #quito los espacios de la cadena de caracteres usando replace quitando los espacios y pasando la palabnra o frase a minusculas

if espacios == espacios[::-1]: #verifico si la palabra invertida es igual a la palabra original si es asi es palindromo de lo contrario no es un palindromo
    print(f"la palabra o frase: {palabra} es un palindromo")
else:
    print(f"la palabra o frase: {palabra} no es un palindromo")

#EJERCICIO 8

numero = int(input("Introduce un número entero positivo: ")) #ingresar n numero

if numero < 0: # si el numero es menor a 0 es porque el numero es negativo
    print("Por favor, introduce un número positivo.")
else:
    suma = 0   #si no es negativo el contador de la suma comienza en 0

  
    while numero > 0: # mientras que el numero sea mayor a 0 sera positivo
        digito = numero % 10  # mientras que el numero sea mayor a 0
        suma += digito        # asignar el digito a la suma
        numero = numero // 10   # eliminar el ultimo digito  

    print(f"La suma de los dígitos es: {suma}")

#EJERCICIO 9 

numeros = [5,8,2,10,3,7]

# inicio de variables
mayor = numeros[0]  # asumimos que el primer elemento es el mayor
menor = numeros[0]  # asumimos que el primer elemento es el menor
suma = 0  # para calcular el promedio

for numero in numeros:
    # comparamos para encontrar el mayor
    if numero > mayor:
        mayor = numero
    # comparamos para encontrar el menor
    if numero < menor:
        menor = numero
    # sumamos todos los elementos
    suma += numero

# calculamos el promedio el numero total de elementos que da len entre la suma
promedio = suma / len(numeros)

print(f"Número más grande: {mayor}, Promedio: {promedio}, Número más pequeño: {menor}")

#EJERCICIO 10

cadena = input("Introduce una cadena de texto: ") #ingresar el texto

# crear un diccionario vacio para almacenar el conteo
conteo = {}

# recorrer cada caracter en la cadena
for caracter in cadena:
    if caracter in conteo:
        conteo[caracter] += 1  # si ya existe incremento el contador
    else:
        conteo[caracter] = 1  # si no existe agrego el valor


print(f"Conteo de caracteres: {cadena} \n {conteo}")
