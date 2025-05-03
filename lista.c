// gcc hello.c -o hello.exe
// ./hello.exe
#include <stdio.h>

int main()
{
    // exercicio 1

    char nome [90];
    char endereco[90];
    char sexo[90];
    int telefone, idade;

    printf("Digite o seu nome: ");
    scanf("%s",&nome);

    printf("Digite a sua idade: ");
    scanf("%d",&idade);

    printf("Digite o seu sexo: ");
    scanf("%s",&sexo);

    printf("Digite o seu endereço: ",endereco);
    scanf("%s",&endereco);

    printf("Digite o seu telefone: ",telefone);
    scanf("%d",&telefone);

    printf("Nome:%s\nIdade:%d\nSexo:%s\nEndereço:%s\nTelefone:%d",nome,idade,sexo,endereco,telefone);

    return 0;
}