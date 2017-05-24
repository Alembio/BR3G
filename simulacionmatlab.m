% UTEC - Fundamentos de Robotica 2017-1
% Ejemplo robot Fanuc M-10iA 

matlabrc % Para evitar problemas con funciones
addpath('C:\Users\Alessio\Documents\MATLAB\rvctools\common')
addpath('C:\Users\Alessio\Documents\MATLAB\rvctools\robot')

% Declaración de variables
L1 = 0;
L2 = 13;
L3 = 13;

% Definición del robot usando DH (th,d,a,alfa)
L(1)=Link([0, L1, 0, pi/2]);
L(2)=Link([0,     0,  L2,    0]); 
L(3)=Link([0,     0, L3, 0]);

% Creación del robot
br3g = SerialLink(L, 'name', 'BR3G'); 

% Cinemática directa (ejemplo)
br3g.fkine([pi/2 pi/4 -pi/2])

% Visualización
q1 = 0;
B = load('angulos.txt');
N = size(B,1);
puntos = zeros(3,N);


for i=1:N
    q1 = B(i,1) * pi / 180;
    q2 = B(i,2) * pi / 180;
    q3 = B(i,3) * pi / 180;
    
   br3g.plot([q1 q1 q3 ]);
    %pause(0.01);
    A = br3g.fkine([q1 q2 q3-pi]);
    puntos(:,i) = A(1:3,4);
end

figure
plot3(puntos(1,:),puntos(2,:), puntos(3,:), '*')

xlabel('x');
ylabel('y');
zlabel('z');

grid on

%espacio de trabajo
axis ([-26 26 0 26 0 1]);

% ver en plano x, y
view([0 0 1])
