import termios, sys, os
import rospy
from geometry_msgs.msg import Twist

from turtlesim.srv import TeleportAbsolute, _TeleportRelative
from numpy import pi



import sys #para uar la linea de comandos
TERMIOS = termios

def teleAbsLaTortuga():
    rospy.init_node('teleAbsTortuga', anonymous=True)#crear el nodo
    
    servi=rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)
    rate=rospy.Rate(10)#la misma rata del mensaje

    posicion=servi(5.5, 5.5, 0.0)

    rate.sleep()#para que se configure según la frecuencia 




if __name__ == '__main__':
    try:
        
        teleAbsLaTortuga()
    except rospy.ROSInterruptException:
        pass