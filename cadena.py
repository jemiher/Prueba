cadena1="Hola soy Dalto"
cadena2="Bienvenidos todos"
cadena3="1 23 a b c"
#dir devuelve la lista de atributos válidos del objeto
print(dir(cadena1))

#upper pasa a mayusculas, lower a minusculas
# , capitalize a primera mayusculas
resultado=cadena2.upper()
print(resultado)

#FIND busca cadenas dentro de otras cadenas, 
# cuando no encuentra regresa -1
find=cadena1.find("a")
print(find)

#INDEX funciona igual que find, 
# pero si no encuentra manda error
index=cadena2.index("to")
print(index)

#ISNUMERIC si es numeric manda true
esnumerico=cadena3.isnumeric()
print("Es numerico? ",esnumerico)

#IS ALPHA, devuelve trueo false
alfanumerico=cadena3.isalpha()
print("Es alfanumerico? ", alfanumerico)

#COUNT, dice cuantas veces encuentra una coincidencia
count=cadena1.count("a")
print("Conteo de apariciones: ", count)

#LEN es una funcion que cuenta cuantos caracteres tiene una cadena
len=len(cadena2)
print("Conteo de carácteres: ", len)

#STARWITH dice si una cadena empieza con otra cadena y manda true
start=cadena1.startswith("h")
print("Empieza con...?", start)

#ENDSWITH verifica si una cadena termina con otra cadena dada y manda true
end=cadena2.endswith("s")
print("Termina con...?", end)

#REPLACE reemplaza pedazs de cadena dada por otra dada
reemplaza=cadena2.replace("Bienvenidos","Hola")
print("Nueva cadena 2: ", reemplaza)

#SPLIT separa cadenas con la cadena que le des
split=cadena1.split(",")
print(split)
