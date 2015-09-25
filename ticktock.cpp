#include <stdio.h>
#include <iostream.h>
#include <conio.h>
#include <oct.h>

struct Tickers {
	int ts;
	string symbol; 
	string[100] fields; //This will store field names in each test case
	int[100] values; //This will store the field values
};
Tickers* t;
int cases = 0;

int sum(int start, int end, string symbol, string field);

int product(int start, int end, string symbol, string field1, string field2);

int max(int start, int end, string symbol, string field, int num);

int delta(string symbol, string field, int num);

int main(){
	string inp;
	ifstream inputFile;
	inputFile.open("filename");
	//Replace suitable input method here
	cin >> cases;
	inp+=getline(cin,inp);
	
	int ind = 0;
	string temp = inp;
	while(true){
		if(temp.find('\n') > -1){cases++; temp = temp.substr(temp.find('\n')+1);}
		else{break;}
	}
	t = malloc(cases*sizeof(Tickers));
	caseNum = 0;
	//Allocate the cases to individual Tickers structs in array
	for(int i = 0; i < inp.size(); i++){
		if(inp.at(i)=='\n'){caseNum++; ind=0; continue;}
		if(inp.at(i)==' '){
			if(ind==0){t[caseNum].ts = 0;}
			else{
				if(ind==1){t[caseNum].symbol = "";}
				else{
					if(ind%2 == 0){t[caseNum].field[] = "";}
					else{t[caseNum].field[] = "";}
				}
			}
		}
	}
	return 0;
}

int sum(int start, int end, string symbol, string field){
	bool running = false;
    int sum = 0;
	for(int i = 0; i < cases; i++){
		if(!running){
			if(t[i].ts == start){	running = true;}
		}
		if(t[i].ts > end){running = false; break;}
		if(running){
			if(t[i].symbol == symbol){
				//Add the values of fields here by finding index of field in t[i].fields and value of field in t[i].values at the index
                 sum+=t[i].values[t[i].field.find(field)];
			}
		}
	}
}