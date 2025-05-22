#include <stdio.h>

// exercicio 1

// int main()
// {
//     char nome [90];
//     char endereco[90];
//     char sexo[90];
//     int telefone, idade;

//     printf("Digite o seu nome: ");
//     scanf("%s",&nome);

//     printf("Digite a sua idade: ");
//     scanf("%d",&idade);

//     printf("Digite o seu sexo: ");
//     scanf("%s",&sexo);

//     printf("Digite o seu endereço: ",endereco);
//     scanf("%s",&endereco);

//     printf("Digite o seu telefone: ",telefone);
//     scanf("%d",&telefone);

//     printf("Nome:%s\nIdade:%d\nSexo:%s\nEndereço:%s\nTelefone:%d",nome,idade,sexo,endereco,telefone);

//     return 0;
// }

// exercicio 2
// int main()
// {
//     char nome[200];
//     float nota1, nota2, nota3, nota4;

//     printf("Digite o nome do aluno: ");
//     scanf("%s",&nome);

//     printf("Digite a primeira nota: ");
//     scanf("%f",&nota1);

//     printf("Digite a segunda nota: ");
//     scanf("%f",&nota2);

//     printf("Digite a terceira nota: ");
//     scanf("%f",&nota3);

//     printf("Digite a quarta nota: ");
//     scanf("%f",&nota4);

//     printf("\n\n====================\nNome:%s\nBimestre 1º = %f\nBimestre 2º = %f\nBimestre 3º = %f\nBimestre 4º = %f\n",nome,nota1,nota2,nota3,nota4);

//     return 0;
// }

// exercicio 3
// int main()
// {
//     char nome [200];
//     int titulo, candidato;

//     printf("Digite o nome do eleitor: ");
//     scanf("%s",&nome);

//     printf("Digite o titulo: ");
//     scanf("%d",&titulo);

//     printf("Digite o núemero do candidato: ");
//     scanf("%d",&candidato);

//     printf("\n\n=======Eleição=======\nNome:%s\nTitulo:%d\nCandidato:%d",nome,titulo,candidato);


//     return 0;
// }

// exercicio 4
// int main()
// {
//     char placa[7];
//     char modelo [150];
//     char cor [90];

//     printf("Digite a placa do carro: ");
//     scanf("%7s",&placa);
//     while (getchar() != '\n'); // funçao para limpar o buffer
    
//     printf("Digite o modelo do carro: ");
//     scanf("%s",&modelo);

//     printf("Digite a cor do carro: ");
//     scanf("%s",&cor);

//     printf("====Detran====\nPlaca:%s\nModelo:%s\nCor:%s",placa,modelo,cor);

//     return 0;
// }

// exercicio 5
// int main()
// {
//     char nome[900];
//     char disciplina[900];
//     float nota1, nota2, nota3, media;

//     printf("Digite o nome do aluno: ");
//     scanf("%s",&nome);

//     printf("Digite o nome da disciplina: ");
//     scanf("%s",&disciplina);

//     printf("Digite a primeira nota: ");
//     scanf("%f",&nota1);

//     printf("Digite a segunda nota: ");
//     scanf("%f",&nota2);

//     printf("Digite a terceira nota: ");
//     scanf("%f",&nota3);
//     media = (nota1+nota2+nota3)/3;

//     printf("Nome:%s\nDisciplina:%s\nA média é %f",nome,disciplina,media);

//     return 0;
// }

// exercicio 6
// int main()
// {
//    float base, altura,resultado;

//    printf("Digite a base:");
//    scanf("%f",&base);

//    printf("Digite a altura:");
//    scanf("%f",&altura);

//    resultado = base*altura;

//    printf("a área de retângulo é %f",resultado);

//     return 0;
// }

// exercicio 7
// int main()
// {
//    float base, altura,resultado;

//    printf("Digite a base:");
//    scanf("%f",&base);

//    printf("Digite a altura:");
//    scanf("%f",&altura);

//    resultado = base*altura;

//    printf("a área do triangulo é %f",resultado/2);

//     return 0;
// }

// exercicio 7
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

// exercicio 9
// int main()
// {
//     char nome[900];
//     char disciplina[900];
//     float nota1, nota2, nota3, media;

//     printf("Digite o nome do aluno: ");
//     scanf("%s",&nome);

//     printf("Digite o nome da disciplina: ");
//     scanf("%s",&disciplina);

//     printf("Digite a primeira nota: ");
//     scanf("%f",&nota1);

//     printf("Digite a segunda nota: ");
//     scanf("%f",&nota2);

//     printf("Digite a terceira nota: ");
//     scanf("%f",&nota3);
//     media = (nota1+nota2+nota3)/3;

//     if(media>=6){
//         printf("Nome:%s\nDisciplina:%s\nA média é %f (aprovado)",nome,disciplina,media);
//     } else{
//         printf("Nome:%s\nDisciplina:%s\nA média é %f (reprovado)",nome,disciplina,media);
//     }
//     return 0;
// }

// exercicio 10
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

// exercicio 11
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

// exercicio 12
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

// exercicio 13
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

// exercicio 14
// int main()
// {
//     int numeroConta;
//     float saldo,debito,credito,saldoatual;

//     printf("Digite o número da conta: ");
//     scanf("%d",&numeroConta);

//     printf("Digite o saldo: ");
//     scanf("%f",&saldo);

//     printf("Digite o débito: ");
//     scanf("%f" &debito);

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

// exercicio 15
// int main()
// {
//     char sexo;

//     printf("Qual seu sexo?\nDigite F para feminino e M para masculino: ");
//     scanf(" %c",&sexo);
//     if (sexo == 'F' || sexo == 'f') {
//         printf("Sexo Feminino confirmado.");
//     } else if (sexo == 'M' || sexo == 'm') {
//         printf("Sexo Masculino confirmado.");
//     } else {
//         printf("Sexo inválido");
//     }
//     return 0;
// }

// exercicio 16
// int main()
// {
//     int numero1, maior, menor, i = 1;
//     printf("Digite o primero número: ");
//     scanf("%d",&numero1);
//     maior = menor = numero1;
//     while (i<3){
//         printf("digite o numero %d: ", i+1);
//         scanf("%d", &numero1);

//         if (numero1 >maior){
//             maior = numero1;
//         }
//         if (numero1 <menor){
//             menor = numero1;
//         }
//         i++;
//     }
//     printf("maior: %d\n", maior);
//     printf("menor: %d\n", menor);
//     return 0;
// }