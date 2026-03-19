#include <stdio.h>
int main() {
  float f = 0.0;
  float *p = &f;
  printf("%f\n",(*p));
  (*p) = 50.0;
  printf("%f\n",(*p));
  return 0;

}
