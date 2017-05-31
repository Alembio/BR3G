#include<iostream>
#include<math.h>
#include <fstream>
#include <sstream>
#include<string>
#include<vector>
# define M_PI           3.14159265358979323846  // pi
using namespace std;

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
	int L1, L2;
	float ang1, ang2, ang3;

	string puntos;
	float j = 0;
	int flag = 1;
	vector<float> arr;
	float x, y, z;
	

	L1 = 13;
	L2 = 13;

	ifstream file("puntos.txt");
	if (file.is_open())
	{
		while (getline(file, puntos))
		{
			istringstream iss(puntos);

			while (flag != 0)
			{
				if (iss >> j)
				{
					arr.push_back(j);
				}
				else {
					flag = 0;
				}
				++j;
			}
		}

		for (unsigned int i = 0; i < arr.size(); i = i + 3)
		{
			x = arr[i];
			y = arr[i + 1];
			z = arr[i + 2];

			x = convx(x);
			y = convy(y);

			ang1 = angulo1(x, y);
			ang2 = angulo2(x, y, z, L1, L2);
			ang3 = angulo3(x, y, z, L1, L2);

			cout << ang1 << " " << ang2 << " " << ang3 << endl;
		}

	}
	else
	{
		cout << "No se encontro archivo" << endl;
	}

}
