#include <stdio.h>

void update(int *a, int *b) {
  int sum = *a + *b;
  int subtraction = *a - *b;
  subtraction = subtraction < 0 ? -subtraction : subtraction;

  *a = sum;
  *b = subtraction;
}

int main() {
  int a, b;
  int *pa = &a, *pb = &b;

  scanf("%d %d", &a, &b);
  update(pa, pb);
  printf("%d\n%d", a, b);

  return 0;
}
