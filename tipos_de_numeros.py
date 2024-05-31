edad = 19
estatura = 1.80
n_comp = 5 + 4
estatura = 1.70
peso = 70
imc = peso / (estatura **2)
print(imc)

institucion = "universidad de los lagos"
asignatura = "progamacion"
descripcion = "asignatura de primer semestre de la carrera de ingieneria civil en informatica"
#Imprimir la posicion de un caracter
print (institucion[-1])
#Concatenacion
resultado = print(institucion + " " + asignatura)
#multiplicacion de texto por un numero
salida = print(institucion * 4)
#Utilizando la variable split en la string 
print(institucion.split())
#Len cuenta las palabras
print(len(institucion))
#booleanos
ampolleta = False
interruptor = True
print(type(ampolleta),type(interruptor))
print(type(imc))
print(type(peso))
#comparaciones booleanas
print(1 <= 0)
print(100 >= 10)
print(19 == 19)
#funcion bool
print(bool(0))
print(bool(1))
#listas
ciudades = ["castro", "ancud", "quellon", "chonchi", "castro"]
varios = ["nicolas", 20,True]
print(type(ciudades))
print(type(varios))
#Otra forma de inicializar listas
lista2 = list(["python", "ruby"])
print(ciudades)
print(type(ciudades))
#Cantidad de elementos de una lista
print(len(ciudades))
#Cuenta la cantidad de ocurrencias de una lista
print(ciudades.count("castro"))
#Impresion de elemento especifico en una lista
print(ciudades[-3])
listnum = [1,2,3,4,5,6,7,8,9,10]
listnum2 = list(range(10,1001,10))
print(listnum2)
#Reasignando valores de listas
ciudades[0] = "quemchi"
print(ciudades)
#Tuplas
#Las tuplas tiene que ser actualizadas directamente de donde inicia la lista
musica = tuple()
generos = ("rock", "blues", "pop") 
print(generos)
print(type(generos))
print(generos[2])
#Consulta la posicion de un elemento
print(generos.index("pop"))
#Cambio de estructura tupla a lista
tuplita = ("matthew", 200, "univesidad", True)
print(tuplita)
tuplita = list(tuplita)
print("la tupla ahora es de tipo", type(tuplita))
#tomando un trozo de una tupla
print(tuplita[0:3])
#sets connjuntos
#cada que ocupo add en un set se guarda en cualquier posicion
conjunto_vacio = set()
conjunto_x = {"javascript"}
print(type(conjunto_vacio))
print(type(conjunto_x))
colores = {"azul", "rojo", "amarillo", "verde", "violeta"}
animales = set({"gato",  "perro", "caballo", "hamster"})
print(colores)  
print(animales)
#ingresando un nuevo elemento al set
colores.add("celeste")
print(colores)
#diccionario
paciente = {
    nombre = "nelson" ,
    edad = 30
    ciudad = "castro"}
doctor = dict{
    "nombre" : "elson"
    "edad" : 40,}
print(type(doctor))
print(type(paciente))