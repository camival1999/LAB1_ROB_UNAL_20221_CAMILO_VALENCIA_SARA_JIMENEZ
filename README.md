Date of creation 17/March/2022.

This repository will contain the work from Camilo Valencia and Sara Jiménez for the course "Robótica 2022-1" in the Universidad Nacional de Colombia Sede Bogotá, starting with "Taller 1"
The content will be from own property  and we'll do our best to keep the repository up to date at all times.

# Laboratorio 1: Introducción a ROS
### Sección A:


### Sección B:
Iniciamos con dos terminales de Kitty abiertos para correr los comandos _roscore_ y *rosrun turtlesim turtlesim_node*, de forma que tengamos la simulación de un TurtleBot, TurtleSim corriendo sin problemas en ROS y comenzamos experimentando un poco con las funciones de ROS en Matlab, lo cual da origen al archivo "turtleSim_Matlab.m". Partimos con el arranque del nodo maestro en Matlab que permite la comunicación con el nodo maestro de ROS. Tras ello hacemos uso de un publisher para enviar datos de velociad linear y angular al tópico "/turtle1/cmd_vel" encargado de publicar el parámetro de velocidad a la tortuga y generar su movimiento. Además de emplear desplazamientos, también podemos pasar los datos de una pose específica mediante el uso de servicios concretos que posee */TurtleSim* como en este caso un servicio que permite teletransportar la tortuga a la pose indicada. Para ello se requiere implementar un cliente y servidor pues la comunicación en los servicios es de dos vías.
