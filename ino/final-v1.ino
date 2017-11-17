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

float arreglo[] = { -250.0, 170, 1, -249.5125, 171.5, 1, -249.025, 173.0, 1, -248.5375, 174.5, 1, -248.05, 176.0, 1, -247.5625, 177.5, 1, -247.075, 179.0, 1, -246.5875, 180.5, 1, -246.1, 182.0, 1, -245.6125, 183.5, 1, -245.125, 185.0, 1, -244.6375, 186.5, 1, -244.15, 188.0, 1, -243.6625, 189.5, 1, -243.175, 191.0, 1, -242.6875, 192.5, 1, -242.2, 194.0, 1, -241.7125, 195.5, 1, -241.225, 197.0, 1, -240.7375, 198.5, 1, -240.25, 200, 1, -239.7625, 198.5, 1, -239.275, 197.0, 1, -238.7875, 195.5, 1, -238.3, 194.0, 1, -237.8125, 192.5, 1, -237.325, 191.0, 1, -236.8375, 189.5, 1, -236.35, 188.0, 1, -235.8625, 186.5, 1, -235.375, 185.0, 1, -234.8875, 183.5, 1, -234.4, 182.0, 1, -233.9125, 180.5, 1, -233.425, 179.0, 1, -232.9375, 177.5, 1, -232.45, 176.0, 1, -231.9625, 174.5, 1, -231.475, 173.0, 1, -230.9875, 171.5, 1, -230.5, 170, 0, -233.425, 173.0, 0, -236.35, 176.0, 0, -239.275, 179.0, 0, -242.2, 182.0, 0, -245.125, 185.0, 0, -245.125, 185, 1, -244.6375, 185.0, 1, -244.15, 185.0, 1, -243.6625, 185.0, 1, -243.175, 185.0, 1, -242.6875, 185.0, 1, -242.2, 185.0, 1, -241.7125, 185.0, 1, -241.225, 185.0, 1, -240.7375, 185.0, 1, -240.25, 185.0, 1, -239.7625, 185.0, 1, -239.275, 185.0, 1, -238.7875, 185.0, 1, -238.3, 185.0, 1, -237.8125, 185.0, 1, -237.325, 185.0, 1, -236.8375, 185.0, 1, -236.35, 185.0, 1, -235.8625, 185.0, 1, -235.375, 185, 0, -234.4, 188.0, 0, -233.425, 191.0, 0, -232.45, 194.0, 0, -231.475, 197.0, 0, -230.5, 200.0, 0, -230.5, 200.0, 0, -229.3, 200.0, 0, -228.1, 200.0, 0, -226.9, 200.0, 0, -225.7, 200.0, 0, -224.5, 200.0, 0, -224.5, 200.0, 0, -230.8, 192.8, 0, -237.1, 185.6, 0, -243.4, 178.4, 0, -249.7, 171.2, 0, -256.0, 164.0, 0, -256.0, 164.0, 0, -254.8, 164.0, 0, -253.6, 164.0, 0, -252.4, 164.0, 0, -251.2, 164.0, 0, -250.0, 164.0, 0 };

int S = sizeof(arreglo) / sizeof(arreglo[0]); //Definir el tamaño del arreglo

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
  for (int i = 0; i < S; i = i + 3)
  {
    x = arreglo[i];
    x = convx(x);
    y = arreglo[i + 1];
    y = convy(y);
    z = arreglo[i + 2];

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
