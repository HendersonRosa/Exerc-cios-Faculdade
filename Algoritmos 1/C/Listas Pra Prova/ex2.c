#include <stdio.h>

int sinalizarUmidade(int u){
  if (u == -1) {
    return 2;  
  }
  if (u < 20 || u > 90){
    return 1;
  }
    return 0;
}
  
int main(){
  int umidade = 0;
  int alertas = 0;
  
  while (umidade != 2) {
    printf("Insira a umidade: ");
    scanf("%d", &umidade);
    int resultado = sinalizarUmidade(umidade);
    umidade = resultado;
    if (resultado == 1) {
      alertas++;
    }
  }
  printf("Houve: %d\n", alertas);
  return 0;
}
