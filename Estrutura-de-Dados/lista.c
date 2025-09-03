#include <stdio.h>
// ex.1
// struct Pessoa {
//     char nome[50];  
//     int idade;
//     float altura;
// };

// int main() {
//     exercicio 1
//     struct Pessoa p;

//     printf("Digite o nome da pessoa: ");
//     scanf(" %[^\n]", p.nome); 
//     printf("Digite a idade: ");
//     scanf("%d", &p.idade);

//     printf("Digite a altura (em metros): ");
//     scanf("%f", &p.altura);

//     printf("\n--- Dados da Pessoa ---\n");
//     printf("Nome: %s\n", p.nome);
//     printf("Idade: %d anos\n", p.idade);
//     printf("Altura: %.2f m\n", p.altura);

//     return 0;
// }

// ex.2
// struct Retangulo {
//     float base;
//     float altura;
// };

// float calcularArea(struct Retangulo r) {
//     return r.base * r.altura;
// }

// int main(){
    
//     struct Retangulo ret;

//     printf("Digite o valor da base do retangulo: ");
//     scanf("%f", &ret.base);

//     printf("Digite o valor da altura do retangulo: ");
//     scanf("%f", &ret.altura);
    
//     float area = calcularArea(ret);
//     printf("\narea do retangulo e: %.2f\n", area);
    
//     return 0;
// }

// ex.3

// struct data {
//     int dia;
//     int mes;
//     int ano;
// };

// int main() {
//     struct data d;

//     printf("Digite o dia: ");
//     scanf("%d", &d.dia);

//     printf("Digite o mes: ");
//     scanf("%d", &d.mes);

//     printf("Digite o ano: ");
//     scanf("%d", &d.ano);

//     printf("\nA data digitada e: %02d/%02d/%04d\n", d.dia, d.mes, d.ano);

//     return 0;
// }

// ex.4

// struct Produto {
//     char nome[50];
//     float preco;
//     int quantidade;
// };

// int main() {
//     struct Produto prod;

//     printf("Digite o nome do produto: ");
//     scanf("%s", prod.nome);

//     printf("Digite o preco do produto: ");
//     scanf("%f", &prod.preco);

//     printf("Digite a quantidade em estoque: ");
//     scanf("%d", &prod.quantidade);

//     float valor_total = prod.preco * prod.quantidade;

//     printf("\n--- Resumo do Produto ---\n");
//     printf("Nome: %s\n", prod.nome);
//     printf("Preco: R$ %.2f\n", prod.preco);
//     printf("Quantidade: %d\n", prod.quantidade);
//     printf("Valor total em estoque: R$ %.2f\n", valor_total);

//     return 0;
// }

// ex.5

struct Funcionario {
    char nome[50];
    float salario_base;
    int tempo_empresa;
};

int main() {
    struct Funcionario func;
    float salario_final;

    printf("Digite o nome do funcionario: ");
    scanf("%s", func.nome);

    printf("Digite o salario base: ");
    scanf("%f", &func.salario_base);

    printf("Digite o tempo de empresa (em anos): ");
    scanf("%d", &func.tempo_empresa);

    if (func.tempo_empresa <= 3) {
        salario_final = func.salario_base * 1.05;
    } else {
        salario_final = func.salario_base * 1.10;
    }

    printf("\n--- Dados do Funcionario ---\n");
    printf("Nome: %s\n", func.nome);
    printf("Salario Base: R$ %.2f\n", func.salario_base);
    printf("Tempo de Empresa: %d anos\n", func.tempo_empresa);
    printf("Salario Final com Bonus: R$ %.2f\n", salario_final);

    return 0;
}