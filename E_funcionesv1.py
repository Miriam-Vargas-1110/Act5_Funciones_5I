print("Manejo de funciones V1")
def hola_mundo():
    print("Hola aqui estoy dentro de la funcion")

def Mensa(msg):
    print(msg)
def EscribeNC(Nombre, Apellido):
    print(Nombre,Apellido)
    print(f"tu nombre completo es {Nombre} {Apellido}")
def Suma2numeros(n1,n2):
    s=n1+n2
    return f"la suma de {n1} y {n2} es = {s}"
# llamando a la funcion
hola_mundo() 
Mensa("Hola whatsApp") #llama a la funcion mensa con 1 parametro
Mensa("El profe me sorprende enviando mensajes") #llama a la funcion mensa con 1 parametro
EscribeNC("Miriam", "Vargas")
print("Funciones que regresan valores")
print(Suma2numeros(7,3))
print(Suma2numeros(15,45))