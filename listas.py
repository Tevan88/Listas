dias = ["Lunes", "Martes", "Miércoles"]
print(dias)
print(dias[2])
print(type(dias))

lista_range = list(range(1,10))
print(lista_range)

#También se puede agregar el intervalo
lista_range_intervalo = list(range(0,10,2))
print(lista_range_intervalo)

#Utilizar el split nos permite, a una cadena de string separarla y crear una lista con cada elemento:
hola = "Hola mundo cruel ya nunca te veré"
lista_separada = hola.split()
print(lista_separada)

#Slicing, a partir de una lista, quedarme con un elemento determinado
lista_slicing = ["Esteban", 9.8, False, "Jorge", 56]
elemento_determinado = lista_slicing[2]
print(elemento_determinado)
#Y para pedir de un rango determinado:
rango_lista = lista_slicing[0:2]#Los valores deben estar delimitados por ":"
print(rango_lista)

#append para agregar elementos a la lista, siempre los agrega al final de la lista.
lista_slicing.append("Jogo Bonito")
print(lista_slicing)
lista_slicing.append(True)
print(lista_slicing)

#remove sirve para eliminar determinados elementos de la lista.
lista_slicing.remove("Esteban")
print(lista_slicing)

#Actualizar elementos, intercambiar algun elemento de la lista por otro dato.
lista_slicing[2] = "Cambié este elemento"
print(lista_slicing)

#Concatenación, sumar dos ó más listas ó sumar a una lista existente otra nueva lista
lista_slicing2 = lista_slicing + ["Osvaldo", False, 69]
print(lista_slicing2)

#Comprobar si un valor existe dentro de una lista utilizando el término "in".
print(8 in lista_slicing2)
print("Jogo Bonito" in lista_slicing2)

#Listas anidadas, puede haber listas dentro de otras listas.
lista_nueva_anidada = [1, 1.3, ["UTN", "Mendoza"]]
print(lista_nueva_anidada)
lista_nueva_anidada_posicion2 = lista_nueva_anidada[2] #Así extraemos los elementos de la posicion 2 de la lista original, que es otra lista.
print(lista_nueva_anidada_posicion2)
lista_nueva_anidada_posicion2_1 = lista_nueva_anidada_posicion2[1]#Así extraemos el elemento 2 de la lista dentro de la lista.
print(lista_nueva_anidada_posicion2_1)

#Ejercicio
a = [9.1, 8.5]
b = ['UTN', True]
print(a + b)