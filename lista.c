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

// exercicio 8
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

// exercicio 17
// int main() {
//     float salarioAtual, aumento, valorAumento, novoSalario;

//     printf("Digite o salario atual do funcionário: ");
//     scanf("%f", &salarioAtual);

//     if (salarioAtual <= 280.00) {
//         aumento = 0.20; 
//     } else if (salarioAtual <= 700.00) {
//         aumento = 0.15; 
//     } else if (salarioAtual <= 1500.00) {
//         aumento = 0.10; 
//     } else {
//         aumento = 0.05; 
//     }
    
//     valorAumento = salarioAtual * aumento;
//     novoSalario = salarioAtual + valorAumento;

//     printf("\n--- Reajuste Salarial ---\n");
//     printf("Salario antes do reajuste: R$ %.2f\n", salarioAtual);
//     printf("Percentual de aumento aplicado: %.0f%%\n", aumento * 100);
//     printf("Valor do aumento: R$ %.2f\n", valorAumento);
//     printf("Novo salario, apos o aumento: R$ %.2f\n", novoSalario);

//     return 0;
// }

// exercicio 18 (pedi ajuda pro GPT🙈)
// int main() {
//     float valorHora, horasTrabalhadas;
//     float bruto, descontoIR = 0.0, descontoINSS, fgts, totalDesconto, salarioLiquido;

//     printf("Digite o valor da hora de trabalho:  ");
//     scanf("%f", &valorHora);
//     printf("Digite a quantidade de horas trabalhadas no mes: ");
//     scanf("%f", &horasTrabalhadas);

//     bruto = valorHora * horasTrabalhadas;

//     if (bruto <= 900.00) {
//         descontoIR = 0.0;
//     } else if (bruto <= 1500.00) {
//         descontoIR = bruto * 0.05; 
//     } else if (bruto <= 2500.00) {
//         descontoIR = bruto * 0.10; 
//     } else { 
//         descontoIR = bruto * 0.20;
//     }

//     descontoINSS = bruto * 0.10;
//     fgts = bruto * 0.11;
//     totalDesconto = descontoIR + descontoINSS;
//     salarioLiquido = bruto - totalDesconto;
    
//     printf("\n"); 
//     printf("Salario Bruto: (%.0f * %.0f): R$ %.2f\n", valorHora, horasTrabalhadas, bruto);
//     printf("(-) IR ");

//     if (bruto <= 900.00) {
//         printf("(Isento)");
//     } else if (bruto <= 1500.00) {
//         printf("(5%%)"); 
//     } else if (bruto <= 2500.00) {
//         printf("(10%%)");
//     } else {
//         printf("(20%%)");
//     }
//     printf(": R$ %.2f\n", descontoIR);
//     printf("(-) INSS (10%%): R$ %.2f\n", descontoINSS);
//     printf("FGTS (11%%): R$ %.2f\n", fgts);
//     printf("Total de descontos: R$ %.2f\n", totalDesconto);
//     printf("Salario Liquido: R$ %.2f\n", salarioLiquido);

//     return 0;
// }

// exercicio 19
// int main()
// {
//     float lado1, lado2, lado3;
//     printf("Digite o primeiro lado: ");
//     scanf("%f",&lado1);
//     printf("Digite o segundo lado: ");
//     scanf("%f",&lado2);
//     printf("Digite o terceiro lado: ");
//     scanf("%f",&lado3);

//     if (lado1 == lado2 && lado2 == lado3 && lado1 == lado3){
//         printf("o triangulo é equilátero");
//     } else if (lado1 != lado2 && lado2 != lado3 && lado1 != lado3)
//     {
//         printf("o triangulo é escaleno");
//     } else{
//         printf("o triangulo é isósceles");
//     }
    
//     return 0;
// }

// // exercicio 20
// int main()
// {
//     int matricula, feminino = 0, masculino = 0, masculinoBom = 0, porcentagemMasculino;
//     int status;
//     int altura;
//     char sexo;
//     int alunos = 0;

//     while (alunos < 3) 
//     {
//         printf("Digite a matrícula do aluno(a): ");
//         scanf("%d", &matricula);

//         printf("Digite a altura do aluno(a): ");
//         scanf("%f", &altura);

//         printf("Digite o status físico do aluno(a) (1-bom, 2-regular, 3-ruim): ");
//         scanf("%d", &status);

//         while (getchar() != '\n'); 

//         printf("Digite o sexo do aluno(a) (M/F): ");
//         scanf("%c", &sexo);

//         if ((sexo == 'F' || sexo == 'f') && altura > 170)
//         {
//             feminino++;
//         }

