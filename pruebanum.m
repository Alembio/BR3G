matlabrc % Para evitar problemas con funciones
addpath('C:\Users\Alessio\Documents\MATLAB\rvctools\common')
addpath('C:\Users\Alessio\Documents\MATLAB\rvctools\robot')


A = load('utec.txt')/10/100;
N = [];
for k = 1:3:(length(A))
    N = [N; A(k) A(k+1) A(k+2)];
end

h  = 0.07;
l1 = 0.115;
l4 = 0.16;
d  = 0.025;

% Definición del robot usando DH (th,d,a,alfa)
L(1)=Link([0,   h,  0, pi/2]);
L(2)=Link([0,   0, l1, pi]); 
L(3)=Link([0,  -d, l4, 0]);

% Creación del robot
robot = SerialLink(L, 'name', 'robot'); 

q = [270; 135; 240];
qq = []; X=[]; ff = [];
xx=[]; yy=[]; zz=[];

for i=1:size(N,1)
    qq = [qq q]; 
    r = 0.05;
    % x = r*cos(i/180*pi);
    % y = 0.05 + r*sin(i/180*pi);
    % z = 0;
    x = N(i,1);
    y = N(i,2);
    z = N(i,3);
    xx = [xx x]; yy = [yy y]; zz = [zz z];
    xd = [x;y;z];
    q = ikine(xd, q);
    
    %robot.plot(q'/180*pi);
    f = robot.fkine(q'/180*pi);
    ff = [ff f(1:3,4)];
    
end

%ang0 = [180, 0, 180];
%ang = [90, 0, 0] + ang0;
%ang = [90, 135, 60] + ang0;
%ang = [ -345.5225 256.8241 597.9878]
%robot.plot(ang/180*pi);

figure
plot3(ff(1,:),ff(2,:), ff(3,:), '*')

Q = [];
for i=1:size(qq,2)
    Q = [Q qq(1,i)-180 qq(2,i) qq(3,i)-180];
end


dlmwrite('out.txt', Q,'delimiter',' ')
