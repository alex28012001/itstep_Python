#include"CrosswordSolver.h"
#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<vector>

	
int main()
{
	setlocale(0, "");
	CrosswordSolver obj;
	obj.getAllWithLen(14);
	obj.getAllWithInit("а");
	

	return 0;
}
