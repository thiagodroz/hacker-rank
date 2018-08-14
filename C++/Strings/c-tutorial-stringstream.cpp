#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
  vector<int> result;
  int value;
  char ch;
  stringstream ss(str);

  while (ss >> value) {
    result.push_back(value);
    ss >> ch;
  }

  return result;
}

int main() {
  string str;
  cin >> str;
  vector<int> integers = parseInts(str);
  for (int i = 0; i < integers.size(); i++) {
    cout << integers[i] << "\n";
  }

  return 0;
}
