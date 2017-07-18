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
	void findByMask(const std::string x);
	void getAnagrams(std::string word) ;

	~CrosswordSolver() {};
};
