#include <stdio.h>
int main() {
  int x = 0;
  int *p = &x;
  printf("%d\n",*p);
  (*p) = 50;
  printf("%d\n",(*p));
  return 0;

}
