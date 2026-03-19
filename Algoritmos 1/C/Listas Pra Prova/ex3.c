#include <stdio.h>
#include <string.h>

void substituiVogais(char origem[], char destino[]) {
    int i = 0;

    while (origem[i] != '\0') {

        if (origem[i] == 'a') {
            destino[i] = '@';
        }
        else if (origem[i] == 'e') {
            destino[i] = '#';
        }
        else if (origem[i] == 'i') {
            destino[i] = '!';
        }
        else if (origem[i] == 'o') {
            destino[i] = '$';
        }
        else if (origem[i] == 'u') {
            destino[i] = '%';
        }
        else {
            destino[i] = origem[i];
        }

        i++;
    }

    destino[i] = '\0';
}

int main() {
    char origem[50];
    char destino[50];

    printf("Digite uma string: ");
    fgets(origem, 50, stdin);

    substituiVogais(origem, destino);

    printf("%s", destino);

    return 0;
}