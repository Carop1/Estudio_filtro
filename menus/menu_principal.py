opciones = ['Registrar nuevo cliente','Borrar Cliente','Actualizar Cliente','Buscar','salir']



def generarMainMenu():
    bandera = False
    header="""
    +++++++++++++++++++++++++++++++++++
    + SISTEMA DE REGISTRO DE CLIENTES +
    +++++++++++++++++++++++++++++++++++
    """
    print(header)
    
    for i,item in enumerate(opciones):
        print(f'{(i+1)} - {item}')    
    try:
        opciones_len = int(input("Escriba la opcion del menú que necesita"))
        if opciones_len <= 5:
            badera = True
    except IndexError:
            print("El valor ingresado es invalido")
    else:
            bandera = False
    
    
    return opciones_len, 