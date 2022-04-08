import rospy
from geometry_msgs.msg import Twist

import sys #para uar la linea de comandos 

#al correr roscore  -- rosrun turtlesim turtlesim_node  --- rostopic list 
#podemos ver que hay un publicador para la velocidad (/turtle1/cmd_vel)y la pose (/turtle1/pose)

#Primero definimos una función que tiene cómo entrada la velocidad lineal y angular 

def moverLaTortuga(velLinear,velAngular):
    rospy.init_node('moviendoTortuga', anonymous=True)#crear el nodo
    pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)#publicador con nombre /turtle1/cmd_vel con mensaje tipo twist y una rata de 10
    rate=rospy.Rate(10)#la misma rata del mensaje

    velocidad=Twist() #creamos el mensaje 

    #creamos un loop while
    while True:
        #al publicar por medio de rostopic pub /turtle1/cmd_vel nos damos cuenta que hay dos categorías linear y angular cada una con 3 valores 
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
        rate.sleep()#para que se configure según la frecuencia 


if __name__ == '__main__':
    try:
        moverLaTortuga(-5,2)
    except rospy.ROSInterruptException:
        pass






