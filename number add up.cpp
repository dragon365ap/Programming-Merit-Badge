//run in https://cplayground.com/
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