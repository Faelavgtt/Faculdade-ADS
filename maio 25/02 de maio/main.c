// gcc hello.c -o hello.exe
// ./hello.exe

#include <stdio.h>
#include <locale.h>

int main()
{
    setlocale(LC_ALL, "Portuguese");
    // ## exercicio 1 aula
    // int ano;
    // printf("Digite o ano: ");
    // scanf("%d",&ano);
    
    // if((ano%4==0&&ano%100!=0)||ano%400==0){
    //     printf("o ano %d é bissexto", ano);
    // }
    // else{
    //     printf("o ano de %d não é bissexto", ano);
    // }

    // ## exercicio 2 aula

    // float salariofixo, salariofinal, valor_vendas, valor_comissao;
    // int comissao;

    // printf("qual o valor do salário fixo: ");
    // scanf("%f",&salariofixo);
    // printf("qual o valor total das vendas do funcionário: ");
    // scanf("%f",&valor_vendas);
    // printf("qual a porcentagem de comissão dos funcionários: ");
    // scanf("%d",&comissao);

    // valor_comissao = valor_vendas*comissao;
    // salariofinal = salariofixo + valor_comissao;
    // printf("o valor é %f ",salariofinal);

    // ## exercicio 3 aula

    float produto, valorFinal;

    printf("Digite o valor do produto: ");
    scanf("%f",&produto);

    valorFinal = produto-(produto*0.10);
    printf("o valor final do produto com o desconto e %f",valorFinal);



    return 0;
}