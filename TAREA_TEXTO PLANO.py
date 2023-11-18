
#EJERCICIO 1
# Se abre un archivo en modo Append Extended (a+). Si el archivo no
# existe, lo crea, con capacidad de lectura y escrituta. El
# apuntador de escritura se coloca al final del archivo.
archivo="colores.txt"
f = open(archivo,"a+")
# Verificacion de que ya se creo.
if os.path.exists(archivo):
 print("\nEl archivo ya existe")
else:
 print("\nEl archivo no existe")
# Se cierra el archivo.
f.close()

#EJERCICIO 2
# Abro el archivo en modo Write Extended.
# Si el archivo no existe, lo genera. Si existe, lo remplaza.
# Los contenidos van en secuencia.
archivo="colores.txt"
f = open(archivo,"w+")
# Escribo 4 contenidos en secuencia.
f.write("Blanco")
f.write("Negro")
f.write("Naranja")
# Cierro el archivo.
f.close()

#EJERCICIO 3
# Para saltos de línea, se utiliza \n
# Abro el archivo en modo Write Extended
archivo="colores.txt"
f = open(archivo,"w+")
# Escribo 4 líneas adicionales.
f.write("Rojo\n")
f.write("Amarillo\n")
f.write("Verde\n")
# Agregando los elementos de un iterable
mas_colores=["Morado\n","Celeste\n","Rosa\n"]
f.writelines(mas_colores)
# Cierro el archivo.
f.close()

#EJERCICIO 4
archivo="colores.txt"
f = open(archivo,"a+")
# Agregando los elementos de un iterable
mas_colores=["Morado\n","Celeste\n","Rosa\n"]
f.writelines(mas_colores)
# Cierro el archivo.
f.close()

#EJERCICIO 5
# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")
# Leo el contenido y se lo asigno a la variable
# contenido.
contenido=f.read()
# Muestro el contenido. Debe ser todo el archivo.
print(contenido)
# Cierro el archivo.
f.close()

#EJERCICIO 6
# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")
# Leo únicamente los primeros 5 caracteres del archivo.
contenido=f.read(5)
# Muestro el contenido
print(contenido)
# Leo otros 5 caracteres del archivo.
contenido=f.read(5)
# Muestro el contenido
print(contenido)
# Cierro el archivo.
f.close()


#EJERCICIO 7
# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")
# Leo únicamente la primer línea del archivo.
contenido=f.readline()
# Muestro el contenido
print(contenido)
# Leo siguiente línea
contenido=f.readline()
# Muestro el contenido
print(contenido)
# Cierro el archivo.
f.close()

#EJERCICIO 8
# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")
# Leo únicamente los primeros 5 caracteres del arvhivo.
for linea in f:
 print(">", linea)
# Cierro el archivo.
f.close()

#EJERCICIO 9
f.close()
print(f.closed)

#EJERCICIO 10
with open("colores.txt","r") as f:
 contenido=f.read()
 print(contenido)
# Comprobando que, aunque no se aplicó close(), el archivo
# está cerrado.
print("¿Archivo cerrado?",f.closed)

#EJERCICIO 11
# Lista a escribir en un archivo.
marcas=["Audi\n","Alfa Romeo\n","BMW\n","Mercedes Benz\n"]
# Se abre en modo Write Extended, que permite lectura.
with open("marcas.txt","w+") as f:
 # Escribe cada elemento de la lista como una línea
 f.writelines(marcas)
 # Se va al inicio del archivo.
 f.seek(0,0)
 # Lee secuencialmente el archivo, desde el inicio.
 for linea in f:
 print(linea)

#EJERCICIO 12
# Datos iniciales. Entradas es una lista que contiene listas.
Entradas=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]
for e in Entradas:
 print(f'{e[0]}|{e[1]}|{e[2]}')

 #EJERCICIO 13
 # Se imprime el contenido de la lista, para cotejar.
print(">> Contenido de la lista.\n")
print(Entradas)
# Revisa si existe el CSV, en cuyo caso, si existe el BAK lo elimina
# y renombra el CSV como BAK
if os.path.exists("agenda.csv"):
 if (os.path.exists("agenda.bak")):
 os.remove("agenda.bak") 
 os.rename("agenda.csv","agenda.bak")
# Se escribe el contenido de la lista, usando with y F-String
with open("agenda.csv","w+") as f:
 for e in Entradas:
 f.write(f"{e[0]}|{e[1]}|{e[2]}\n")
# Se revisa el contenido del archivo.
print("\n>> Contenido del archivo.\n")
with open("agenda.csv") as f:
 print(f.read())

#EJERCICIO 14
Entradas=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]
with open("agenda.csv","w+") as f:
 for e in Entradas:
 f.write(f"{e[0]}|{e[1]}|{e[2]}\n")


 #EJERCICIO 15
 # Se crea una lista vacía.
