#include <iostream>
#include <stdlib.h>


using namespace std;


void menu()
{
  int start = 0;
  cout << "You can either\n1:Send a file\n2:Recieve a file\n3:look at your transfers\n4:quit" << endl;
  cin >> start;
  switch (start)
    {
      case 1:
      {
        cout <<"Preparing to send a file" << endl;
        break;
      }
      case 2:
      {
          cout << "Listening for a client connection" << endl;
          break;
      }
      case 3:
      {
        cout << "Don't hold your breath I haven't built this part in python yet!" << endl;
        break;
      }
      case 4:
      {
        cout <<"Are you sure you want to close the program?\n1:Quit\n2:Return to menu" << endl;
        int quit = 0;
        cin >> quit;
        if (quit == 1)
        {
          cout << "Quitting..." << endl;
          exit (0);
        }
        else if (quit == 2)
        {
          cout << "Retuning to the menu" << endl;
          menu ();
        }
        else
        {
          cout << "That's not a valid response" << endl;
        }
        break;
      }
      default:
      {
        cout << "Sorry that's not a valid statement please enter a number from the menu" << endl;
        menu();
        break;
      }
    }
}


int main()
{
  cout << "Welcome to FTPy, re-written for c++" << endl;
  menu();
  return 0;
}
