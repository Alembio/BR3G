#include <Servo.h>

Servo myservo1;
Servo myservo2;
Servo myservo3;
int flag;

void setup() {

  //Vincular servos a los pines del arduino
  myservo1.attach(9); 
  myservo2.attach(10);
  myservo3.attach(11);

  Serial.begin(9600); //Iniciar la comuncación serial

  //Posiciones iniciales
  myservo1.write(90); 
  myservo2.write(0);
  myservo3.write(0);

  //Esperar 3 segundos para asegurar que todo este bien
  Serial.print("Starting up... Please wait");
  Serial.print("\n");
  delay(3000);

  Serial.print("\n");
  Serial.print("DONE");
  Serial.print("\n");
  delay(100);
  Serial.print("Press 1 to run the code"); //instrucción
  delay(300);

}



void loop() {
  
  if(Serial.available()){ //Si hay comunicación serial
    
    flag = Serial.read(); //Restricción
}

if(flag > 0) //Restricción
{ 
  delay(300);
  Serial.print("Hello Again World"); //huevada
  Serial.print("\n");

  //Motor3
  Serial.print("Motor3: ");
  for (int pos = 0; pos <= 130; ++pos) { //Mover motor 3 de 0 a 130

    myservo3.write(pos);
    delay(30);
    Serial.print(pos);
    Serial.print("\n");
  }
  
  
  //Motor2
  Serial.print("Motor2: ");
  for (int pos = 0; pos <= 110; ++pos) { //Mover motor 2 de 0 a 110

    myservo2.write(pos);
    delay(30);
    Serial.print(pos);
    Serial.print("\n");
  }

  //Motor1
  Serial.print("Motor1: ");
  for (int pos = 90; pos <= 180; ++pos) { //Mover motor 1 de 90 a 180 y de regreso a 90

    myservo1.write(pos);
    delay(30);
    Serial.print(pos);
    Serial.print("\n");
  }
  for (int pos = 180; pos >= 0; --pos) {

    myservo1.write(pos);
    delay(30);
    Serial.print(pos);
    Serial.print("\n");
  }
  for (int pos = 0; pos <= 90; ++pos) {

    myservo1.write(pos);
    delay(30);
    Serial.print(pos);
    Serial.print("\n");
  }

  delay(300);
  
  //Motor2
  Serial.print("Motor2: ");
  for (int pos = 110; pos >= 0; --pos) { //Regresar el motor 2 a 0

    myservo2.write(pos);
    delay(30);
    Serial.print(pos);
    Serial.print("\n");
  }
  
  //Motor3
  Serial.print("Motor3: ");
  for (int pos = 130; pos >= 0; --pos) { //Regresar el motor 3 a 0

    myservo3.write(pos);
    delay(30);
    Serial.print(pos);
    Serial.print("\n");
  }
  
  }

  flag = 0; //Restricción
 }
