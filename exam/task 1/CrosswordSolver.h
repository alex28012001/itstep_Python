#pragma once
#include<string>
#include<fstream>
#include<vector>
class CrosswordSolver
{
	std::vector<std::string> temp;

public:
	CrosswordSolver();
	void getAllWithLen(const int value);
	void getAllWithInit(const std::string letter);
	void getAnagrams(const std::string word) ;

	~CrosswordSolver() {};
};
