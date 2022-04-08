# hello_turtle
En este archivo se realizó un nodo que publica y crea dos servidores para realizar funciones por medio de un topico y dos servicios:

El topico usado fue /turtle1/cmd_vel para poder cambiar la velocidad lineal y angular según la tecla presionada 

Los servicios usados fueron /turtle1/teleport_absolute para movimiento absoluto donde se usa el mundo como marco de referencia y el servicio /turtle1/teleport_relative para poder realizar los giros de 180 grados independientes de la posición 