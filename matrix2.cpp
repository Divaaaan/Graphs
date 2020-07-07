#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<iomanip>
#include<cstdio>

using namespace std;

void f(int& e)
{
	e = 186;
}

void transpose(int**& a, int& n, int& m)
{
	int** b = new int* [m];
	for (int i = 0; i < m; i++)
	{
		b[i] = new int[n];
		for (int j = 0; j < n; j++)
			b[i][j] = a[j][i];
	}

	for (int i = 0; i < n; i++)
		delete[] a[i];
	delete[] a;

	int c = n;
	n = m;
	m = c;
	a = b;
}

int main()
{
	int a = 4;
	int& s = a;
	s = 5;
	cout << a;
	f(a);
	int** p;
	int n, m;
	transpose(p, n, m);
	system("pause");
}