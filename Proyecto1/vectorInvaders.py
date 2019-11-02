#Proyecto No. 1 Vector Invaders
#Materia: Introducción a la graficación por compuntadora
#Integrantes:
#-Andrés Fidel García González
#-Cruz Alejandro Cordova Alanis

from OpenGL.GLUT import *    
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random
import sys
import subprocess 
import time 

#Musica de fondo
global bgmusica 

global posicionNave 
global vidas 
global Puntuacion 
global banderas, banderasB, banderasC
global disparoYA
global disparoYB
global estado
global puntoCentralX, puntoCentralY 
global disparoPosicion

#Variables para la interaccion con la interfaz
global visible
global menu
global terminar

#Variable para la dificultad del juego
global dificultad  
global limite
global apuntar


#Variables para los enemigos
global enemigoX1, enemigoX2
global enemigoY1, enemigoY2
global direccion
global enemigos

#Variabes para los proyectiles enemigos
global laserEAX, laserEBX
global laserEAY, laserEBY
global estadoLaserE
global direccionE

#Variables para la nave extra
global rango, posicionNaveExtra, estadoExtra

global disminuir

#Metodo para la creación de texto. A
def escritura(font, string):  
  for char in string:
    glutBitmapCharacter(font,ord(char))

#Metodo para la creacion de texto B
def escritura2(font, string):
   for char in string:
       glutStrokeCharacter(fond,ord(char))


#Metodo para mostrar los mensajes en la terminal
def mostrarMensajes():
    print ("Proyecto 1: Vector Invaders")
    print ("Integrantes:")
    print ("Andrés Fidel García González")
    print ("Cruz Alejandro Cordova Alanis")

#Metodo para la inicializacion del escenario
def init():
    global posicionNave
    global vidas
    global Puntuacion
    global banderas, banderasB, banderasC
    global disparoYA
    global disparoYB
    global estado
    global puntoCentralX, puntoCentralY
    global disparoPosicion

    #Para la animacion de destruccion
    global visible
    global contador

    #Dificultad del juego
    global dificultad, limite
    global apuntar
    
    #Proyectiles del enemigo IMPORTANTE
    global ProyectilAY, ProyectilBY
    global ProyectilCentroX, ProyectilCentroY
    global EstadoEnemigo


    
    #Para el menu y final del juego
    global menu
    global finalizar
    global terminar

    #Variables para los enemigo
    global enemigoX1, enemigoX2
    global enemigoY1, enemigoY2
    global direccion #Direccion de los enemigos
    global enemigos

    #Variables para los proyectiles enemigos
    global laserEAX, laserEBX
    global laserEAY, laserEBY
    global estadoLaserE
    global direccionE

    #Nave extra
    global rango, posicionNaveExtra, estadoExtra

    global disminuir

    glClearColor(0.0, 0.0, 0.0, 0.0) 
    posicionNave=0
    vidas=3
    Puntuacion=0
    disparoYA=87.5
    disparoYB=92.5
    estado=False
    puntoCentralX=0.0
    puntoCentralY=0.0
    disparoPosicion=0.0

    visible=True
    contador=0.0
    menu=True 
    finalizar=False 
    terminar=False

    enemigoX1=0.0
    enemigoX2=0.0
    enemigoY1=550
    enemigoY2=580

    direccion=True
    direccionE=True
    enemigos=True

    #Banderas para los bloques
    banderas=[[True for col in range(0,12)] for fila in range(0,5)]
    
    banderasB=[[True for col in range(0,12)] for fila in range(0,5)]

    banderasC=[[True for col in range(0,12)] for fila in range(0,5)]

    estadoExtra=True

    enemigos = [[True for col in range(0,7)] for fila in range(0,5)] 

    estadoLaserE = [[True for col in range(0,7)] for fila in range(0,5)] 
    
    apuntar = [[False for col in range(0,7)] for fila in range(0,5)] 

    disminuir = [[0 for col in range(0,7)] for fila in range(0,5)]

    laserEAX=0.0
    laserEAY=0.0
    laserEBX=0.0
    laserEBY=0.0

    rango=True
    posicionNaveExtra=-200

    dificultad=0
    limite=4
   
  
 
#Metodo para dibujar la vida del jugador
def mostrarVida():
    glColor3f(0.9, 0.9, 0.9)
    glRectf(10.0, 15.0, 40, 30.0);
    glColor3f(0.9, 0.2, 0.0)
    glRectf(20.0, 30.0, 30.0, 40.0);

