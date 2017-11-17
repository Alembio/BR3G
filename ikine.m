function [qout, i, f] = ikine(xd, qinit)

dt = 0.01;
k = 10;
epsilon = 0.001;
max_iter = 1000; % Máximo número de iteraciones

h  = 0.07;
l1 = 0.115;
l4 = 0.16;
d  = 0.025;

q = qinit/180*pi;

for i=1:max_iter
    q1=q(1); q2=q(2); q3=q(3);
    
    J = [ d*cos(q1) - l1*cos(q2)*sin(q1) - l4*cos(q2)*cos(q3)*sin(q1) - l4*sin(q1)*sin(q2)*sin(q3), -cos(q1)*(l1*sin(q2) + l4*sin(q2 - q3)), l4*sin(q2 - q3)*cos(q1);
          d*sin(q1) + l1*cos(q1)*cos(q2) + l4*cos(q1)*cos(q2)*cos(q3) + l4*cos(q1)*sin(q2)*sin(q3), -sin(q1)*(l1*sin(q2) + l4*sin(q2 - q3)), l4*sin(q2 - q3)*sin(q1);
          0,            l1*cos(q2) + l4*cos(q2 - q3),        -l4*cos(q2 - q3)];
    x = d*sin(q1) + l1*cos(q1)*cos(q2) + l4*cos(q1)*cos(q2)*cos(q3) + l4*cos(q1)*sin(q2)*sin(q3);
    y = l1*cos(q2)*sin(q1) - d*cos(q1) + l4*cos(q2)*cos(q3)*sin(q1) + l4*sin(q1)*sin(q2)*sin(q3);
    z = h + l1*sin(q2) + l4*sin(q2 - q3);
    f = [x; y; z];
    e = f-xd;
    q = q - dt*k*inv(J)*e;
    
    if (norm(e)<epsilon)
        break;
    end
    if (i== (max_iter-1))
        q=qinit/180*pi;
    end
end

qout = q/pi*180;



