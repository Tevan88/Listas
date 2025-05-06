#Lista original:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#Agregamos "jugo" a la lista del 3er cliente.
compras[2].append("jugo")

#Reemplazamos "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

#Eliminamos pan del elemento 0 (que es el primer cliente)
compras[0].remove("pan")

#Mostramos por pantalla la lista actualizada.
print(compras)


