#include <stdio.h>
int main() {
  int a;
  int b;
  int *p = &a;
  int *p2 = &b;
  printf("%d\n%d\n",(*p),(*p2));
  return 0;

}
