Date of creation 17/March/2022.

This repository will contain the work from Camilo Valencia and Sara Jiménez for the course "Robótica 2022-1" in the Universidad Nacional de Colombia Sede Bogotá, starting with "Taller 1"
The content will be from own property  and we'll do our best to keep the repository up to date at all times.

# Laboratorio 1: Introducción a ROS
## Sección A:
### Metodología y Resultados
Empleando como guía el artículo compartido (http://www.informit.com/blogs/blog.aspx?uk=The-10-Most-Important-Linux-Commands), comenzamos a explorar el uso del terminal en Linux, en este caso Ubuntu corriendo distintos comando en una variante del terminal instalada llamada Kitty:
1. `pwd`. Este comando sirve  para ver la ubicación donde nos encontramos ahora mismo en el sistema de archivos, tal como "/home/CamiloPC" o cualquier carpeta donde nos encontremos.
2. `ls`. Comando que nos permite ver el contenido en la ruta/carpeta actual o ruta que especifiquemos.
3. `cd`. Uno de los comandos más empleados. Permite moverse entre directorios/carpetas o a rutas que especifiquemos directamte. Se puede combinar con ".." para simplemente regresar al directorio anterior.
4. `touch`. Permite crear archivos, generalmente de texto, con el nombre que especifiquemos.
5. `rm`. Comando que elimina el archivo que deseemos de el directorio actual generalmente. Se puede combinar con más argumentos para eliminar directorios y otro tipo de archivos.
6. `mkdir`. Contrario al caso anterior, permite crear directorios/carpetas nuevas.
7. `rmdir`. Realiza la misma función de `rm` con argumentos adicionales para eliminar directorios directamente.
8. `mv`. Como se puede intuir, proviene del inglés "move" y permite mover archivos o directorios a la ubicación deseada.
9. `cp`. En lugar de mover archivos y/o directorios, los copia.
10. `man`. El comando más útil si se desea revisar información adicional de un comando, muestra el manual del comando que especifiquemos.
 
Aquí podemos ver el resultado de correr cada uno de estos comandos en orden:
![Screenshot from 2022-04-07 18-42-22](https://user-images.githubusercontent.com/55710287/162336786-a43e6b44-1382-4de6-82ef-d69f93cbb326.png)
Y el manual de usuario resultante al llamar `man rm`:
![Screenshot from 2022-04-07 18-42-11](https://user-images.githubusercontent.com/55710287/162336791-09f16a88-31df-419b-9d3d-1c5191302810.png)


### Análisis
Como se puede observar, el terminal de comandos es una gran herramienta para moverse por el sistema de archivos del sistema, y así mismo generar los cambios y modificaciones necesarios de manera ágil. Adicionalemente hay que tener en cuenta el tema de permisos, para lo cual podemos usar el comando prefijo `sudo` y correr el comando que le sigue con permisos de administrador, permitiendo realizar acciones que no serían posibles de otra manera como la eliminación de archivos protegidos o la vista de ciertos archivos ocultos.
## Sección B:
### Metodología y Resultados
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

### Análisis:

Como se pudo observar, es posible tener un manejo completo de ROS desde Matlab, lo cual es muy útil a la hora de emplear cálculos complejos y automatizaciones que no son posibles en el terminal. La parte más compleja es el manejo de servicios, dado que difiere bastante de su forma en el terminal, pero desde luego es de gran utilidad para controlar la pose de la tortuga directamente. Respecto a los resultados obtenidos podemos decir que son satisfactorios: Se logró controlar la tortuga mediante el manejo de publicadores y velocidades, incluso combinando en este caso dos movimientos dirigidos por velocidades lineares y angulares, además de ser capaces de extraer la información de la pose en ciertos puntos con el uso de suscripciones a tópicos, en este caso al tópico de pose. Finalmente no hubo problemas en definir el servidor y cliente necesarios para el uso del servicio de teletransporte y emplear este para manipular de forma directa la pose de la tortuga, junto a la verificación de este cambio empleando la suscripción mencionada y el cierre del nodo maestro en Matlab para finalizar la práctica de esta sección.


## Sección C:

### Metodología y Resultados:
Para realizar este trabajo se inició revisarndo qué topico y servicios se necesitaban usar para lograr cumplir los objetivos del trabajo, estos eran:
- /turtle1/cmd_vel: Permite modificar la velocidad lineal y angular, util para la tarea de desplazarse hacia adelante y atras usando las teclas "W" y "S" y girar en sentido horiario y antihorario usando las teclas"A" y "D" 
- /turtle1/teleport_absolute: Permite ubicar la tortuga en un lugar especifico del espacio usando cómo marco de referencia el mundo, por lo que se dirige a la posición especificada por coordenadas, fue usado al momento de querer regresar al punto inicial 
- /turtle1/teleport_relative: Permite mover la tortuga desde su posición actual en sentido lineal y giros angulares, fue usado al momento de girar 180 grados.

El código consiste en un adeclaración e nodo, 4 funciones y un main.
En la primera parte se debe declarar el nodo y sus elementos que van a ser usados, por esta razón se crearon los dos Proxys para los servicios y el Publisher para el tópico, en estos se llama cada uno y el tipo de dato que recibe, en el caso del Publisher se usa un mensaje tipo Twist y en los servicios son tipo TeleportAbsolut y TeleportRelative. 

Para conocer los tipos se puede usar el comando:`rosservice call /turtle1/teleport_absolute `

Luego iniciando con las funciones tenemos la de conseguir la tecla `getkey` esta fue sacada del planteamiento del taller donde plantean usar la librería termios, esta retorna un valor c que es un binario con la tecla, es decir si presiohnar la tecla W esta función retorna `b'w'` 

La siguiente función `moverLaTortuga` permite crear un mensaje tipo Twist y lo publica por medio del Publisher de nuestro nodo, este mensaje "velocidad" contiene los 6 valores de la velovidad linear y angular en los 3 ejes. 
`       #configuración vel linal en x `
`        velocidad.linear.x=velLinear`
`        velocidad.linear.y=0`
`        velocidad.linear.z=0`
`        #Configuración vel angular` 
`        velocidad.angular.x=0`
`        velocidad.angular.y=0`
`        velocidad.angular.z=velAngular`
Esta función recibe dos entradas la velocidad linear y la angular.

Las siguientes dos funciones son muy similares ya que solo se llama el servicio y se le entregan los parámetros requeridos, en el cado de la `teleAbsLaTortuga()` la posición central se encuentra cuando la coordenada x y y están en 5.5 y el ángulo en ceros. Luego para la función `teleRelTortuga()` se usa pi importado de numpy para girar un valor de pi que es equivalente a 180 grados. 

Por último el main se engarga de que según la tecla detectada se usa cada una de las diferentes funciones previamente definidas. 

Finalmente no en el script se creó una linea en `CMakeLists.txt` para incluir el script previamente realizado`scripts/myTeleop.py`

### Análisis:

Este ejercicio es muy interesante ya que permite no solo conocer cómo funcionan los topicos y los servicios, pero tambien permitió crear un script ejecutable que permite realizar estas funciones desde la consola solo presionando teclas. Una de las dificultades que encontré fue al momento de usar el nodo ya que desconocía que solo se puede crear un nodo por script, por lo que se pudo solucionar creandolo cómo una variable global.

## Conclusiones:
