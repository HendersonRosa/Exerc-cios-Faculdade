#include<stdio.h>
//adicionei opção de entrada ao exemplo do slide. Quando coloco uma string na primeira entrada ele pula a segunda entrada e da um valor absurdo no final ao invés de dar erro.
int main() {
  int A;
  int B;
  printf("Insira valor do primeiro número: ");
  scanf("%d", &A);
  printf("Insira valor do segundo número: ");
  scanf("%d", &B);
  double media = (A+B) /2.0;
  printf("Os resultados foram: A = %d, B = %d, Média = %.2lf\n", A,B,media);
  return 0;
}