#Metodo para mostrar el menu principal 
def mostrarTitulo():
    glColor3f(0.0, 0.0, 0.0)
    glRectf(0 , 0, 400, 650)
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos3f(85.0, 400.0, 0.0)
    escritura(GLUT_BITMAP_TIMES_ROMAN_24,"VECTOR INVADERS")
    glRasterPos3f(130.0, 300.0, 0.0)
    escritura(GLUT_BITMAP_HELVETICA_18,"PRESS SPACE")

    glColor3f(1.0, 1.0, 0.0)
    glRasterPos3f(30.0, 200.0, 0.0)
    escritura(GLUT_BITMAP_HELVETICA_18,"Proyecto No. 1")
    glRasterPos3f(30.0, 175.0, 0.0)
    escritura(GLUT_BITMAP_HELVETICA_18,"Integrantes: ")
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos3f(30.0, 145.0, 0.0)
    escritura(GLUT_BITMAP_HELVETICA_18,"-> Andrés Fidel García González")
    glRasterPos3f(30.0, 115.0, 0.0)
    escritura(GLUT_BITMAP_HELVETICA_18,"-> Cruz Alejandro Cordova Alanis")

def finDelJuego():
    global Puntuacion
    glColor3f(0.0, 0.0, 0.0)
    glRectf(0 , 0, 400, 650)
    glColor3f(1.0, 1.0, 1.0)
    glRasterPos3f(115.0, 400.0, 0.0)
    escritura(GLUT_BITMAP_TIMES_ROMAN_24,"GAME OVER")
    glRasterPos3f(130.0, 280.0, 0.0)
    escritura(GLUT_BITMAP_HELVETICA_18,"HI-SCORE: "+str(Puntuacion))



#Metodo para mostrar los mensajes en el escenario
def mensajesInterfaz():
    global Puntuacion
    global vidas
    maxPuntuacion=99999999

    glColor3f(1.0, 1.0, 0.0) 
    glLineWidth(2.0);
    glBegin(GL_LINES);
    glVertex3f(0.0, 60.0, 0.0);
    glVertex3f(400.0, 60.0, 0.0);
    glEnd();

    if vidas>1:
        mostrarVida()
        if vidas>2:
            glPushMatrix()
            glTranslatef(40, 0.0, 0.0)
            mostrarVida()
            glPopMatrix()
   
    glColor3f(0.9, 0.3, 0.0)
    glRasterPos3f(140.0, 40.0, 0.0)
    escritura(GLUT_BITMAP_8_BY_13,"JUGADOR: ")

    glColor3f(1.0, 1.0, 0.0)
    glRasterPos3f(140.0, 20.0, 0.0)
    escritura(GLUT_BITMAP_9_BY_15,"Player 1")

    if Puntuacion>maxPuntuacion:
        Puntuacion=maxPuntuacion

    strPuntuacion = str(Puntuacion)
    lenPuntuacion = len(strPuntuacion)
    printPuntuacion = (8-lenPuntuacion)*'0'+strPuntuacion

    glColor3f(1.0, 1.0, 0.0)
    glRasterPos3f(280.0, 40.0, 0.0)
    escritura(GLUT_BITMAP_8_BY_13,"HI-SCORE")
    glRasterPos3f(280.0, 20.0, 0.0)
    escritura(GLUT_BITMAP_9_BY_15,printPuntuacion)
   
#Metodo para el efecto de destrucción del jugador
def destruirJugador():
    global contador
    global visible
    contador+=0.6
    #Diagonales
    glColor3f(1.0, 0.0+contador/20, 0.0)
    glPushMatrix()
    glTranslatef(contador, contador, 0.0)
    glRectf(posicionNave+15, 72, posicionNave+20, 77)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(contador*-1, contador, 0.0)
    glRectf(posicionNave+15, 72, posicionNave+20, 77)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(contador*-1, contador*-1, 0.0)
    glRectf(posicionNave+15, 72, posicionNave+20, 77)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(contador, contador*-1, 0.0)
    glRectf(posicionNave+15, 72, posicionNave+20, 77)
    glPopMatrix()

    #Horizontales
    glColor3f(0.0+contador/20, 1.0-contador/20, 0.0)
    glPushMatrix()
    glTranslatef(contador, 0.0, 0.0)
    glRectf(posicionNave+10, 72, posicionNave+20, 83)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(contador*-1, 0.0, 0.0)
    glRectf(posicionNave+10, 72, posicionNave+20, 83)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, contador, 0.0)
    glRectf(posicionNave+10, 72, posicionNave+20, 83)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.0, contador*-1, 0.0)
    glRectf(posicionNave+10, 72, posicionNave+20, 83)
    glPopMatrix()

    if contador >= 40:
        visible=True
        contador=0

