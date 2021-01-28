from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarSacate():

    glColor3f(0.012,0.724,0)
    glBegin(GL_QUADS)
    glVertex3f(-1.0,-0.5,0.0)
    glVertex3f(1.0,-0.5,0.0)
    glVertex3f(1.0,-1.0,0.0)
    glVertex3f(-1.0,-1.0,0.0)
    glEnd()

def dibujarSol():
    glColor(1, 1, 0.1)
    glBegin(GL_POLYGON)

    for x in range(360):
        angulo = x * 3.1416 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.6,sin(angulo) * 0.2 + 0.6 ,0.0)

    glEnd()

def dibujarCielo():

    glColor3f(0.2, 0.9, 1)
    
    glBegin(GL_QUADS)
    glVertex3f(1.0,1.0,0.0)
    glVertex3f(1.0,-0.5,0.0)
    glVertex3f(-1.0,-0.5,0.0)
    glVertex3f(-1.0,1.0,0.0) 
    
    glEnd()

def dibujarCasa():

    glColor3f(0.8, 0.5, 0.2) 
    
    glBegin(GL_QUADS)
    glVertex3f(0.0,0.3,0.0) #sup izquierdo
    glVertex3f(0.5,0.3,0.0) #sup derecho
    glVertex3f(0.5,-0.5,0.0) #inf derecho
    glVertex3f(0.0,-0.5,0.0) #inf izquierdo
 
    glEnd()

def dibujarPuerta():
    glColor3f(0.4, 0.2, 0)
    
    glBegin(GL_QUADS)
    glVertex3f(0.3,-0.1,0.0) #sup izquierdo
    glVertex3f(0.5,-0.1,0.0) #sup derecho
    glVertex3f(0.5,-0.5,0.0) #inf derecho
    glVertex3f(0.3,-0.5,0.0) #inf izquierdo
 
    glEnd()

def dibujarManija():
    glColor(1,1,1)
    glBegin(GL_POLYGON)

    for x in range(360):
        angulo = x * 3.1416 / 180.0
        glVertex3f(cos(angulo) * 0.02 + 0.45,sin(angulo) * 0.02 - 0.3 ,0.0)

    glEnd()

def dibujarTecho():

    glColor3f(0.5, 0.2, 0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.1,0.3,0.0)
    glVertex3f(0.45,0.8,0.0) #pico
    glVertex3f(.6,0.3,0.0)

    glEnd()

def dibujarVentana():

    glColor3f(0.5, 0.1, 0)
    glBegin(GL_QUADS)
    glVertex3f(0.10,0.2,0.0) #sup izquierdo
    glVertex3f(0.25,0.2,0.0) #sup derecho
    glVertex3f(0.25,-0.1,0.0) #inf derecho
    glVertex3f(0.10,-0.1,0.0) #inf izquierdo
 
    glEnd()

def dibujarVentana1():

    glColor3f(0.2, 0.9, 1)
    glBegin(GL_QUADS)
    glVertex3f(0.11,0.18,0.0) #sup izquierdo
    glVertex3f(0.23,0.18,0.0) #sup derecho
    glVertex3f(0.23,0.05,0.0) #inf derecho
    glVertex3f(0.11,0.05,0.0) #inf izquierdo
 
    glEnd()


def dibujarVentana2():

    glColor3f(0.2, 0.9, 1)
    glBegin(GL_QUADS)
    glVertex3f(0.11,0.04,0.0) #sup izquierdo
    glVertex3f(0.23,0.04,0.0) #sup derecho
    glVertex3f(0.23,-0.08,0.0) #inf derecho
    glVertex3f(0.11,-0.08,0.0) #inf izquierdo

    glEnd()

def dibujarPalo():
    glColor3f(0.6, 0.3, 0.1)
    
    glBegin(GL_QUADS)
    glVertex3f(-0.5,-0.1,0.0) #sup izquierdo
    glVertex3f(-0.6,-0.1,0.0) #sup derecho
    glVertex3f(-0.6,-0.7,0.0) #inf derecho
    glVertex3f(-0.5,-0.7,0.0) #inf izquierdo
 
    glEnd()

def dibujarRamas():
    glColor3f(0.4, 0.5, 0)
    glBegin(GL_POLYGON)

    for x in range(360):
        angulo = x * 3.1416 / 180.0
        glVertex3f(cos(angulo) * 0.2 - 0.6,sin(angulo) * 0.2 -0.1 ,0.0)

    glEnd()

def dibujarRamas1():
    glColor3f(0.4, 0.5, 0)
    glBegin(GL_POLYGON)

    for x in range(360):
        angulo = x * 3.1416 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.6,sin(angulo) * 0.15 +.1 ,0.0)

    glEnd()

def dibujarRamas2():
    glColor3f(0.4, 0.5, 0)
    glBegin(GL_POLYGON)

    for x in range(360):
        angulo = x * 3.1416 / 180.0
        glVertex3f(cos(angulo) * 0.15 - 0.5,sin(angulo) * 0.15  ,0.0)

    glEnd()


def dibujarNubes():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)

    for x in range(360):
        angulo = x * 3.1416 / 180.0
        glVertex3f(cos(angulo) * 0.25 - 0.3,sin(angulo) * 0.1 + .6 ,0.0)

    glEnd()

def dibujarNubes1():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)

    for x in range(360):
        angulo = x * 3.1416 / 180.0
        glVertex3f(cos(angulo) * 0.25 - 0.1,sin(angulo) * 0.1 + .7 ,0.0)

    glEnd()

def dibujarNubes2():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)

    for x in range(360):
        angulo = x * 3.1416 / 180.0
        glVertex3f(cos(angulo) * 0.25 + 0.6,sin(angulo) * 0.1 + .6 ,0.0)

    glEnd()


def dibujarRayos():

    glColor(1, 1, 0.1)
    glBegin(GL_LINES)
    glVertex3f(-0.6,.35,0.0)
    glVertex3f(-0.6,0.5,0.0)

    glVertex3f(-0.35,0.8,0.0)
    glVertex3f(-0.8,0.5,0.0)

    glVertex3f(-0.85,0.8,0.0)
    glVertex3f(-0.3,0.5,0.0)

    glVertex3f(-0.85,0.8,0.0)
    glVertex3f(-0.3,0.5,0.0)

    glVertex3f(-0.6,0.9,0.0)
    glVertex3f(-0.6,0.3,0.0)

    glEnd()

def dibujar():
    #rutinas de dibujo
    dibujarSacate()
    dibujarCielo()
    dibujarNubes()
    dibujarNubes1()
    dibujarNubes2()
    dibujarSol()
    dibujarCasa()
    dibujarPuerta()
    dibujarManija()
    dibujarTecho()
    dibujarVentana()
    dibujarVentana1()
    dibujarVentana2()
    dibujarPalo()
    dibujarRamas()
    dibujarRamas1()
    dibujarRamas2()
    dibujarRayos()



def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.0,0.0,0.0,0.0)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()