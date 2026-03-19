#include <stdio.h>

void ajustarTemperatura(int *t){
  if (*t <= -99){
      *t = -100;
    }
  else {
    if (*t <= 0){
      *t = 0;
    }
    if (*t >= 60){
      *t = 60;
    }
  }
}
  
int main(){
  int temperatura = 0;
  printf("Insira a temperatura: ");
  scanf("%d", &temperatura);
  ajustarTemperatura(&temperatura);
  if (temperatura > -99) {
    printf("A temperatura foi de: %d\n",temperatura);
    }
  else {
    printf("Temperatura Inválida \n");
  }
  return 0;
}
