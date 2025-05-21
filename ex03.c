#include <stdio.h>

// exercicio 3
int main()
{
    char nome [200];
    int titulo, candidato;

    printf("Digite o nome do eleitor: ");
    scanf("%s",&nome);

    printf("Digite o titulo: ");
    scanf("%d",&titulo);

    printf("Digite o núemero do candidato: ");
    scanf("%d",&candidato);

    printf("\n\n=======Eleição=======\nNome:%s\nTitulo:%d\nCandidato:%d",nome,titulo,candidato);


    return 0;
}