//enunciado: Um sistema de segurança tem sensores de porta, janela e movimento. Se qualquer um for verdadeiro, o alarme dispara. Definir valores lógicos e a expressão para verificar disparo.
#include <stdio.h>
 int main() {
 	int porta = 0 , janela = 0 , movimento = 1;
 	if (porta || janela || movimento == 1) {
 	  printf("alarme dispara\n");
 	} else {
 	  printf("alarme não dispara\n");
 	  }
 	return 0;
 }
