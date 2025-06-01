#include <stdio.h>

// exercicio 4
int main()
{
    char placa[7];
    char modelo [150];
    char cor [90];

    printf("Digite a placa do carro: ");
    scanf("%7s",&placa);
    while (getchar() != '\n'); // funçao para limpar o buffer
    
    printf("Digite o modelo do carro: ");
    scanf("%s",&modelo);

    printf("Digite a cor do carro: ");
    scanf("%s",&cor);

    printf("====Detran====\nPlaca:%s\nModelo:%s\nCor:%s",placa,modelo,cor);

    return 0;
}