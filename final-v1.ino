#include<Servo.h>
#include<math.h>

Servo myServo1;
Servo myServo2;
Servo myServo3;

int L1 = 13;
int L2 = 13;
float ang1, ang2, ang3;
float x, y, z;
int flag;

float redondear(float posf) //función para redondear
{
  return floor(posf + 0.5);
}

float angulo1(float x, float y) //Función para calcular el ángulo del primer motor
{
  float ang;
  ang = atan2(y, x);
  ang = ang * 180 / PI;
  ang = redondear(ang);
  return ang;
}

float angulo2(float x, float y, float z, float L1, float L2) //Función para hallar el ángulo del segundo motor
{
  float ang;
  float alpha;
  float beta;
  alpha = (L1*L1 + x*x + y*y + z*z - L2*L2) / (2 * L1 * sqrt(x*x + y*y + z*z));
  alpha = acos(alpha);
  alpha = alpha * 180.0 / PI;

  beta = z / (sqrt(x*x + y*y));
  beta = atan(beta);
  beta = beta * 180.0 / PI;

  ang = alpha + beta;
  ang = redondear(ang);
  return ang;
}

float angulo3(float x, float y, float z, float L1, float L2) //Función para hallar el ángulo del tercer motor
{
  float w;
  w = (L1*L1 + L2*L2 - (x*x + y*y + z*z)) / (2 * L1 * L2);
  float ang;
  ang = acos(w);
  ang = ang * 180.0 / PI;
  ang = redondear(ang);
  return ang;
}

float convx(float x) //Converitr pixeles a cm
{
  x = x / 400 * 20;
  return x;
}

float convy(float y) //Converitr pixeles a cm
{
  y = 20 * (y) / 300;
  return y;
}

void setup() {

  Serial.begin(9600); //Iniciar comunicación serial

  //Vincular los motores a los pines 9, 10 y 11 del arduino
  myServo1.attach(9);
  myServo2.attach(10);
  myServo3.attach(11);

  //Definir posiciones iniciales
  myServo1.write(0);
  myServo2.write(0);
  myServo3.write(0);

  Serial.println("Escribe 1 para correr el codigo");
}

void loop() {

if(Serial.available()){ //Si hay comunicación serial

    flag = Serial.read(); //Restricción
}

if(flag > 0)//Restricción
{
  for (int i = 0; i < pi; i = i + 0.1)
  {
    //dibuja un cardioid
    theta = i;
    r= 2 + 3*cos(theta);
    x = r*cos(theta);
    y = r*sen(theta) + 10
    z = 0;

    ang1 = angulo1(x, y);
    ang2 = angulo2(x, y, z, L1, L2);
    ang3 = angulo3(x, y, z, L1, L2);

    //Imprimir datos
    Serial.print(ang1);
    Serial.print(" ");
    Serial.print(ang2);
    Serial.print(" ");
    Serial.print(ang3);
    Serial.print("\n");
  }

  flag = 0; //Restricción
 }
}
