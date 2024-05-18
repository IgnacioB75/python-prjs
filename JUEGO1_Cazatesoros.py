import random

Intro = print("\n🥇 Juego cazatesoros 🏴‍☠️ \n\
Eres el aventurero Peponic Strauv y buscas tu gran tesoro, ¡El gran Rojo! \
Tu misión será encontrarlo atravesando oceanos y desiertos por el gran Kittopolis, el gran mar del pacífico.\n\
Te encontrarás con grandes bestias, desde cucarachas hasta murcielagos...\
¡Pero no temáis! si tu deseo es la fortuna, ser un guerrero valiente y audaz es lo que debes ser.\n") 

# Estadísticas personaje
Salud = 100
Dureza = 100
Felicidad = 50

def datos():
    global Salud,Dureza, Felicidad
    print("- - - - - - - - - - - -")
    print(f'Salud: {Salud}')
    print(f'Dureza: {Dureza}')
    print(f'Felicidad: {Felicidad}')
    print("- - - - - - - - - - - -")

def primer_mar():
    direccion = input()
    if direccion.lower() == 'norte':
        print("Has elegido el mar del Norte, ¡excelente opción! \n")
        mar_norte()
    if direccion.lower() == 'sur':
        print("Has elegido el mar del Sur, ¡excelente opción!")
        mar_sur()

def mar_norte():
    global Salud, Felicidad
    print("En el transcurso de 2 días navegando, te encuentras una isla llena de cocos pero para desembarcar aquí deberás vencer a los nativos, ¡Unos Monos con piedra!")
    accion = input("¿Atacar o correr?\n")
    randOp = random.randint(1,2)
    
    if accion.lower() == "atacar":
        if randOp == 1:
            print("¡Has ganado la pelea! pero te han dañado, has perdido 10 PS")
            Salud -= 10
            datos()
            mar_sur()
            
        if randOp == 2:
            print("¡Has ganado!, y conseguiste un nuevo amigo: ¡Changuito!")
            print("Por tu gran hasaña has conseguido 10 puntos de felicidad")
            Felicidad += 10
            datos()
            tesoro()

    if accion.lower() == "correr":
        print("Has escapado de la pelea, por ser un cobarde tu felicidad ha disminuido -10 puntos")
        Felicidad -= 10
        datos()
        print("Sin embargo, tu aventura ha acabado. Estos mares son solo para valientes ")

def mar_sur():
    global Salud, Felicidad, Dureza
    print("Has arrimado hacia el pueblo de los Paltekos y te ofrecen una palta.")
    opcion = input("¿Aceptas? (Si / No) \n")


    if opcion.lower() == "si":
        print("Los habitantes de Paltek te han dado una palta, les caíste bien.")
        print("¡Has ganado +10 puntos de felicidad!")
        Felicidad += 10
        datos()
        tesoro()
    
    if opcion.lower() == "no":
        print("Los habitantes de Paltek te odian por no aceptarla. Te atacaron con cuchillos y moriste 💀")

def tesoro():
    global Felicidad
    print("\nLuego de tanto viaje te acuestas a dormir 😴... y te das cuenta que toda la aventura fue un sueño. \nTe das cuenta que todo en realidad fue un sueño, te despiertas al lado de tu esposo que te preparó ¡un videojuego en su computadora!")
    input("¿Besar? (Si / No)")
    Felicidad = 100

while True: 
    iniciar = input("¿Deseas continuar..? (Si / No) \n")

    if iniciar.lower() == "si":
        print("¡Comienza tu aventura! deberás elegir si comenzar por el mar del Norte o el Sur.")
        primer_mar()

        print(".......................")
        print("Fin del juego.")
        datos()
        break
    if iniciar.lower() == "no":
        print("Te has ido del juego.")
        break
    else:
        print("\nPor favor, selecciona una opción válida.")

        