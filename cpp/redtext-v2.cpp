#include<iostream>
#include<math.h>
#include <fstream>
#include <sstream>
#include<string>
#include<vector>
# define M_PI           3.14159265358979323846  // pi
using namespace std;

int main()
{
	string puntos;
	float j = 0;
	int flag = 1;
	vector<float> arr;
	float x, y, z;

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

			cout << x << " " << y << " " << z << endl;
		}

	}
	else
	{
		cout << "No se encontro archivo" << endl;
	}

}
