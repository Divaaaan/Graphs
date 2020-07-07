#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<functional>

using namespace std;

int** scan1(int* n, int* m)
{
	cin >> *n >> *m;
	int** a = new int* [*n];
	for (int i = 0; i < *n; i++)
	{
		a[i] = new int[*m];
		for (int j = 0; j < *m; j++)
			cin >> a[i][j];
	}
	return a;
}

void scan2(int*** a, int* n, int* m)
{
	cin >> *n >> *m;
	*a = new int* [*n];
	for (int i = 0; i < *n; i++)
	{
		(*a)[i] = new int[*m];
		for (int j = 0; j < *m; j++)
			cin >> (*a)[i][j];
	}
}

void print(int** a, int n, int m)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
			cout << a[i][j] << " ";
		cout << endl;
	}
}

void transpose(int*** a, int* n, int* m)
{
	int** b = new int* [*m];
	for (int i = 0; i < *m; i++)
	{
		b[i] = new int[*n];
		for (int j = 0; j < *n; j++)
			b[i][j] = (*a)[j][i];
	}

	for (int i = 0; i < *n; i++)
		delete[](*a)[i];
	delete[](*a);

	int c = *n;
	*n = *m;
	*m = c;
	*a = b;
}

void func(int a = 1, int b = 5)
{
	cout << a + b;
}

int main()
{
	//func(2);
	int n, m;
	int** p = scan1(&n, &m);
	transpose(&p, &n, &m);
	print(p, n, m);
	system("pause");
}