#include <stdio.h>

void contaAtaques(int vidaInicial, int* ataques){
    int valorAtaque = 7;

    while (vidaInicial > 0) {
        vidaInicial = vidaInicial - valorAtaque;
        (*ataques)++;
    }
}

int main(){
    int vidaInicial;
    int ataques = 0;

    printf("Insira a vida inicial: ");
    scanf("%d", &vidaInicial);

    contaAtaques(vidaInicial, &ataques);

    printf("Foram necessarios: %d\n", ataques);

    return 0;
}