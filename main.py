import random
import time
import signal
import os
import colorama
from colorama import Fore

def limpiar():
    os.system("cls || clear")

limpiar()
def saludar(nombre):
    limpiar()
    print(f'{Fore.RED}Hola {nombre} bienvenido al campo de batalla pokemon{Fore.RESET} ')
    
nombre = input(f'{Fore.BLUE}Como te gustaria llamarte? {Fore.RESET}')
if not nombre:
    nombre = "entrenador"

def pokemones():
    print(f'''
{Fore.GREEN}Estos son los pokemones que tienes en tu pokedex{Fore.GREEN}
    {Fore.YELLOW}Bulbasaur
    (1)Bulbasaur
    (2)Charmander
    (3)Pikachu
    (4)Squirtle
    {Fore.RESET}
    Si quieres una eleccion aleatoria solo deja vacia esta opcion ''')

saludar(nombre)
time.sleep(2)
pokemones()

def jugador():
    eleccion = int(input(f'{Fore.YELLOW} Selecciona una opcion 1-4: '))
    if not eleccion:
        eleccion = random.randint(1, 4)
        print(f'{Fore.BLUE} No elegise un pokemon se eligio el pokemon {eleccion}')
    elif eleccion == 1:
        return "Bulbasaur"
    elif eleccion == 2:
        return "Charmander"
    elif eleccion == 3:
        return "Pikachu"
    else:
        return "Squirtle"
    print(f'Elegiste {eleccion}')

def enemigo():
    pokenemigo = random.randint(1, 4)
    if pokenemigo == 1:
        return "Bulbasaur"
    elif pokenemigo == 2:
        return "Charmander"
    elif pokenemigo == 3:
        return "Pikachu"
    else:
        return "Squirtle"
    print(f'El enemigo eligio {pokenemigo}')

def ganador(entrenador, enemigo):
    if entrenador == enemigo:
        ganado = random.choice(["Eligieron el mismo pokemon pero ganaste", "Eligieron el mismo pokemon pero perdiste"])
    elif entrenador == "Bulbasaur" and enemigo == "Pikachu":
        return "El tipo planta le gana al tipo electrico, Ganaste :D"
    elif entrenador == "Pikachu" and enemigo == "Bulbasaur":
        return "El tipo planta le gana al tipo electrico, Perdiste :c"
    elif entrenador == "Pikachu" and enemigo == "Squirtle":
        return "EL tipo agua es debil al electrico, Ganaste :D"
    elif entrenador == "Squirtle" and enemigo == "Pikachu":
        return "El tipo agua es debil al electrico, Perdiste :c"
    elif entrenador == "Squirtle" and enemigo == "Bulbasaur":
        return "El tipo planta es fuerte contra el tipo agua, Perdiste :c"
    elif entrenador == "Bulbasaur" and enemigo == "Squirtle":
        return "El tipo planta es fuerte contra el tipo agua, Ganaste :D"
    elif entrenador == "Charmander" and enemigo == "Squirtle":
        return "El tipo fuego es debil contra el tipo agua, Perdiste :c"
    elif entrenador == "Squirtle" and enemigo == "Charmander":
        return "El tipo fuego es debil conte el tipo agua, Ganaste :D"

def notificacion():
    j = jugador()
    e = enemigo()
    g = ganador(j, e)
    print(f'''
{Fore.GREEN}Elecciones {Fore.RESET}
     {Fore.YELLOW}El enemigo eligio {e}
     Tu elegiste {j}
     
     {Fore.BLUE}
Resultado:
    {g}
{Fore.RESET}
Nota el codigo no esta completo si sale none de resultado es que falta el elif''')
    
notificacion()
def salir():
    limpiar()
    print(f'{Fore.CYAN}Gracias por jugar, saliendo...')
    time.sleep(2)
    limpiar()
    os.system("exit")

jugar = input("Quieres volver a jugar? si/no")
if jugar == "si":
    pokemones()
    notificacion()
elif jugar == "no":
   salir()
else:
    print(f'{Fore.RED}Opcion no valida, salieno...')
    time.sleep(2)
    salir()