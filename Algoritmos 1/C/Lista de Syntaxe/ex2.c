#include <stdio.h>
int main() {
  int distancia;
  int tempo;
  printf("Insira os km percorrido pelo carro: ");
  scanf("%d", &distancia);
  printf("Insira o tempo (horas) de viagem: ");
  scanf("%d", &tempo);
  int vm = distancia / tempo;
  printf("A velocidade média do carro foi de %d km/h\n", vm); 
  return 0;
}
