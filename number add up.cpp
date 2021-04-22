//run in https://cplayground.com/
//this program takes in a number and adds up all the numbers before (from 1) with the current number. For example, if you put the number 4, the program would calculate 1+2+3+4 and return 10.

#include <iostream>
using namespace std;

int main() {
  int x;
  int y = 0;
  cout << "Type a number: "; // Type a number and press enter
  cin >> x; // Get user input from the keyboard
  for (int i = 1; i <= x; i++) {
      y = y + i;
  }
  cout << "Your number is: " << y;
  return 0;
}
