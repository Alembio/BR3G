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
	ifstream file("puntos.txt");
	string line;
	int x, y, z;

	if (file.is_open())
	{
		vector<int> arr;

		while (getline(file, line))
		{
			istringstream iss(line);
			int a, b, c;

			if (!(iss >> a >> b >> c)) 
			{ 
				cout << "error" << endl;
				break;
			} 
			else 
			{
				cout << a << " " << b << " " << c << endl;
				arr.push_back(a);
				arr.push_back(b);
				arr.push_back(c);
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
}
