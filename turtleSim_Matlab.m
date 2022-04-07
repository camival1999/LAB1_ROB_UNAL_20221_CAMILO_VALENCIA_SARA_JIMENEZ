%% Primero abrir 2 terminales y correr en cada uno respectivamente:
% roscore -> para correr el nodo maestro de ROS
% rosrun turtlesim turtlesim_node  -> Para correr el simulador de TurtleSim

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
    pause(2)
%% Subscripción a tópico de pose en turtle1
%Definimos el subscriber al topico pose, con el tipo de mensaje obtenido usando en terminal el comando "rostopic info /turtle1/pose"
    poseSub = rossubscriber('/turtle1/pose','turtlesim/Pose'); 

%Pausa opara permitir que la subscripción se procese
    pause(1); 

%Usamos la función "receive()" para poner al subscriptor en modo "escucha",a la espera de que se transmita un mensaje del tópico
    msgPose = receive(poseSub);
    disp("Pose tras finalizar los movimientos")
    disp(msgPose)
%% Envío de una pose aleatoria a turtle1
%Los servicios son un sistema de comunicacion a dos vias, con un cliente
%que pide información o envía solicitudes y un servidor que responde.
%Usamos el servidor/servicio de "/turtle1/teleport_absolute" para
%introducir la pose de la tortuga directamente a través de un cliente que
%definimos como:
%Creación del cliente
    poseClient = rossvcclient("/turtle1/teleport_absolute","DataFormat","object"); 

%Obtenemos el mensaje que necesita el servidor para la comunicación.
    poseReq = rosmessage(poseClient);

%Esperamos a que el cliente se conecte con el servidor de forma exitosa    
    waitForServer(poseClient,"Timeout",3) 

%Introducimos los valores deseados de la pose
    poseReq.X = 3;
    poseReq.Y = 7;
    poseReq.Theta = pi/2;

%Enviamos los valores al servidor mediante el cliente. En este caso no
%esperamos una respuesta dado que buscamos un cambio en la pose de la tortuga.
    poseResp = call(poseClient,poseReq,"Timeout",3);

%Revisamos la información del tópico pose para confirmar la pose introducida.
    msgPose = receive(poseSub);
    disp("Pose tras modificar la pose")
    disp(msgPose)

%% Finalizar nodo maestro de ROS en Matlab
    rosshutdown;