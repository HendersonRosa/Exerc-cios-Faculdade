#include <stdio.h>
//código tem dois problemas q vi, quando tu coloca uma das entradas como uma string ele da um resultado absurdo e o segundo problema é q quando a entrada é negativa ela passa (deve dar de resolver usando if, mas vou deixar pra dps)
int main() {
  int megabits;
  int tempo;
  printf("insira o total de megabits: ");
  scanf("%d", &megabits);
  printf("insira o tempo de download: ");
  scanf("%d", &tempo);
  int total = (megabits * tempo) * 1000000; //esse número é a conversão de megabits para bits*/
  printf("O total baixado foi de %d bits \n", total);
  return 0;
}
