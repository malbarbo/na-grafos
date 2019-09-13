// Programa para calcular o Número de Erdős
//
// Este programa foi feito como exemplo para uma aula inicial de Algoritmos em
// Grafos. O programa não usa um algoritmo eficiente, mas sim um algoritmo
// ingênuo que é simples e direto.

#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Representa que uma pessoa ainda não tem número
#define NENHUM -1

struct Pessoa {
    char* nome;
    int num;
};

struct Par {
    char* nome1;
    char* nome2;
};

// Criar um par entre nome1 e nome2
struct Par par(char* nome1, char* nome2);

// Criar uma pessoa com o nome especificado e número NENHUM
struct Pessoa pessoa(char* nome);

// Encontra uma pessoa com o nome especificado
struct Pessoa* encontra_pessoa(struct Pessoa* pessoas, size_t n, char* nome);

// Encontra o "número de Erdős" de cada pessoa no arranjo pessoas usando o
// arranjo pares como lista de cooperação. Uma pessoa (representado o Erdős) do
// arranjo de pessoas deve ter o número 0.
void enumera(struct Par* pares, size_t m, struct Pessoa* pessoas, size_t n);

// Lê os pares de nomes a partir de arquivo e enumera as pessoas a partir da
// pessoa como nome inicio
void run(char* arquivo, char* inicio);

// Função que testa enumera com um exemplo
void test();

int main(int argc, char* argv[])
{
    // Se nenhum argumento for especificado, executa os testes;
    // Senão é necessário dois argumentos, o nome do arquivo com os pares e o
    // nome da pessoal inicial.
    if (argc == 1) {
        test();
    } else if (argc == 3) {
        run(argv[1], argv[2]);
    } else {
        printf("Número de argumentos inválido!\n");
        printf("  use %s arquivo-de-pares nome-pessoa-inicial\n", argv[0]);
        return 1;
    }
}

void enumera(struct Par* pares, size_t m, struct Pessoa* pessoas, size_t n)
{
    for (int num = 0; (size_t)num < n; num += 1) {
        // Encontra pessoas que não tem número e estão ligadas a pessoas com número num,
        // e atribuí número num + 1 a elas.
        for (size_t i = 0; i < m; i += 1) {
            struct Pessoa* p1 = encontra_pessoa(pessoas, n, pares[i].nome1);
            struct Pessoa* p2 = encontra_pessoa(pessoas, n, pares[i].nome2);
            if ((p1->num == num) && (p2->num == NENHUM)) {
                p2->num = num + 1;
            } else if ((p2->num == num) && (p1->num == NENHUM)) {
                p1->num = num + 1;
            }
        }
    }
}

void test()
{
    size_t N = 14;
    size_t M = 19;
    struct Par pares[] = {
        par("babai", "imrich"),
        par("babai", "lovasz"),
        par("bondy", "murty"),
        par("chvatal", "bondy"),
        par("chvatal", "hell"),
        par("deng", "papadimitriou"),
        par("erdos", "babai"),
        par("erdos", "chvatal"),
        par("erdos", "harary"),
        par("erdos", "hell"),
        par("erdos", "lovasz"),
        par("harary", "hell"),
        par("harary", "white"),
        par("hell", "bondy"),
        par("hell", "deng"),
        par("hell", "watkins"),
        par("imrich", "watkins"),
        par("papadimitriou", "gates"),
        par("white", "bondy"),
    };

    struct Pessoa pessoas[] = {
        pessoa("babai"),
        pessoa("bondy"),
        pessoa("chvatal"),
        pessoa("deng"),
        pessoa("erdos"),
        pessoa("gates"),
        pessoa("harary"),
        pessoa("hell"),
        pessoa("imrich"),
        pessoa("lovasz"),
        pessoa("murty"),
        pessoa("papadimitriou"),
        pessoa("watkins"),
        pessoa("white"),
    };

    encontra_pessoa(pessoas, N, "erdos")->num = 0;

    enumera(pares, M, pessoas, N);

#define ASSERT_NUM(nome, n) assert(encontra_pessoa(pessoas, N, nome)->num == n)

    ASSERT_NUM("babai", 1);
    ASSERT_NUM("bondy", 2);
    ASSERT_NUM("chvatal", 1);
    ASSERT_NUM("deng", 2);
    ASSERT_NUM("erdos", 0);
    ASSERT_NUM("gates", 4);
    ASSERT_NUM("harary", 1);
    ASSERT_NUM("hell", 1);
    ASSERT_NUM("imrich", 2);
    ASSERT_NUM("lovasz", 1);
    ASSERT_NUM("murty", 3);
    ASSERT_NUM("papadimitriou", 3);
    ASSERT_NUM("watkins", 2);
    ASSERT_NUM("white", 2);

    printf("Testes executados com sucesso.\n");
}