#Metodo para generar nave extra
def dibujarNaveExtra():
    global posicionNaveExtra
    global estadoExtra, estado
    global puntoCentralX, puntoCentralY
    global Puntuacion

    if puntoCentralX >= posicionNaveExtra and puntoCentralX <= posicionNaveExtra+20 and puntoCentralY >= 620 and estadoExtra==True:
        estadoExtra=False
        estado=False
        disparoYA=87.5
        disparoYB=92.5
        Puntuacion+=100

    if estadoExtra == True:
        glBegin(GL_TRIANGLES)
        glVertex3f(posicionNaveExtra, 5*math.sin(posicionNaveExtra*0.5)+635, 0)
        glVertex3f(posicionNaveExtra+20, 5*math.sin(posicionNaveExtra*0.5)+635, 0)
        glVertex3f(posicionNaveExtra+10, 5*math.sin(posicionNaveExtra*0.5)+615, 0)
        glEnd()

#Metodo para actualizar el escenario
def idle():
    global posicionNaveExtra
    global rango
    if rango:
        if posicionNaveExtra<600:
            posicionNaveExtra+=50/100
        else:
            rango=False
        glutPostRedisplay()
    if rango == False:
        if posicionNaveExtra>-200:
            posicionNaveExtra-=50/100
        else:
            rango=True
        glutPostRedisplay()

#Dibujado de naves
def DibujarNavePrincipal():
    global posicionNave
    global disparoYA, disparoYB
    global puntoCentralX, puntoCentralY 
    global visible

    glColor3f(0.9, 0.2, 0.0)
    glRectf(posicionNave+10.0, 85.0, posicionNave+20.0, 95.0);
    glColor3f(0.9, 0.9, 0.9)
    glRectf(posicionNave, 70.0, posicionNave+30, 85.0);

    #Guardando las coordenadas del punto central del disparo.
    puntoCentralX=posicionNave+15
    puntoCentralY=disparoYA+2.5

    if visible == False:
        destruirJugador()

    glutPostRedisplay()

#Metodo para hacer que el jugador dispare
def disparar():
    global disparoYA, disparoYB
    global disparoPosicion
    posicionNave=0.0
    posicionNave=disparoPosicion

    glColor3f(1.0, 1.0, 0.0)
    glRectf(posicionNave+12.5, disparoYA, posicionNave+17.5, disparoYB);
    
    disparoYA += 5
    disparoYB += 5



#Metodo para generar los disparos de los enemigos
def ataqueEnemigo():
    global laserEnemigoAX, laserEnemigoBY
    global laserEAX, laserEAY, laserEBX, laserEBY
    global estadoLaserE
    global direccionE
    global posicionNave
    global limite, dificultad, apuntar, disminuir
    global puntoCentralX, puntoCentralY

    espacioX=0.0
    espacioY=0.0

    total=0

    for i in range(5):
        for j in range(7):
            glColor3f(0.0, 0.0, 1.0)

            total+=1
            azari=random.randint(1, 35)

            if total == azari and dificultad <= limite and apuntar[i][j] == False and estadoLaserE[i][j] == True:
                dificultad+=1
                apuntar[i][j]=True

            auxX=laserEAX+espacioX
            auxY=laserEBY+espacioY

            if estadoLaserE[i][j] == True and apuntar[i][j] == False:
                #Posicionando disparo en el centro del enemigo
                glRectf(72.5+laserEAX+espacioX, 562.5+laserEAY+espacioY, 77.5+laserEBX+espacioX, 567.5+laserEBY+espacioY)
            else:
                if apuntar[i][j] == True:
                    disminuir[i][j]-=2
                    glRectf(72.5+auxX, 562.5+auxY+disminuir[i][j], 77.5+auxX, 567.5+auxY+disminuir[i][j])
                    
                    #Limitando disparo
                    if  562.5+auxY+disminuir[i][j] <= 0 or puntoCentralX >= 72.5+auxX and puntoCentralX <= 77.5+auxX and puntoCentralY >= 562.5+auxY+disminuir[i][j] or estadoLaserE==False:
                        apuntar[i][j]=False
                        dificultad-=1


            
            espacioX+=40
            
            

                            
            
            if  (60+laserEAX+espacioX) >= 400 and direccionE == True and estadoLaserE[i][j] == True:
                laserEAY-=10
                laserEBY-=10
                direccionE=False 
                
            if  (laserEAX+espacioX) <= 0 and direccionE == False and estadoLaserE[i][j] == True:
                laserEAY-=10
                laserEBY-=10
                direccionE=True

            if j == 6:
                espacioY-=50
                espacioX=0

    if direccion == True:
        laserEAX+=50/100
        laserEBX+=50/100
    
    if direccion == False:
        laserEAX-=50/100
        laserEBX-=50/100

