
#include<iostream>
#include<math.h>
# define M_PI           3.14159265358979323846  //pi 
using namespace std;

float x;
float y;
float z;

int L1, L2;
float ang1, ang2, ang3;

const int S = 303;

float redondear(float posf) //función para redondear
{
	return floor(posf + 0.5);
}

float angulo1(float x, float y) //Función para calcular el ángulo del primer motor
{
	float ang;
	ang = atan2(y, x);
	ang = ang * 180 / M_PI;
	//ang = redondear(ang);
	return ang;
}

float angulo2(float x, float y, float z, float L1, float L2) //Función para hallar el ángulo del segundo motor
{
	float ang;
	float alpha;
	float beta;
	alpha = (L1*L1 + x*x + y*y + z*z - L2*L2) / (2 * L1 * sqrt(x*x + y*y + z*z));
	alpha = acos(alpha);
	alpha = alpha * 180.0 / M_PI;

	beta = z / (sqrt(x*x + y*y));
	beta = atan(beta);
	beta = beta * 180.0 / M_PI;

	ang = alpha + beta;
	//ang = redondear(ang);
	return ang;
}

float angulo3(float x, float y, float z, float L1, float L2) //Función para hallar el ángulo del tercer motor
{
	float w;
	w = (L1*L1 + L2*L2 - (x*x + y*y + z*z)) / (2 * L1 * L2);
	float ang;
	ang = acos(w);
	ang = ang * 180.0 / M_PI;
	//ang = redondear(ang);
	return ang;
}

float convx(float x)
{
	x = x / 400 * 20;
	return x;
}

float convy(float y)
{
	y = 20 * (y) / 300;
	return y;
}

int main()
{
	float arreglo[S];
	float c = -5;

	for (int i = 0; i < 101; i ++)
	{
		
		arreglo[i*3] = c;
		float v = 13 + sqrt(25 - (c*c));
		arreglo[i * 3 + 1] = v;
		arreglo[i * 3 + 2] = 1;
		c = c + 0.1;
	}

	L1 = 13;
	L2 = 13;

	
	for (int i = 0; i < S; i = i + 3)
	{
		x = arreglo[i];
		//x = convx(x);
		y = arreglo[i + 1];
		//y = convy(y);
		z = arreglo[i + 2];

		/*
		cout << x << "  " << y << "  " << z << endl;
		cout << endl;
		*/
		
		
		//cout << i + 1 << endl;
		ang1 = angulo1(x, y);
		//cout << "El angulo 1 es: " << ang1 << endl;

		ang2 = angulo2(x, y, z, L1, L2);
		//cout << "El angulo 2 es: " << ang2 << endl;

		ang3 = angulo3(x, y, z, L1, L2);
		//cout << "El angulo 3 es: " << ang3 << endl;

		//cout << endl;

		cout << ang1 << " " << ang2 << " " << ang3 << endl;
		
	}


}