struct Pessoa* encontra_pessoa(struct Pessoa* pessoas, size_t n, char* nome)
{
    for (size_t i = 0; i < n; i += 1) {
        if (strcmp(pessoas[i].nome, nome) == 0) {
            return &pessoas[i];
        }
    }
    fprintf(stderr, "Pessoa não encontrada: %s\n", nome);
    exit(1);
}

struct Par par(char* nome1, char* nome2)
{
    return (struct Par) { nome1, nome2 };
}

struct Pessoa pessoa(char* nome)
{
    return (struct Pessoa) { nome, NENHUM };
}

int compara_pessoa(const struct Pessoa* p1, const struct Pessoa* p2)
{
    return strcmp(p1->nome, p2->nome);
}

/////////////////////////////////////
// Extra: leitura a partir de arquivo

// Lê uma sequência de pares a partir de arquivo
struct Par* ler_pares(char* arquivo);

// Verifica se o arranjo pessoa contém uma pessoa com o nome especificado.
bool contem_pessoa(struct Pessoa* pessoas, size_t n, char* nome);

// Compara duas pessoas pelo nome
int compara_pessoa(const struct Pessoa* p1, const struct Pessoa* p2);

void run(char* arquivo, char* inicial)
{
    struct Par* pares = ler_pares(arquivo);

    // encontra a quantidade de pares
    size_t m = 0;
    while (pares[m].nome1 != NULL) {
        m += 1;
    }

    // um limite fácil de usar para o número de pessoas é m + 1
    struct Pessoa* pessoas = malloc(sizeof(struct Pessoa) * (m + 1));

    // cria a lista de pessoas
    size_t n = 0;
    for (size_t i = 0; i < m; i += 1) {
        if (!contem_pessoa(pessoas, n, pares[i].nome1)) {
            pessoas[n] = pessoa(pares[i].nome1);
            n += 1;
        }
        if (!contem_pessoa(pessoas, n, pares[i].nome2)) {
            pessoas[n] = pessoa(pares[i].nome2);
            n += 1;
        }
    }

    // ordena as pesssoas pelo nome
    qsort(pessoas, n, sizeof(struct Pessoa), (int (*)(const void*, const void*))compara_pessoa);

    // inicia o número da pessoa inicial para 0
    encontra_pessoa(pessoas, n, inicial)->num = 0;

    enumera(pares, m, pessoas, n);

    // exibe os números
    for (size_t i = 0; i < n; i += 1) {
        printf("%s = %d\n", pessoas[i].nome, pessoas[i].num);
    }

    free(pares);
    free(pessoas);
}

struct Par* ler_pares(char* arquivo)
{
    FILE* f = fopen(arquivo, "r");
    if (f == NULL) {
        perror("run");
        exit(1);
    }

    // aloca um espaço inicial para 10 pares
    int n = 10;
    int i = 0;
    struct Par* pares = malloc(sizeof(struct Par) * n);
    char nome1[31];
    char nome2[31];
    int items;
    while ((items = fscanf(f, "%30s%30s", nome1, nome2)) != EOF) {
        if (items != 2) {
            fprintf(stderr, "Não foi possível ler o par %d\n", i + 1);
            exit(1);
        }
        if (i + 1 >= n) {
            // não tem mais espaço, tenta realocar o dobro
            n *= 2;
            struct Par* p = realloc(pares, sizeof(struct Par) * n);
            if (p == NULL) {
                perror("run");
                free(pares);
                exit(1);
            }
            pares = p;
        }
        pares[i] = par(strdup(nome1), strdup(nome2));
        i += 1;
    }

    if (ferror(f) != 0) {
        perror("run");
        free(pares);
        exit(1);
    }

    fclose(f);
    pares[i].nome1 = NULL;
    pares[i].nome2 = NULL;

    return pares;
}

bool contem_pessoa(struct Pessoa* pessoas, size_t n, char* nome)
{
    for (size_t i = 0; i < n; i += 1) {
        if (strcmp(pessoas[i].nome, nome) == 0) {
            return true;
        }
    }
    return false;
}
