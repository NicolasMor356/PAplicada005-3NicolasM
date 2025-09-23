###########################################
#################LISTAS####################
###########################################

mi_lista = ["rojo", "azul", "amarillo", "naranja"]

print(mi_lista)#imprime mi lista
print(type(mi_lista))#imprime el tipo de clase que es mi lista
print(mi_lista[2])#imprime el elemento que esta ubicado en la posicion 2 

print("mi_lista size: ", len(mi_lista))#len(mi_lista) lo que hace es calcular el numero de elementos de mi lista
print(mi_lista[0:2])#imprime mi lista del elemento 0 hasta el 2
print(mi_lista[:2])

mi_lista.append("blanco")#agrega al final de mi lista el elemento blanco
print(mi_lista)#imprime la lista

mi_lista.insert(2,"negro")#agrega en la posicion 2 el elemento negro
print(mi_lista)#imprime la lista

mi_lista.extend(["gris" , "cafe"])#concatena la lista [gris, cafe]
print(mi_lista)#imprime la lista

print(mi_lista.index("azul"))#imprime la posicion de "azul"

mi_lista.remove("cafe")#remueve el elemento cafe
print(mi_lista)#imprime la lista

mi_lista.append("morado")#agrega al final de la lista el elemento "morado"
print(mi_lista)#imprime la lista

print(mi_lista.pop())
tamaño = len(mi_lista)#dice que el la variable tamaño va a ser igual a el numero de elementos de la lista
print("tamaño de la lista =", tamaño)#imprime el tamaño de la lista va a ser igual a la variable tamaño

mi_lista.remove("negro")#quita el elemento negro
print(mi_lista)#imprime la lista

mi_lista.remove("gris")#quita el elemento gris
mi_lista.append("beige")#agrega al final de la lista el elemento beige
print(mi_lista)#imprime la lista

print("El tamaño final de mi lista es: ",tamaño)#imprime el tamaño final de la lista

print("-------------------------------------------------")
print("-------------------------------------------------")

mi_numlista = [5,4,8,6,7,10,9,2,3,1]# Lista de números desordenados

print("Ordenando la lista: ")#imprime "Ordenando la lista: "
mi_numlista.sort()#Ordena la lista en forma ascendente
print(mi_numlista)#imprime la lista ya ordenada

mi_numlista.sort(reverse=True) # Ordena en forma descendente
print("ordenandola de mayor a menor seria: ", mi_numlista)# Imprime la lista en orden descendente

###########################################
#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)   # Convierte la lista en una tupla (inmutable)
print()
print()
print("my_tuple: ", my_tupla)   # Imprime la tupla

print(my_tupla[0])   # Imprime el primer elemento de la tupla
print(my_tupla[2])   # Imprime el tercer elemento de la tupla

#Evaluar si un elemento está contenido en la tupla (Devuelve True o False)
print('Rojo' in my_tupla)   # Devuelve True si 'Rojo' está en la tupla
print(my_tupla.count('Rojo'))   # Cuenta cuántas veces aparece 'Rojo'

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')   # Esto NO es una tupla, es un string porque falta la coma
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999   # Crea una tupla automáticamente sin paréntesis
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla   # Se asigna cada valor de la tupla a una variable
print(nombre)   # Imprime 'Gaspar'
print(dia)      # Imprime 5
print(mes)      # Imprime 8
print(año)      # Imprime 1999

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)   # Imprime todo en formato texto

#Convertir una tupla en una lista
my_lista2 = list(my_tupla)   # Convierte la tupla en lista (ahora sí se puede modificar)
print(my_lista2)   # Imprime la lista
