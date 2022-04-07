Date of creation 17/March/2022.

This repository will contain the work from Camilo Valencia and Sara Jiménez for the course "Robótica 2022-1" in the Universidad Nacional de Colombia Sede Bogotá, starting with "Taller 1"
The content will be from own property  and we'll do our best to keep the repository up to date at all times.

# Laboratorio 1: Introducción a ROS
### Sección A:


### Sección B:
Iniciamos con dos terminales de Kitty abiertos para correr los comandos `roscore` y `rosrun turtlesim turtlesim_node`, de forma que tengamos la simulación de un TurtleBot, TurtleSim corriendo sin problemas en ROS y comenzamos experimentando un poco con las funciones de ROS en Matlab, lo cual da origen al archivo "turtleSim_Matlab.m". 

![Screenshot from 2022-04-07 17-50-54](https://user-images.githubusercontent.com/55710287/162333613-485e795e-1a8a-4a52-be61-73fd1350ef11.png)

Partimos con el arranque del nodo maestro en Matlab que permite la comunicación con el nodo maestro de ROS. Tras ello hacemos uso de un publisher para enviar datos de velociad linear y angular al tópico "/turtle1/cmd_vel" encargado de publicar el parámetro de velocidad a la tortuga y generar su movimiento, al tiempo que nos podemos suscribir al tópico de pose para obtener información de la misma. 

![Screenshot from 2022-04-07 17-55-04](https://user-images.githubusercontent.com/55710287/162333634-b6ff58fe-3a08-482a-a199-57c94b0846ab.png)

Además de emplear desplazamientos para controlar el movimiento, también podemos pasar los datos de una pose específica mediante el uso de servicios concretos que posee */TurtleSim* como en este caso un servicio que permite teletransportar la tortuga a la pose indicada cuyo comando en terminal es `rosservice call /turtle1/teleport_absolute '{x: x.x, y: y.y, theta: 0.0}'`. Para hacer uso del mismo en Matlab se requiere implementar un cliente y servidor pues la comunicación en los servicios es de dos vías. Se puede apreciar en más detalle y explicación en el mismo código:

![Screenshot from 2022-04-07 17-55-21](https://user-images.githubusercontent.com/55710287/162333670-ab8c5f3a-f73a-4208-bd21-6b8b2a1638c6.png)

Al correr el script de Matlab obtenemos el siguiente movimiento en la tortuga:

![Screenshot from 2022-04-07 17-56-30](https://user-images.githubusercontent.com/55710287/162333682-8beac071-3e88-47ef-b728-3b1dadf8bd66.png)

Con los siguientes reportes de pose obtenidos con la suscripción al tópico de pose:

![Screenshot from 2022-04-07 17-57-06](https://user-images.githubusercontent.com/55710287/162333686-5432364c-f068-4230-9156-c6705bf3aa56.png)


