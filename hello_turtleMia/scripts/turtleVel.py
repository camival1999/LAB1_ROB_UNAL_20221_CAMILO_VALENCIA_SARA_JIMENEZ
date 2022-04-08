#!/usr/bin/env python
import rospy #
from geometry_msgs.msg import Twist # se recibe un mensaje tipo geometry twist en la tortuga al moverse 
# mensaje geometry de tipo twist 
def pubVel():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) # crea un publicar y se trae el metodo publisher que se usa para crear publicadores que le apunta al topico cmd_vel con mensaje tipo twist 
    rospy.init_node('velPub', anonymous=False) #se debe crear un noto para poder publicar el nodo se llama velPub
    vel = Twist() #crea el mensaje tipo twist 
    rate = rospy.Rate(10) #publicar el mensaje con una frecuencia de 10 Hz
    while not rospy.is_shutdown(): #mientras que no esté apagado poner:
        vel.linear.x = 2 #estos valores en el mensaje 
        vel.angular.z = 1
        rospy.loginfo(vel) #imprime en la consola de ros 
        pub.publish(vel) #publique el mensaje
        rate.sleep() #sincroniza y espera el tiempo necesario para cumplir la frecuencia asignada 10Hz

if __name__ == '__main__': # este es el main que se ejecuta de primeras en python si no existe se va a ejecutar en orden
    try:
        pubVel() #intenta llamar el metodo publicar velocidad 
    except rospy.ROSInterruptException: #captura escepciones de ros 
        pass #si no logra llamarlo no pasa nada 