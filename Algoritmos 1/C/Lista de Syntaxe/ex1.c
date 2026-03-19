#include <stdio.h>
int main() {
  int megabits = 100, tempo = 8;
  int total = (megabits * tempo) * 1000000; //esse número é a conversão de megabits para bits
  printf("O total baixado foi de %d bits\n", total);
  return 0;
}