//         if (sexo == 'M' || sexo == 'm')
//         {
//             masculino++;
//             if (status == 1)
//             {
//                 masculinoBom++;
//             }
//         }

//         alunos++;
//     }
//     printf("\nalunas com altura superior a 1.70m: %d\n", feminino);
//     printf("alunos do sexo masculino com status 'bom': %d\n", masculinoBom);


//     return 0;
// }


// exercicio 21
// int main()
// {
//     float salarioFixo, vendas, salarioFinal, comissao;

//     printf("Digite o valor do salário do funcionário: ");
//     scanf("%f",&salarioFixo);
    	
//     printf("Digite o valor das vendas: ");
//     scanf("%f",&vendas);

//     comissao = vendas*0.04;
    
//     salarioFinal = salarioFixo + comissao;

//     printf("o salário final é %f\ntotal de comissão %f",salarioFinal,comissao);  

//     return 0;
// }

// // exercicio 22
// int main() {

//     float precoProduto, desconto;

//     printf("Digite o valor do produto: ");
//     scanf("%f",&precoProduto);

//     desconto = precoProduto - (precoProduto*0.10);
//     printf("novo preço é: %.2f",desconto);
//     return 0;
// }

// exercicio 23
// int main() {

//     int frangos;
//     float calculo;

//     printf("Digite a quantidade de frangos: ");
//     scanf("%d",&frangos);

//     calculo = frangos*(4+7);

//     printf("O calculo de todos os gasto é %f",calculo);
//     return 0;

// }

// exercicio 24
// int main() {

//     int qntSanduiches;
//     float queijo, presunto, carne;

//     printf("Digite a quantidade de sanduiches: ");
//     scanf("%d", &qntSanduiches);

//     queijo = (qntSanduiches * 2 * 50) / 1000.0;
//     presunto = (qntSanduiches * 50) / 1000.0;
//     carne = (qntSanduiches * 100) / 1000.0;

//     printf("Para %d sanduiches, será necessario:\n", qntSanduiches);
//     printf("Queijo: %.2f kg\n", queijo);
//     printf("Presunto: %.2f kg\n", presunto);
//     printf("Carne: %.2f kg\n", carne);
//     return 0;
// }

// exercicio 25
// int main() {
//     int p,m,g;
//     float valor;

//     printf("Digite a quantidade de Camisas p: ");
//     scanf("%d", &p);
//     printf("Digite a quantidade de Camisas m: ");
//     scanf("%d", &m);
//     printf("Digite a quantidade de Camisas g: ");
//     scanf("%d", &g);

//     p = p*10;
//     m = m*12;
//     g = g*15;

//     valor = p+m+g;
//     printf("o valor total é: R$%.2f", valor);
//     return 0;
// }
// exercicio 26
// int main() {
//     float aquisicao, venda;

//     printf("Digite o preço da aquisição: ");
//     scanf("%f",&aquisicao);

//     if(aquisicao<50.00){
//         venda = aquisicao*1.45;
//     }else
//     {
//         venda = aquisicao*1.30;

//     }
//     printf("O valor de venda do produto será: R$ %.2f\n", venda);
//     return 0;
// }
// exercicio 27
// int main() {
//     int i, matricula, statusFisico, totalFeminino = 0;
//     int totalMasculino = 0, maculinoBom = 0;
//     char sexo;
//     float altura;

//     for (i = 0; i < 50; i++) {
//         printf("Digite a matrícula, sexo (M/F), altura (cm) e status físico (1-bom, 2-regular, 3-ruim):\n");
//         scanf("%d %c %f %d", &matricula, &sexo, &altura, &statusFisico);
        
//         if (sexo == 'F' && altura > 170) {
//             totalFeminino++;
//         }
//         if (sexo == 'M') {
//             totalMasculino++;
//             if (statusFisico == 1) {
//                 maculinoBom++;
//             }
//         }
//     }

//     float percentualBom = (totalMasculino > 0) ? ((maculinoBom * 100.0) / totalMasculino) : 0;

//     printf("Quantidade de alunas com altura superior a 170cm: %d\n", totalFeminino);
//     printf("Percentual de alunos do sexo masculino com status físico bom: %.2f%%\n", percentualBom);
//     return 0;
// }
// exercicio 28
// int main() {
//     int num1, num2;
//     float num3;

//     printf("Digite dois números inteiros e um número real:\n");
//     scanf("%d %d %f", &num1, &num2, &num3);

//     float resultado1 = (2 * num1) * (num2 / 2.0);
//     float resultado2 = (3 * num1) + num3;
//     float resultado3 = num3 * num3 * num3;

