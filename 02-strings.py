# Strings, Indexing, Slicing y Stride parte 1

# Un string se corresponde con un conjunto de caracteres que forman una cadena de texto 
# Se pueden definir como " "  o ' '

var = "String con comillas dobles"
var2 = "String con comillas sencillas"

# Indexacion 

# En muchos tipos de datos en Python se pueden acceder a elementos individuales de un conjunto ordenado de datos
# directamente mediante un indice numerico o un valor. Este proceso se llama indexacion 

# En Python las cadenas son secuencias ordenadas de caracteres y por lo tanto pueden ser indexadas de esta manera. Se
# pueden acceder a los caracteres individuales de una cadena especificando el nombre dela cadena seguido de un numero
# entre corchetes [] => Son como los arreglos en js
# El primer caracter de la cadena tiene el indice 0 y el siguiente 1 y asi  sucesivamente

nombre = "Antonio"
#print(nombre[2]) # Tambien se puede utilizar numeros negativos

#Slicing

# Python tambien permite una sintaxis especifica de indexacion que extrae subcadenas de una cadena de texto, a esto se le denomina slicing

nombre = "Antonio Molina"
# print( nombre[0:8] )
# Son maneras de hacer rangos

# Stride 

# El stride es otra variante mas del slicing. Si te añade un : adicional y un tercer indice, se designa un stride, que indica 
# cuantos caracteres saltar hasta obtener el siguiente caracter

nombre = "Miguel Antonio"
# print( nombre[0:8:3] )

# Modificacion de strings

# Un string es un tipo de dato que python considera inmutable, esto quiere decir que no podemos modificar una parte de un string asociada a una variable

# nombre = "Antonio"
# print( nombre[3] )
# nombre[3] = "e"
# print(nombre)

# String de multiples lineas

# Para hacerlo corto => "\n" con esto se hace el tipico salto de linea