#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int arrLength, queries;
  cin >> arrLength >> queries;

  int **arr = new int *[arrLength]();

  for (int i = 0; i < arrLength; i++) {
    int size;
    cin >> size;

    int *i_arr = new int[size]();

    for (int j = 0; j < size; j++) {
      cin >> i_arr[j];
    }

    arr[i] = i_arr;
  }

  for (int query = 0; query < queries; query++) {
    int i, j;
    cin >> i >> j;
    cout << arr[i][j] << endl;
  }

  for (int i = 0; i < arrLength; i++) {
    delete[] arr[i];
  }

  delete[] arr;

  return 0;
}
