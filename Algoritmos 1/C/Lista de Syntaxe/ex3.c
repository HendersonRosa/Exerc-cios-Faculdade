#include <stdio.h>
int main() {
  double distancia;
  double tempo;
  printf("Insira os km percorrido pelo carro: ");
  scanf("%lf", &distancia);
  printf("Insira o tempo (horas) de viagem: ");
  scanf("%lf", &tempo);
  double vm = distancia / tempo;
  printf("A velocidade média do carro foi de %lf km/h\n", vm); 
  return 0;
}
