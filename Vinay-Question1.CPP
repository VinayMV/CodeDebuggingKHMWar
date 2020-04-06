#include<iostream>//iostream
#include<string.h>// string
using namespace std;
int getLIndex(char[],char);//prototype has been added
int getFIndex(char[],char);
int main()
{
	char str[100];
	char ch; 
	int Lindex,Findex; 
	cin>>str;//semi colon added
	cin>>ch;
	Lindex = getLIndex(str,ch);
	Findex = getFIndex(str,ch);
	if(Lindex!=-1)
		cout<<Findex<<endl<<Lindex;
	else
		cout<<"NOT FOUND"<<endl;
	return 0;	
}
int getFIndex(char string[],char c)//square brackets
{
	int size = strlen(string);//strlen has been added
	int i=0;
	while(i<size)
	{
		
		if(string[i]==c){
		    return i;
		   break;
		}	
		i++; 
	}
	
}
int getLIndex(char string[], char c)//square brakcet and data type
{
	int size = strlen(string);
	int i=size; 
	while( i>=0)//semicolon has been removed
{		
		if(string[i]==c)
		{
		    return i;
            break;
		}
	i--;
}
		
}