#Metodo para dibujar las naves enemigas normales
def EnemigoNormal():
    glColor3f(2.0, 1.0, 0.0)
    espacioX=0.0
    espacioY=0.0
    global enemigoX1, enemigoX2
    global enemigoY1, enemigoY2
    global direccion
    global enemigos
    global disparoYA, disparoYB
    global estado
    global estadoLaserE
    global dificultad
    global Puntuacion

    for i in range(5):
        for j in range(7):

            if puntoCentralX >= 60+espacioX+enemigoX1 and puntoCentralX <= 90+espacioX+enemigoX2 and puntoCentralY >= enemigoY1+espacioY and puntoCentralY <= espacioY+enemigoY2 and enemigos[i][j]==True:
                enemigos[i][j]=False
                estado=False
                estadoLaserE[i][j]=False
                disparoYA=87.5
                disparoYB=92.5
                if i == 4:
                    Puntuacion += 1
                if i == 3:
                    Puntuacion += 5
                if i == 2: 
                    Puntuacion += 10
                if i == 1:
                    Puntuacion +=20
                if i == 0:
                    Puntuacion +=30

            #Verificando existencia del enemigo
            if enemigos[i][j] == True:
                print ("Enemigo fila : ", i, "col: ",j, "valor: ",enemigos[i][j])
                glRectf(60+espacioX+enemigoX1, espacioY+enemigoY1, 90+espacioX+enemigoX2, espacioY+enemigoY2)
                
            espacioX+=40

            if (60+enemigoX2+espacioX) >= 400 and direccion == True and enemigos[i][j] == True:
                enemigoY1-=10
                enemigoY2-=10
                direccion=False
                    
            if (enemigoX1+espacioX) <= 0 and direccion == False and enemigos[i][j] == True :
                enemigoY1-=10
                enemigoY2-=10
                direccion=True
                
            if j == 6:
                espacioY-=50
                espacioX=0
                
    if direccion == True:
        enemigoX1+=50/100
        enemigoX2+=50/100
    
    if direccion == False:
        enemigoX1-=50/100
        enemigoX2-=50/100


#Metodo para dibujar las defensas en el escenario.
def dibujarDefesa():
    global banderas, banderasB, banderasC, estado
    global puntoCentralX, puntoCentralY
    global disparoYA, disparoYB

    x1=40
    y1=110
    x2=45
    y2=115

    #Dibujando defensa numero 1
    glColor3f(1.0, 0.0, 0.0);
    for i in range(5):
        for j in range(12):
            print ("puntoCentralX: ",puntoCentralX, " puntoCentralY: ",puntoCentralY, "punto Y= ",y1)
            if puntoCentralX >= x1 and puntoCentralX <= x2 and puntoCentralY >= y1 and banderas[i][j]==True and puntoCentralY<=140:
                estado=False
                banderas[i][j]=False
                disparoYA=87.5
                disparoYB=92.5
            
            if puntoCentralY >= 650:
                estado=False
                disparoYA=87.5
                disparoYB=92.5

            if banderas[i][j] == True:
                glRectf(x1, y1, x2, y2);
            x1=x1+5
            x2=x2+5
            print ("i: ",i," j: ",j)
            print ("Bandera: ",banderas[i][j])
            if j == 11:
                y1=y1+5
                y2=y2+5
                x1=40
                x2=45

    x1=170
    y1=110
    x2=175
    y2=115

    #Dibujando defensa numero 2
    glColor3f(1.0, 0.0, 0.0);
    for i in range(5):
        for j in range(12):
            print ("puntoCentralX: ",puntoCentralX, " puntoCentralY: ",puntoCentralY, "punto Y= ",y1)

            if puntoCentralX >= x1 and puntoCentralX <= x2 and puntoCentralY >= y1 and banderasB[i][j]==True and puntoCentralY<=140:
                estado=False
                banderasB[i][j]=False
                disparoYA=87.5
                disparoYB=92.5
               
            if puntoCentralY >= 650:
                estado=False
                disparoYA=87.5
                disparoYB=92.5

            if banderasB[i][j] == True:
                glRectf(x1, y1, x2, y2);
            x1=x1+5
            x2=x2+5
            print ("i: ",i," j: ",j)
            print ("Bandera: ",banderasB[i][j])
            if j == 11:
                y1=y1+5
                y2=y2+5
                x1=170
                x2=175

    x1=300
    y1=110
    x2=305
    y2=115

    #Dibujando defensa numero 3
    glColor3f(1.0, 0.0, 0.0);
    for i in range(5):
        for j in range(12):
            print ("puntoCentralX: ",puntoCentralX, " puntoCentralY: ",puntoCentralY, "punto Y= ",y1)
            if puntoCentralX >= x1 and puntoCentralX <= x2 and puntoCentralY >= y1 and banderasC[i][j]==True and puntoCentralY<=140:
                estado=False
                banderasC[i][j]=False
                disparoYA=87.5
                disparoYB=92.5
                glutPostRedisplay()

            #Limitando el disparo
            if puntoCentralY >= 650:
                estado=False
                disparoYA=87.5
                disparoYB=92.5

            if banderasC[i][j] == True:
                glRectf(x1, y1, x2, y2);
            x1=x1+5
            x2=x2+5
            print ("i: ",i," j: ",j)
            print ("Bandera: ",banderasC[i][j])
            if j == 11:
                y1=y1+5
                y2=y2+5
                x1=300
                x2=305

