#include<iostream>
#include<math.h>//math header file has been added
using namespace std;
int main ()
{
  int num, d = 0, n, r, p = 0, a = 1;
  char choice;
  cin >> num;//<< has been added
  cin >> choice;//<< has been added
  switch (choice)//switch
  {
    case 'a':// colon and '' has been added 
        n = num;
        while (n != 0)
          {
        	n = n / 10;
        	d++;
          }
        n = num;
        while (n != 0)
          {
        	r = n % 10;
        	a = a * sqrt(r)*d;//== has been replaced by = and sqrt has been added
        	n = n / 10;
           }
        cout << ++a+r+d << "\n";
        break;// break has been added
    case 'p':
        n = num;
        while (n != 0)
          {
        	r = n % 10;
        	p = p * 10 + r;//== has been replaced by = and sqrt has been added
        	n = n / 10;
          }
        cout << p << "\n";
        break;//break has been added
    }
  return(0);
}
