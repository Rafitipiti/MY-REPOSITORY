#ABRIR Y ESCRIBIR EN UN ARCHIVO

archivo = open("archivo.txt", "r")
for linea in archivo.readlines():
    print (linea)
archivo.close()

archivo = open("archivo.txt", "w")
archivo.write("ESCRITURA")
archivo.close()

