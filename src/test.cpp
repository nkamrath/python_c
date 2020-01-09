#include <iostream>

extern "C"{
	int cprint(char* str)
	{
		printf("%s", str);
		return strlen(str);
	}
}

// g++ -c -fPIC foo.cpp -o foo.o
// g++ -shared -Wl,-soname,libfoo.so -o libfoo.so  foo.o