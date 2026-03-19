//enunciado: Uma tela Full HD (1920×1080) precisa exibir 3 bytes por pixel. Calcule e mostre o tamanho total da imagem em megabytes.
#include <stdio.h>
int main() {
  int telah = 1920, telav = 1080;
  int telat = (telah + telav) * 3; //o 3 são os bytes
  int conversão; 
  printf("O tamanho total da imagem em bytes foi de %d\n", telat);
  return 0;
}

