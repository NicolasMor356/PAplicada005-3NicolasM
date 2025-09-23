sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}  
# Crea un diccionario llamado sensors con habitaciones como claves y números como valores.

num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}  
# Crea otro diccionario con ubicaciones como claves y cantidad de cámaras como valores.

print(sensors)  
# Imprime el diccionario sensors completo.

print(num_cameras)  
# Imprime el diccionario num_cameras completo.

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }  
# Diccionario que traduce algunas palabras al idioma ficticio élfico.

print(translations)  
# Imprime el diccionario translations.

#Verifiying an error:
powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3} 

print(powers)  
# Esto nunca se ejecutará correctamente por el error anterior.

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}  
# Diccionario con apellidos como claves y listas de hijos como valores.

print(children)  
# Imprime el diccionario children.

my_empty_dictionary = {}  
# Crea un diccionario vacío.

print(my_empty_dictionary)  
# Imprime el diccionario vacío.

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  
# Diccionario llamado menu con comidas y precios.

print("Before: ", menu)  
# Imprime el menú antes de la modificación.

menu["cheesecake"] = 8  
# Agrega un nuevo elemento al diccionario (cheesecake con precio 8).

print("After", menu)  
# Imprime el menú después de la modificación.

animals_in_zoo = {"dinosaurs": 0}  
# Define un diccionario con "dinosaurs" como clave y 0 como valor.

animals_in_zoo = {"dinosaurs": 0}  
# Lo vuelve a redefinir igual.

animals_in_zoo = {"horses": 2}  
# Vuelve a redefinir el diccionario, ahora con "horses": 2

print(animals_in_zoo)  
# Imprime {"horses": 2}.

#Add multiple keys
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}  
# Crea de nuevo el diccionario sensors.

print("Before", sensors)  
# Imprime antes de la actualización.

# If we wanted to add 3 new rooms, we could use:
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})  
# update() agrega varias claves y valores al diccionario a la vez.

print("After", sensors)  
# Imprime después de la actualización.

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}  
# Diccionario de usuarios y sus IDs.

print(user_ids)  
# Imprime los IDs antes de actualizar.

user_ids.update({"theLooper": 138475, "stringQueen": 85739})  
# Agrega dos nuevos usuarios con sus IDs.

print(user_ids)  
# Imprime después de la actualización.

##Overwrite Values ##
#We know that we can add a key by using the following syntax:
menu["banana"] = 3    

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}  
# Se redefine el diccionario menu.

print("Before: ", menu)  
# Imprime antes de modificar.

menu["oatmeal"] = 5  
# Sobrescribe el valor de la clave "oatmeal", ahora vale 5.

print("After", menu)  
# Imprime después de modificar.

## Notice the value of "oatmeal" has now changed to 5.
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}  
# Diccionario con categorías de premios Oscar y sus ganadores.

print("Before", oscar_winners)  
# Imprime el diccionario inicial.

print()  
# Imprime una línea en blanco.

oscar_winners.update({"Supporting Actress": "Viola Davis"})  
# Agrega la categoría Supporting Actress con su ganadora.

print("After1", oscar_winners)  
# Imprime el diccionario después de la primera actualización.

print()  
# Imprime otra línea en blanco.

oscar_winners["Best Picture"] = "Moonlight"  
# Cambia el valor de "Best Picture" a "Moonlight".

print("After2", oscar_winners)  
# Imprime el diccionario actualizado.

###Dict Comprehensions
#Let’s say we have two lists that we want to combine into a 
#dictionary, like a list of students and a list of their heights, 
#in inches:

names = ['Jenny', 'Alexus', 'Sam', 'Grace']  
# Lista de nombres.

heights = [61, 70, 67, 64]  
# Lista de alturas en pulgadas.

#Python allows you to create a dictionary using 
# a dict comprehension, with this syntax:

zipStudents = zip(names, heights)  
# zip() empareja elementos de ambas listas en tuplas (name, height).

print("zipStudents: ", zipStudents)  
# Imprime el objeto zip (no la lista directamente).

students = {key:value for key, value in zip(names, heights)}  
# Crea un diccionario con comprensión, asignando cada nombre a su altura.

#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}  

print(students)  
# Imprime el diccionario students.

# #zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension:

drinks = ["espresso", "chai", "decaf", "drip"]  
# Lista de bebidas.

caffeine = [64, 40, 0, 120]  
# Lista de niveles de cafeína.

zipped_drinks = zip(drinks, caffeine)  
# zip() junta las dos listas en pares.

print(zipped_drinks)  
# Imprime el objeto zip.

drinks_to_caffeine = {key:value for key, value in zipped_drinks}  
# Crea un diccionario con bebida como clave y cafeína como valor.

print(drinks_to_caffeine)  
# Imprime el diccionario resultante.

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]  
# Lista de canciones.

playcounts = [78, 29, 44, 21, 89, 5]  
# Lista de reproducciones.

plays = {key:value for key, value in zip(songs, playcounts)}  
# Crea un diccionario con cada canción y su número de reproducciones.

print(plays)  
# Imprime el diccionario plays.

plays.update({"Purple Haze": 1})  
# Agrega una nueva canción al diccionario.

plays.update({"Respect": 94})  
# Sobrescribe el valor de "Respect" con 94.

print("After: ", plays)  
# Imprime el diccionario plays actualizado.

library = {"The Best Songs": plays, "Sunday Feelings": {}}  
# Diccionario anidado: una biblioteca con playlists (una tiene canciones, la otra está vacía).

print(library)  
# Imprime la biblioteca completa.
