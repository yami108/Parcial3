import funciones
  
def menuPrincial():
    print("\n\t\t...:::: M E N U  P R I N C I P A L ::::...\n")
    opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Buscar\n\t6.- Limpiar\n\t7.- Salir\n\t\tEscribe un opcion: ").strip()
    return opcion

def agregarPeliculas(pelis):
    print("\n\t\t...:::: AGREGAR PELICULAS ::::...\n")
    peli=input("Introducir el nombre de la pelicula: ").upper().strip()
    pelis.append(peli)
    funciones.accionExitosa()

def mostrarPeliculas(pelis):
    print("\n\t\t...:::: MOSTRAR PELICULAS ::::...\n")
    print("\tCodigo\t\tPelicula\n")
    for i in range(0,len(pelis)):
        print(f"{i}\t\t{pelis[i]}")
    funciones.espereTecla()
    
def limpiarPeliculas(pelis):
    if len(pelis)>0:
        pelis=pelis.clear()
        funciones.accionExitosa()
    else:
        input("...¡No hay peliculas que borrar!...") 
        
def buscarPeliculas(pelis):
    print("\n\t\t...:::: BUSCAR PELICULAS ::::...\n")
    caracteristica=input("Escribir el nombre de la caracteristica: ").upper().strip()
    noencontro=False
    for i in pelis:
        if caracteristica==i:
            print("\tCaracteristica\t\tValor\n")
            print(f"{i}\t\t{pelis[i]}")
            noencontro=True
        funciones.espereTecla()
    if not(noencontro):
        input("...LA PELICULA NO FUE ENCONTRADA")

def borrarPeliculas(pelis):
    print("\n\t\t...:::: BORRAR UNA CARACTERISTICA DE LA PELICULA ::::...\n")
    carateristica=input("Escribir el nombre de la caracteristica: ").upper().strip()
    noencontro=True
    for i in pelis:
        if caracteristica==i:
            if peli==pelis[i]:
                opc=""
                while opc!="si" and opc!="no":
                  opc=input("¿Deseas borrar la pelicula (Si/No)? ").lower().strip()
                if opc=="si":
                    pelis.pop(caracteristica) 
                    funciones.accionExitosa())
    if noencontro:
        input("...¡No exite la caraterisctica que estas buscando, verifique!...")
        noencontro=False
        
def modificarPeliculas(pelis):
    print("\n\t\t...:::: MODIFICAR LA CARACTERISTICA DE UNA PELICULA ::::...\n")
    caracteristica=input("Escribir el valor del caracterisctica: ").upper().strip()
    noencontro=True
    for i in pelis:
         if caracterisctica==i:
             opc=""
            while opc!="si" and opc!="no":
                opc=input("¿Deseas modificar la pelicula (Si/No)? ").lower().strip()
                if opc=="si":
                  print("\tCaracteristica\t\tValor\n")
                  print(f"{i}\t\t{pelis[i]}")
                  pelis[caracterisctica]=input("Escribe el nuevo valor de la caracteristica: ").upper().strip() 
                  noencontro=False
                  funciones.accionExitosa()
    else:
        input("...¡No exite la pelicula que estas buscando, verifique!...")