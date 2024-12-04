import pygame

# crear un motor para juego
pygame.init()

# Definir las dimensiones que va a tener la ventana
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Juego TRIKI")

# Cargar las imagenes
fondo = pygame.image.load("imagenes/Tablero.png")
circulo = pygame.image.load("imagenes/Circulo.png")
equis = pygame.image.load("imagenes/Equis.png")
ganaX = pygame.image.load("imagenes/X.png")
ganaO = pygame.image.load("imagenes/O.png")
reset = pygame.image.load("imagenes/Reset.png")

# Renderizamos las imagenes
fondo = pygame.transform.scale(fondo, (450, 450))
circulo = pygame.transform.scale(circulo, (125, 125))
equis = pygame.transform.scale(equis, (125, 125))
ganaX = pygame.transform.scale(ganaX, (350, 350))
ganaO = pygame.transform.scale(ganaO, (350, 350))
reset = pygame.transform.scale(reset, (40, 40))

# Creamos las matrices de guia
coordenadas = [[(40, 50), (165, 50), (290, 50)],
               [(40, 175), (165, 175), (290, 175)],
               [(40, 300), (165, 300), (290, 300)]]
tablero = [["", "", ""],
           ["", "", ""],
           ["", "", ""]]

# Variables de control
turno = "O"
gameOver = False
reloj = pygame.time.Clock()


# Establecer la logica del juego
def graficarTablero():
    # Mostramos el fondo o llenamos la ventana con la imagen de fondo
    screen.blit(fondo, (0, 0))
    screen.blit(reset, (0, 0))
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == "O":
                graficaO(fila, columna)
            elif tablero[fila][columna] == "X":
                graficaX(fila, columna)
    
            
# Funcion para graficar la X o la O
def graficaO(fila, columna):
    screen.blit(circulo, coordenadas[fila][columna])       

# Funcion para graficar la X o la O
def graficaX(fila, columna):
    screen.blit(equis, coordenadas[fila][columna])

def ganadorX():
    screen.blit(ganaX, (50, 50))

def ganadorO():
    screen.blit(ganaO, (50, 50))
    

def ganador():
    contarX=0
    for i in range(3):  
        if (tablero[i][0]==tablero[i][1]==tablero[i][2] !=""):
            return True
        if (tablero[0][i]==tablero[1][i]==tablero[2][i] !=""):
            return True
    if (tablero[0][0]==tablero[1][1]==tablero[2][2] !=""):
        return True
    if (tablero[0][2]==tablero[1][1]==tablero[2][0] !=""):
        return True
    
    return False               
#Iniciar el juego

while not gameOver:
    reloj.tick(30)
    
    for event in pygame.event.get():
        #Definimos cuando se cierra el juego con la cerrar
        if event.type == pygame.QUIT:
            gameOver = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425):
                fila = (mouseY-50)//125
                columna = (mouseX-40)//125
                if tablero[fila][columna]=="":
                    tablero[fila][columna]=turno
                    conocerGanador = ganador()
                    if conocerGanador:
                        print("gano")
                        print(turno)
                        if turno == "X":
                            ganadorX()
                        else:
                            ganadorO()                 
                        pygame.display.update() 
                        pygame.time.wait(2000)                        
                    if turno == "O":
                        turno = "X"
                    else:
                        turno = "O" 
            if (mouseX >= 0 and mouseX < 40) and (mouseY >= 0 and mouseY < 40):   
                tablero = [["", "", ""], ["", "", ""], ["", "", ""]]
        graficarTablero()
        pygame.display.update()
    
# Si ya esta lleno el tablero finaliza
pygame.quit