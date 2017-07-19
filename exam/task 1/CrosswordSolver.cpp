#include"CrosswordSolver.h"
#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>

std::string int_to_str(const int x)
{
	char str[256];
	_itoa_s(x, str, 10);
	return str;
}


CrosswordSolver::CrosswordSolver()
{
	setlocale(0, "");
	std::ifstream file("Lopatin_dictionary.txt");
	if (!file.is_open())
		std::cout << "File not found";

	std::string tmp;
	while (file >> tmp)
	{
		temp.push_back(tmp);
	}

	file.close();
}




void CrosswordSolver::getAllWithLen(const int value)
{
	std::string FullName = "SizeWords_" + int_to_str(value) + ".txt";
	std::ofstream file(FullName);
	if (!file.is_open())
		std::cout << "File: " << FullName << " not found\n";


	for (auto it : temp)
	{
		if (it.length() == value)
			file << it << "\n";
	}
	file.close();
}


void CrosswordSolver::getAllWithInit(const std::string letter)
{
	std::string FullName = "FirstLetter_" + letter + ".txt";
	std::ofstream file(FullName);
	if (!file.is_open())
		std::cout << "File: " << FullName << " not found\n";

	for (auto it : temp)
	{
		if (it[0] == letter[0])
			file << it << "\n";
	}
	file.close();
}


void CrosswordSolver::getAnagrams(const std::string word)
{
	setlocale(0, "");
	std::string FullName = "Anagrams_" + word + ".txt";
	std::ofstream file(FullName);
	if (!file.is_open())
		std::cout << "File: " << FullName << " not found\n";

	for (auto it : temp)
	{
		if (it.length() == word.length())
		{
			if (std::is_permutation(it.begin(), it.end(), word.begin()))
				file << it << "\n";
		}
	}
	file.close();
}



void CrosswordSolver::findByMask(std::string x)
{
	//с?д
	
	std::vector<char> alf = { 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я' };
	std::vector<std::string> obj;
	for (auto it : temp)
	{

		if (auto index = x.find('?') == true)
		{
			if (it.length() == x.length())
			{
				for (auto it2 : alf)
				{
					x[index] = it2;
					obj.push_back(x);
					if (x == it)
						std::cout << it << "\n";//std::cout << x <<"\n";		
				}
			}
		}
		for (auto it_obj : obj)
		{
			if(it == it_obj)
				std::cout << it << " ";
		}
	}
	
		
	
	
}
