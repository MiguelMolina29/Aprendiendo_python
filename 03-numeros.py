# En python existen tres tipos de datos numericos: enteros ( int ), numeros de punto flotante ( float ) y numeros complejos 

# Numeros Enteros 
# De manera basica los numeros enteros son aqullos que no tienen parte decimal. En python los numeros enteros son referenciados con int

# num = 10
# print(num)

# Es importante diferenciar entre una cadena de texto que sería "10"

# En python podemos transformar tipos de datos, una cadena de texto a un numero
num = "10"
num2 = int(num)
print(num2)

# Para separar numeros debemos usar "_"
num3 = 1_000_000
print(num3)
# Todo esto para poder leer de mejor manera el numero

# Numeros de punto flotante
# Los numero flotantes son los que usan una parte decimal 

numf = 1.16
print(numf)

# De mismo modo se puede usar float() para convertir cadenas de texto

# Los numeros de punto flotante si tienen un tamaño maximo en py
# Cifras cercanas a 2e400  sulen superar el tamaño maximo 
# Cuando se alcanza el valor maximo, py devuelve como valor "inf" de infinito


# Numero complejos 
# Py es uno de los pocos lenguajes de programacion que ofrece soporte
# integrado para los numeros complejos.
# Un numero complejo está formado por dos componentes distintos, una
# parte real y la otra imaginaria.
# Se define la parte real con "+" y la imaginaria terminando con "j"