#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string.h>

using namespace std;


int main()
{
	char c = '2';
	char s[10], a[] = "123";
	char* e = new char[5];
	//cin >> e;
	s[0] = '1';
	s[1] = '2';
	s[2] = '3';
	s[3] = '\0';
	strcpy(e, "1234"); //из 2ой в первую
	strcat_s(s, e); // s + e
	//strcmp(s, e); // сравнение
	cout << s << endl << strlen(s) << endl; // длина строки
	cout << strstr(s + 1, e); //поиск по строке
}