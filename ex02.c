#include <stdio.h>

// exercicio 2
int main()
{
    char nome[200];
    float nota1, nota2, nota3, nota4;

    printf("Digite o nome do aluno: ");
    scanf("%s",&nome);

    printf("Digite a primeira nota: ");
    scanf("%f",&nota1);

    printf("Digite a segunda nota: ");
    scanf("%f",&nota2);

    printf("Digite a terceira nota: ");
    scanf("%f",&nota3);

    printf("Digite a quarta nota: ");
    scanf("%f",&nota4);

    printf("\n\n====================\nNome:%s\nBimestre 1º = %f\nBimestre 2º = %f\nBimestre 3º = %f\nBimestre 4º = %f\n",nome,nota1,nota2,nota3,nota4);

    return 0;
}