//     printf("O produto do dobro do primeiro com metade do segundo: %.2f\n", resultado1);
//     printf("A soma do triplo do primeiro com o terceiro: %.2f\n", resultado2);
//     printf("O terceiro elevado ao cubo: %.2f\n", resultado3);
//     return 0;
// }
// exercicio 29
// int main() {
//     float altura, ideal;
//     char sexo;
    
//     printf("Digite a altura e F ou M para o genero: \n");
//     scanf("%f %c", &altura, &sexo);

//     if (sexo == 'F' || sexo == 'f') {
//         ideal = (62.1 * altura) - 44.7;
//         printf("O peso ideal é: %.2f kg\n", ideal);
//     } else if (sexo == 'M' || sexo == 'm') {
//         ideal = (72.7 * altura) - 58;
//         printf("O peso ideal é: %.2f kg\n", ideal);
//     } else {
//         printf("Entrada inválida! Digite a altura corretamente e 'F' ou 'M' para o gênero.\n");
//     }
    
//     return 0;
// }
// exercicio 30
// int main() {
//     float pesoPeixe, calculo;

//     printf("Digite o peso do peixe: Kg");
//     scanf("%f",&pesoPeixe);

//     if (pesoPeixe < 50)
//     {
//         printf("não paga multa");
//     } else {
//         calculo = (pesoPeixe-50)*4.00 ;
//         printf("a multa é de R$%.2f",calculo);
//     }
    
   
//     return 0;
// }
// exercicio 31
// int main() {
//     char turno;

//     printf("Digite M-matutino, V-vespertino ou N-noturno: ");
//     scanf("%c",&turno);

//     if (turno == 'm' || turno == 'M')
//     {
//         printf("Bom dia!");
//     } else if (turno == 'v' || turno == 'V')
//     {
//         printf("Boa tarde!");
//     } else if (turno == 'N' || turno == 'n')
//     {
//         printf("Boa noite!");
//     }else{
//         printf("Digite apenas N, V ou M");
//     }
    

//     return 0;
// }
// exercicio 32
// int main() {
//     int saque, notas100, notas50, notas10, notas5, notas1;

//     printf("Digite o valor do saque (mínimo R$10 e máximo R$600): ");
//     scanf("%d", &saque);

    
//     if (saque < 10 || saque > 600) {
//         printf("Valor inválido! O saque deve ser entre R$10 e R$600.\n");
//         return 1; 
//     }

    
//     notas100 = saque / 100;
//     saque %= 100;
    
//     notas50 = saque / 50;
//     saque %= 50;
    
//     notas10 = saque / 10;
//     saque %= 10;
    
//     notas5 = saque / 5;
//     saque %= 5;
    
//     notas1 = saque;
    
//     printf("Notas fornecidas:\n");
//     if (notas100 > 0) printf("%d nota(s) de R$100\n", notas100);
//     if (notas50 > 0) printf("%d nota(s) de R$50\n", notas50);
//     if (notas10 > 0) printf("%d nota(s) de R$10\n", notas10);
//     if (notas5 > 0) printf("%d nota(s) de R$5\n", notas5);
//     if (notas1 > 0) printf("%d nota(s) de R$1\n", notas1);

//     return 0;
// }
// exercicio 33
// int main() {
//     float num1, num2, resultado;
//     int operacao;

//     printf("Digite dois números: ");
//     scanf("%f %f", &num1, &num2);

//     printf("Escolha a operação:\n");
//     printf("1 - Soma\n");
//     printf("2 - Subtração\n");
//     printf("3 - Multiplicação\n");
//     printf("4 - Divisão\n");
//     scanf("%d", &operacao);

//     if (operacao == 1) {
//         resultado = num1 + num2;
//     } else if (operacao == 2) {
//         resultado = num1 - num2;
//     } else if (operacao == 3) {
//         resultado = num1 * num2;
//     } else if (operacao == 4) {
//         if (num2 != 0) {
//             resultado = num1 / num2;
//         } else {
//             printf("Erro: divisão por zero!\n");
//             return 1;
//         }
//     } else {
//         printf("Operação inválida!\n");
//         return 1;
//     }

//     printf("Resultado: %.2f\n", resultado);

//     if ((int)resultado % 2 == 0) {
//         printf("O resultado é par.\n");
//     } else {
//         printf("O resultado é ímpar.\n");
//     }

//     if (resultado > 0) {
//         printf("O resultado é positivo.\n");
//     } else if (resultado < 0) {
//         printf("O resultado é negativo.\n");
//     } else {
//         printf("O resultado é zero.\n");
//     }

//     if (resultado == (int)resultado) {
//         printf("O resultado é inteiro.\n");
//     } else {
//         printf("O resultado é decimal.\n");
//     }

//     return 0;
// }

