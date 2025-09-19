
// Inclui a biblioteca de entrada e saída padrão (para funções como printf e scanf)
#include <stdio.h> 
// Inclui a biblioteca padrão (para funções como malloc de alocação de memória)
#include <stdlib.h> 

// Define a estrutura de um "Nó" (um elemento) da lista.
typedef struct No { 
    int valor;           // Cada nó guarda um número inteiro.
    struct No *prox;     // E tem um ponteiro (uma "flecha") para o próximo nó da lista.
} No; 

// Função para inserir um novo número (x) na lista de forma ordenada.
// Ela recebe a lista atual e o número a ser inserido, e retorna o início da lista atualizada.
No* inserirOrdenado(No *lista, int x) { 
    // Aloca (cria) espaço na memória para um novo nó.
    No *novo = (No*) malloc(sizeof(No)); 
    
    // Coloca o número 'x' dentro do novo nó que foi criado.
    novo->valor = x; 
    
    // Por enquanto, a "flecha" do novo nó não aponta para ninguém.
    novo->prox = NULL; 
    
    // Verifica duas condições:
    // 1. A lista está vazia? (lista == NULL)
    // 2. O número 'x' que queremos inserir é menor que o primeiro valor da lista?
    // Se uma dessas for verdade, o novo nó será o primeiro da lista.
    if (lista == NULL || x < lista->valor) { 
        // A "flecha" do novo nó passa a apontar para o antigo início da lista.
        novo->prox = lista; 
        // Retorna o novo nó como o novo início da lista.
        return novo; 
    } 
 
    // Se o código chegou aqui, significa que o novo nó não é o primeiro.
    // Precisamos andar na lista para achar o lugar certo.
    // 'atual' é um ponteiro temporário que começa no início da lista.
    No *atual = lista; 
    
    // Loop para percorrer a lista:
    // Ele continua enquanto não chegamos no fim (atual->prox != NULL) E
    // o valor do PRÓXIMO nó ainda for menor que o nosso número 'x'.
    while (atual->prox != NULL && atual->prox->valor < x) { 
        // Anda para o próximo nó da lista.
        atual = atual->prox; 
    } 
    
    // Quando o loop para, encontramos o lugar certo para inserir.
    // A "flecha" do novo nó aponta para quem 'atual' estava apontando.
    novo->prox = atual->prox; 
    
    // E a "flecha" do 'atual' passa a apontar para o nosso novo nó.
    atual->prox = novo; 
    
    // Retorna o início da lista (que não mudou, pois não inserimos no começo).
    return lista; 
} 

// Função para imprimir todos os valores da lista na tela.
void imprimirLista(No *lista) { 
    // Enquanto não chegarmos ao fim da lista (enquanto a lista não for NULL)...
    while (lista != NULL) { 
        // Imprime o valor do nó atual, seguido de uma seta.
        printf("%d -> ", lista->valor); 
        // Avança para o próximo nó.
        lista = lista->prox; 
    } 
    // Quando o loop acabar, imprime "NULL" para indicar o fim da lista.
    printf("NULL\n"); 
} 

// Função principal, onde o programa começa a rodar.
int main() { 
    // Cria um ponteiro para a lista e o inicializa como NULL (lista vazia).
    No *lista = NULL; 
    
    // Declara duas variáveis inteiras: 'n' para a quantidade de elementos e 'x' para o valor de cada um.
    int n, x; 
    
    // Pede ao usuário para dizer quantos elementos ele quer inserir.
    printf("Quantos elementos deseja inserir? "); 
    
    // Lê o número que o usuário digitou e guarda na variável 'n'.
    scanf("%d", &n); 
    
    // Loop que vai se repetir 'n' vezes.
    for (int i = 0; i < n; i++) { 
        // Pede para o usuário digitar o valor.
        printf("Digite o valor %d: ", i+1); 
        // Lê o valor digitado e guarda na variável 'x'.
        scanf("%d", &x); 
        // Chama a função para inserir o valor 'x' na lista de forma ordenada.
        // O início da lista é atualizado caso a inserção seja no começo.
        lista = inserirOrdenado(lista, x); 
    } 
 
    // Imprime uma mensagem na tela.
    printf("Lista ordenada: "); 
    
    // Chama a função para mostrar a lista completa e ordenada.
    imprimirLista(lista); 
    
    // Retorna 0, indicando que o programa terminou com sucesso.
    return 0; 
}