#Ajustes del escenario.
def redimensionar(w, h): 
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(0.0, 400.0, 0.0, 650.0, -1.0, 1.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity()

#Mostrando el escenario del juego
def mostrarEscenario():
    glClear(GL_COLOR_BUFFER_BIT)

     #Mostrando titulo del juego
    if menu == True:
        mostrarTitulo()
    else:
        mensajesInterfaz()
        
        glColor3f(0.0, 0.0, 0.0)
        DibujarNavePrincipal()
        dibujarDefesa()
        EnemigoNormal()
        
        if estado == True:
            disparar()
            glutPostRedisplay()

        ataqueEnemigo()

        dibujarNaveExtra()

    if terminar == True:
        finDelJuego()
    
        
    glFlush()

#Finalizando la musica al terminar el programa.
def finalizar():
    global bgmusica
    print (" Termino Ventana")  
    bgmusica.terminate()
    sys.exit(0)

#Metodo para las funciones del teclado.
def teclado(key, x, y):
    global Puntuacion
    global vidas
    global posicionNave
    global bgmusica  # Tambien con 
    global estado

    global posicionNave
    global disparoPosicion

    if key == b'a': # izquierda
        if posicionNave>0:
            posicionNave-=2
            glutPostRedisplay();
    
    if key == b'\033': 
        #bgmusica.kill()
        sys.exit(0) 

    if key == b'd':
        if posicionNave<400-30:
            posicionNave+=2
            glutPostRedisplay()

    #Base para cuando el jugador pierde una vida
    if key == b't':
        vidas=vidas-1
        posicionNave=0
        glutPostRedisplay()

    if key == b' ':
        global menu
        menu=False
        glutPostRedisplay()

    if key == b'k':
        estado=True
        disparoPosicion=posicionNave
        #fuego = subprocess.Popen(['mplayer', './rifleHaz.mp3'])
        glutPostRedisplay()
    
    if key == b'l':
        print ("Pruebas para proyectiles enemigos")
        glutPostRedisplay()
    
    #Prueba para destruir nave
    if key == b'u':
        global visible
        visible=False
        glutPostRedisplay()
    
    if key == b'f':
        global terminar
        terminar=True
        glutPostRedisplay()


#Metodo principal main
def main():
    global bgmusica
    #bgmusica = subprocess.Popen(['mplayer', './bgbattletoad.mp3', '-loop','0','&'])
    mostrarMensajes()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(450, 100)
    glutInitWindowSize(400, 560)
    glutCreateWindow("Proyecto No.1 , Vector Ivaders")
    glutReshapeFunc(redimensionar)
    glutDisplayFunc(mostrarEscenario)
    glutKeyboardFunc(teclado)
    glutIdleFunc(idle)
    glutWMCloseFunc(finalizar) 

    init()

    glutMainLoop()
  
main()