#include"CrosswordSolver.h"
int main()
{
	setlocale(0, "");
	CrosswordSolver obj;
	obj.getAllWithLen(14);
	obj.getAllWithInit("х");
	obj.getAnagrams("апельсин");

	return 0;
}
