#include <stdio.h>

// exercicio 1
// int main()
// {
//     int numero;
    
//     printf("Digite um número: ");
//     scanf("%d",&numero);

//     if (numero<10){
//         printf("o %d é menor que 10",numero);
//     } else if (numero>10){
//         printf("o %d é maior que 10",numero);
//     } else if (numero == 10){
//         printf("o %d é igual a 10",numero);
//     }

//     return 0;
// }

// exercicio 2
// int main()
// {
//     int idade;
    
//     printf("Digite a sua idade: ");
//     scanf("%d",&idade);

//     if (idade <=2){
//         printf("%d é bebê",idade);
//     } else if (idade >=3 && idade <=11){
//         printf("%d é Criança",idade);
//     } else if (idade >=12 && idade <=21){
//         printf("%d é jovem",idade);
//     } else if (idade >=22 && idade <=64){
//         printf("%d é Adulto",idade);
//     } else if (idade >=65 && idade <=100){
//         printf("%d é Idoso",idade);
//     } else if (idade >=101){
//         printf("%d é muito velhinho",idade);
//     } 

//     return 0;
// }

// exercicio 3
// int main()
// {
//     float base, altura,resultado;

//    printf("Digite a base:");
//    scanf("%f",&base);

//    printf("Digite a altura:");
//    scanf("%f",&altura);

//    resultado = base*altura;

//    printf("a área do triângulo é %f",resultado/2);

//     return 0;
// }

// exercicio 4
// int main()
// {
//    float km, litro,resultado;

//    printf("Digite a distância em km:");
//    scanf("%f",&km);

//    printf("Digite o consumo por litro");
//    scanf("%f",&litro);

//    resultado = (km/litro)*6.29;

//    printf("o Custo total é %f",resultado);

//     return 0;
// }

// exercicio 5
// int main()
// {
//     int numero;

//     printf("Digite o número:");
//     scanf("%d",&numero);
    
//     if (numero >0) {
//         printf("o %d é positivo",numero);
//     } else {
//         printf("o %d é negativo",numero);
//     }
    
//     return 0;
// }

// exercicio 6
// int main()
// {
//     int numero;
//     printf("Digite o número:");
//     scanf("%d",&numero);
    
//     if (numero%2==0) {
//         printf("o %d é par",numero);
//     } else {
//         printf("o %d é impar",numero);
//     }
    
//     return 0;
// }

// exercicio 7
// int main()
// {
//     float base, altura,resultado;

//    printf("Digite a base:");
//    scanf("%f",&base);

//    printf("Digite a altura:");
//    scanf("%f",&altura);

//    resultado = base*altura;

//    printf("a área do retangulo é %f",resultado);
    
//     return 0;
// }

// exercicio 8
// int main()
// {
//     int numeroConta;
//     float saldo,debito,credito,saldoatual;

//     printf("Digite o número da conta: ");
//     scanf("%d",&numeroConta);

//     printf("Digite o saldo: ");
//     scanf("%f",&saldo);

//     printf("Digite o débito: ");
//     scanf("%f",&debito);

//     printf("Digite o crédito: ");
//     scanf("%f",&credito);

//     saldoatual = saldo - debito + credito;

//     printf("Saldo atual da conta %d: %f\n",numeroConta,saldoatual);

//     if (saldoatual>=0) {
//         printf("Saldo Positivo\n");
//     } else {
//         printf("Saldo Negativo\n");
//     }

   
//     return 0;
// }