Datos=[]
# Se lee el archivo de forma secuencial, y se agregan los elementos
# a la lista.
with open("agenda.csv","r") as f:
 # Se lee secuencialmente el archivo de texto.
 for linea in f:
 # Se toma el texto de la línea leída, y se divide tomando como separador
 # el caracter pipe. La función retorna una lista, donde cada parte del
 # texto es un elemento.
 lista=linea.split("|")
 # El último elemento contiene \n como salto de linea. Se remplaza por nada.
 lista[2]=lista[2].replace("\n","")
 Datos.append(lista)
 
# Se revisa el contenido de la lista
print(">> Contenido de la nueva lista.\n")
print(Datos)

#EJERCICIO  16
Datos=[]
with open("agenda.csv","r+") as f:
 for linea in f:
 lista=linea.split("|")
 lista[2]=lista[2].replace("\n","")
 Datos.append(lista)

#EJERCICIO 17
# Se importa el módulo para trabajar con JSON.
import json
# Se crea un objeto de muestra, para serializar.
Original=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]
print(">> Tipo del objeto.\n")
print(type(Original))
print("\n>> Contenido del objeto.\n")
print(Original)
print("\n>> Serialización a JSON.\n")
Original_JSON=json.dumps(Original,indent=4)
print(Original_JSON)
print("\n>> Deserialización desde JSON.\n")
Nueva_Lista=json.loads(Original_JSON)
print(Nueva_Lista)
print(type(Nueva_Lista))
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==Nueva_Lista)

#EJERCICIO 18
# Grabando el JSON en un archivo.
with open("archivo.json","w+") as f:
 json.dump(Original,f,indent=4)
# Leyendo datos de un archivo json
with open("archivo.json","r") as f:
 recuperados=json.load(f)
print(recuperados)
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==recuperados)

#EJERCICIO 19
# Se importa el módulo para trabajar con JSON.
import pickle
# Observa cómo pickle es un formato binario.
print("\n>> Serialización a Pickle.\n")
Original_pickle=pickle.dumps(Original)
print(Original_pickle)
print("\n>> Deserialización desde Pickle.\n")
Nueva_Lista=pickle.loads(Original_pickle)
print(Nueva_Lista)
print(type(Nueva_Lista))
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==Nueva_Lista)

#EJERCICIO 20
# Grabando el pickle en un archivo.
with open("archivo.pickle","wb+") as f:
 pickle.dump(Original,f)
# Leyendo datos de un archivo pickle
with open("archivo.pickle","rb") as f:
 recuperados=pickle.load(f)
print(recuperados)
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==recuperados)

#EJERCICIO 21
# Datos iniciales. Carga y mostrado.
Entradas=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]
for e in Entradas:
 print(f'{e[0]},{e[1]},{e[2]}')

#EJERCICIO 22
# Verifica si existen los archivos de respaldo, en cuyo
# caso, se eliminan. Usa exists() y remove()
if os.path.exists('agenda.csv.bak'):
 os.remove('agenda.csv.bak')
if os.path.exists('agenda.json.bak'):
 os.remove('agenda.json.bak')
# Verifica si existen los archivos de trabajo con datos, en cuyo
# caso, se renombran a sus equivalentes de respaldo. 
# Usa exists() y rename()
if os.path.exists('agenda.csv'):
 os.rename('agenda.csv','agenda.csv.bak')
if os.path.exists('agenda.json'):
 os.rename('agenda.json','agenda.json.bak')
# Este código no genera salidas.

#EJERCICIO 23
# Abre el archivo de datos CSV, en modo de solo lectura.
# Usa f como apuntador de archivo. Usa open() en modo r.
f=open('agenda.csv','r')
# Lee el contenido del archivo y colócalo en una variable
# llamada contenido. Utiliza read().
contenido=f.read()
# Cierra el archivo. Utiliza close()
f.close()
# Muestra el contenido del archivo, que ya tienes en una variable.
print(contenido)

#EJERCICIO 24
# Se genera una lista vacía llamada Contactos
Contactos=[]
# Abrir el archivo de datos CSV, en modo de solo lectura.
# usa open, en modo r.
f = open('agenda.csv','r')
# Elabora un ciclo for, que coloque en una variable llamada
# linea a cada una de las líneas en el archivo apuntado
# como f. Recuerda que leer un archivo plano con for equivale
# a leerlo línea por línea.
for linea in f: 
 # Asigna a una variable llamada lista_datos, el equivalente
 # en lista del contenido de datos, usando como separador 
 # el pipe line. Usa split(), con "|" como delimitador.
 lista_datos=linea.split('|')
 print(lista_datos)
 # Elimina el salto de línea del último elemento de la lista
 lista_datos[2]=lista_datos[2].replace("\n","")
 # Agrega la lista de datos contenida en lista_datos
 # a la lista Contactos
 Contactos.append(lista_datos)
# Cerrar archivo
f.close()
# Imprime Entradas y Contactos, y comprueba que son iguales
print(Entradas)
print(Contactos)

