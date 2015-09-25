#include <stdio.h>
#include <conio.h>
#include <oct.h>

struct Tickers {
int ts;
char* symbol; 
char** field; //This will store field names in each test case
int* values; //This will store the field values
};

int sum(int start, int end, char* symbol, char* field);

int product(int start, int end, char* symbol, char* field1, char* field2);

int max(int start, int end, char* symbol, char* field, int num);

int delta(char* symbol, char* field, int num);
