%% Arranque del nodo maestro de ROS en Matlab
    rosinit; 

%% Crea un publicador para cmd_vel y su respectivo mensaje
    [velPub, velMsg] = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); 

%% Asignamos un valor al mensaje, en este caso una combinación de avance y rotación n formato Twist y lo enviamos con el publicador
    velMsg.Linear.X  = 2;
    velMsg.Linear.Y  = 0;
    velMsg.Linear.Z  = 0;
    velMsg.Angular.X = 0;
    velMsg.Angular.Y = 0;
    velMsg.Angular.Z = 5;
    send(velPub,velMsg); %Envio
    pause(2)

    velMsg.Linear.X  = 4;
    velMsg.Linear.Y  = 0;
    velMsg.Linear.Z  = 0;
    velMsg.Angular.X = 0;
    velMsg.Angular.Y = 0;
    velMsg.Angular.Z = 1;
    send(velPub,velMsg); %Envio

%% Subscripción a tópico de pose en turtle1
%Definimos el subscriber al topico pose, con el tipo de mensaje obtenido usando en terminal el comando "rostopic info /turtle1/pose"
    poseSub = rossubscriber('/turtle1/pose','turtlesim/Pose'); 
    pause(1); %Pausa opara permitir que la subscripción se procese
%Usamos la función "receive()" para poner al subscriptor en modo "escucha",a la espera de que se transmita un mensaje del tópico
    msgPose = receive(poseSub)

%% Envío de una pose aleatoria a turtle1
%Falta agregar script para enviar todos los valores a la pose turtle1,
%revisar rosnode info /turtlesim -> servicios, rosservice call /turtle1/teleport_absolute '{x: 5.5, y: 5.5, theta: 0.0}', rosservice call /clear

%% Finalizar nodo maestro de ROS en Matlab
    rosshutdown;
