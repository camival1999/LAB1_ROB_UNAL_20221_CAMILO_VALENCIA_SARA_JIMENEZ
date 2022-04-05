%% Arranque del nodo maestro de ROS
rosinit; 
%% Crea un publicador para cmd_vel y su respectivo mensaje
velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist'); 
velMsg = rosmessage(velPub); 
%% Asignamos un valor al mensaje, en este caso desplazamiento linear de 1 unidad en X y lo enviamos con el publicador
velMsg.Linear.X = 1; %Valor del mensaje
send(velPub,velMsg); %Envio
pause(1)