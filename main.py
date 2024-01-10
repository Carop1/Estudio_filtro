import menus.menu_principal as mp
import os

if __name__ == '__main__':
    isActiveApp = True
    opMainMenu =0
    
    while (isActiveApp):
        os.system('cls')
        mp.generarMainMenu()
        try:
            opMainMenu = int(input(":)_"))
        except ValueError:
            print("Error en el dato ingresado")
        else:
            if(opMainMenu == 1):
                pass
            elif (opMainMenu == 2):
                pass
            elif (opMainMenu == 3):
                pass
            elif (opMainMenu == 4):
                pass
            elif (opMainMenu == 5):
                isActiveApp = False