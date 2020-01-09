#include <iostream>

extern "C"{
	int cprint(char* str)
	{
		printf("%s", str);
		return strlen(str);
	}

	int csum(int* array, int length)
	{
		int sum = 0;
		for(int i = 0; i < length; i++)
		{
			sum += array[i];
		}
		array[length-1] = 0;
		return sum;
	}
}
