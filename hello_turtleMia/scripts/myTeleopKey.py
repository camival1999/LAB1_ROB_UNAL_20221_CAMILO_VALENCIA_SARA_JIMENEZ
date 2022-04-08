import termios, sys, os
import rospy
from geometry_msgs.msg import Twist

from turtlesim.srv import TeleportAbsolute, TeleportRelative
from numpy import pi

import sys #para uar la linea de comandos
TERMIOS = termios

rospy.init_node('miNodoSeLlamaAsi', anonymous=True)#creo el nodo para este programa de python
#ahora las funciones del nodo un publisher y un servicio proxy
servi=rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)#creo el proxy para el servicio el tipo es TeleportAbsolute lo consegui con:rosservice type /turtle1/teleport_relative 
pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)#publicador con nombre /turtle1/cmd_vel con mensaje tipo twist y una rata de 10
servi2=rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)

#Funcion para detectar la tecla regresa la tecla presionada 
def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c

#Funcion para movimiento de la tortuga 
def moverLaTortuga(velLinear,velAngular):
    #rospy.init_node('moviendoTortuga', anonymous=True)#crear el nodo
    #pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)#publicador con nombre /turtle1/cmd_vel con mensaje tipo twist y una rata de 10
    rate=rospy.Rate(10)#la misma rata del mensaje

    velocidad=Twist() #creamos el mensaje 

    #creamos un loop para dar el movimiento 
   
    for x in range(10):
        #al publicar por medio de rostopic pub /turtle1/cmd_vel nos damos cuenta que hay dos categorias linear y angular cada una con 3 valores 
        #configuración vel linal en x 
        velocidad.linear.x=velLinear
        velocidad.linear.y=0
        velocidad.linear.z=0
        #Configuración vel angular 
        velocidad.angular.x=0
        velocidad.angular.y=0
        velocidad.angular.z=velAngular

        #hay que publicar estos valores 
        pub.publish(velocidad)
        rate.sleep()#para que se configure segun la frecuencia 

#función para la teletransportacion absoluta
def teleAbsLaTortuga():
    #rospy.init_node('teleAbsTortuga', anonymous=True)#crear el nodo
    
    #servi=rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)#creo el proxy para el servicio 
    rate=rospy.Rate(10)#la misma rata del mensaje

    posicion=servi(5.5, 5.5, 0.0)

    rate.sleep()#para que se configure según la frecuencia 

def teleRelTortuga():
    rata=rospy.Rate(10)
    son180=pi
    print(son180)
    giro=servi2(0.0, son180)
    rata.sleep()#para que se configure según la frecuencia 






if __name__ == '__main__':
    try:
        #rospy.init_node('miNodoSeLlamaAsi', anonymous=True)#creo el nodo para este programa de python
        #ahora las funciones del nodo un publisher y un servicio proxy
        #servi=rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)#creo el proxy para el servicio 
        #pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)#publicador con nombre /turtle1/cmd_vel con mensaje tipo twist y una rata de 10

        while True:
            print('presione una tecla')
            letra=getkey()        
            print('\n')
            print('la tecla presioada fue: ')
            print(letra)
            prueba=b'y'
            if letra == prueba:
                print('esto es una y')

            tecla=letra


            if tecla == b'w':
                print('se presiona w y va hacia adelante ')
                moverLaTortuga(1,0)
                moverLaTortuga(0,0)
            elif tecla == b's':
                print('se presiona s y va hacia atras ')
                moverLaTortuga(-1,0)
            elif tecla == b'a':
                print('se presiona a y 90 grados gira en sentido antihorario')
                moverLaTortuga(0,1)
            elif tecla == b'd':
                print('se presiona d y gira 90 grados en sentido horario')
                moverLaTortuga(0,-1)
            elif tecla == b'r':
                print('se presiona r y regresa a su pocicion y orientacion centrales')
                teleAbsLaTortuga()
            elif tecla == b' ':
                print('se presiona ESPACIO y gira 180 grados ')
                teleRelTortuga()
                




    except rospy.ROSInterruptException:
        pass