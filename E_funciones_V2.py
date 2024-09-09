print("funciones creadas por el usuario")
# las funciones
def Mi_lista():
    print("LISTAS:")
    amigos=["Homero","Paty","Lety"]
    for Vargas in amigos:
        print(Vargas)

def Mi_tupla():
    print("TUPLAS:")
    gatos=("Armin","kira","luna","khao")
    for misg in gatos:
        print(misg)

def Mi_conjunto():
    print("CONJUNTOS:")
    Cdegatos= {"blanco","negro","gris","calico"}
    for colores in Cdegatos:
        print(colores)

def Mi_diccionario():
    print("DICCIONARIOS:")
    papeleria={
        "id": "01",
        "Nombre": "Marcadores",
        "Material": "plastico",
        "Cantidad": "100"
    }
    for mercancia,marcadores in papeleria.items ():
        print(mercancia,marcadores)

# llamadas a funciones
Mi_lista()
print("\n")
Mi_tupla()
print("\n")
Mi_conjunto()
print("\n")
Mi_diccionario()
