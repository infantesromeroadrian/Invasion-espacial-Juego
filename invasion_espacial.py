import pygame
import random
import math

# Inicializa el motor de pygame
pygame.init()

# Crea la ventana
pantalla = pygame.display.set_mode((800,600))

# Carga la imagen
pygame.display.set_caption("Invasion Espacial")

#Tirulo e icocno

pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("invasion-espacial.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("space-galaxy-background.jpg")

#Variables del jugador
jugadorImg = pygame.image.load("astronave-2.png")
jugadorX = 368
jugadorY = 500
jugadorX_change = 0


#Variables enemigo
enemigoImg = []
enemigoX = []
enemigoY = []
enemigoX_change = []
enemigoY_change = []
cantidad_enemigos = 8

for i in range(cantidad_enemigos):
    enemigoImg.append(pygame.image.load("enemigo.png"))
    enemigoX.append(random.randint(0, 736))
    enemigoY.append(random.randint(50, 150))
    enemigoX_change.append(4)
    enemigoY_change.append(40)


enemigoImg = pygame.image.load("nave-espacial.png")
enemigoX = random.randint(0, 736)
enemigoY = random.randint(50, 200)
enemigoX_change = 0.5
enemigoY_change = 50


#Variables bala
balaImg = pygame.image.load("bala.png")
balaX = 0
balaY = 500
balaX_change = 0
balaY_change = 3
bala_visible = False


# Puntaje

puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)


# Funcion jugador
def jugador(x, y):
    pantalla.blit(jugadorImg, (x, y))

# Funcion enemigo
def enemigo(x, y):
    pantalla.blit(enemigoImg, (x, y))

# Funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(balaImg, (x + 16, y + 10))

#Funcion colision

def colision(enemigoX, enemigoY, balaX, balaY):
    distancia = math.sqrt((math.pow(enemigoX - balaX, 2)) + (math.pow(enemigoY - balaY, 2)))
    if distancia < 27:
        return True
    else:
        return False


# Loopeamos hasta que el usuario cierre la ventana
se_ejecuta = True
while se_ejecuta:

    #Imagene de fondo
    pantalla.blit(fondo, (0, 0))


    #Iterar eventos
    for event in pygame.event.get():

        # evento de cierre
        if event.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Izquierda")
                jugadorX_change =-0.1
            if event.key == pygame.K_RIGHT:
                print("Derecha")
                jugadorX_change =-0.1
            if event.key == pygame.K_UP:
                print("Arriba")
                jugadorY -= 0.1
            if event.key == pygame.K_DOWN:
                print("Abajo")
                jugadorY += 0.1
            if event.key == pygame.K_SPACE:
                if not bala_visible:
                    balaX = jugadorX
                    print("Disparar")
                    disparar_bala(balaX, balaY)
                    balaY -= balaY_change

        # evento soltar tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("No se mueve en el eje X")
                jugadorX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                print("No se mueve en el eje Y")
                jugadorY_change = 0


    # Movimiento del jugador
    jugadorX += jugadorX_change


    #mantener dentro de la ventana al jugador
    if jugadorX <= 0:
        jugadorX = 0
    elif jugadorX >= 736:
        jugadorX = 736


    # Movimiento del enemigo
    enemigoX += enemigoX_change


    #mantener dentro de la ventana al enemigo

    for i in range(cantidad_enemigos):
        if enemigoX[i] <= 0:
            enemigoX_change[i] = 0.3
            enemigoY[i] += enemigoY_change[i]
        elif enemigoX[i] >= 736:
            enemigoX_change[i] = -0.3
            enemigoY[i] += enemigoY_change[i]

        # Colision
        colision_enemigo = colision(enemigoX[i], enemigoY[i], balaX, balaY)
        if colision_enemigo:
            balaY = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigoX[i] = random.randint(0, 736)
            enemigoY[i] = random.randint(50, 150)

        enemigo(enemigoX[i], enemigoY[i])

    if enemigoX <= 0:
        enemigoX_change = 1
        enemigoY += enemigoY_change
        enemigoX = 0
    elif enemigoX >= 736:
        enemigoX = -1
        enemigoY += enemigoY_change


    # Movimiento de la bala
    if balaY <= -64:
        balaY = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(balaX, balaY)
        balaY -= balaY_change

    #Colision

    colision = colision(enemigoX, enemigoY, balaX, balaY)
    if colision:
        balaY = 500
        bala_visible = False
        puntaje += 1
        print(puntaje)
        enemigoX = random.randint(0, 736)
        enemigoY = random.randint(50, 200)

    jugador(jugadorX, jugadorY)
    enemigo(enemigoX, enemigoY)


    pygame.display.update()