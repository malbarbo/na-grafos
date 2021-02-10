// Este programa calcula o grau de entrada e o grau de saída para cada vértice
// de um grafo orientado.

#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

// Representação dos grafos
//
// Os grafos são representados por lista de adjacências. Cada lista de adjacência
// é um arranjo terminado pelo valor -1.
//
// Os vértices de um grafo com n vértices são representados pelos números
// 0, 1, ..., n - 1.
//
// Os atributos (inclusive a lista de adjacentes) dos vértices são armazenados
// em arranjos indexados pelos vértices. Por exemplo, para um vértice v
// e um atributo atrib, o elemento atrib[v] representa aquele atributo para
// o vértice v.


// Calcula o grau de saída de dos vértices 0, 1, ...,  n-1 do grafo adj.
//
// O resultado é devolvido em um novo arranjo que deve ser desalocado
// posteriormente. Se não for possível alocar o arranjo, a função devolve
// NULL.
int* graus_de_saida(int* adj[], size_t n)
{
    int* graus = calloc(n, sizeof(int));

    if (graus == NULL) {
        return NULL;
    }

    for (size_t u = 0; u < n; u += 1) {
        // Veja outra forma de fazer este for na função graus_de_entrada
        for (int* v = adj[u]; *v != -1; v++) {
            graus[u] += 1;
        }
    }

    return graus;
}


// Calcula o grau de entrada de dos vértices 0, 1, ...,  n-1 do grafo adj.
//
// O resultado é devolvido em um novo arranjo que deve ser desalocado
// posteriormente. Se não for possível alocar o arranjo, a função devolve
// NULL.
int* graus_de_entrada(int* adj[], size_t n)
{
    int* graus = calloc(n, sizeof(int));

    if (graus == NULL) {
        return NULL;
    }

    for (size_t u = 0; u < n; u += 1) {
        // Veja outra forma de fazer este for na função graus_de_saida
        for (size_t i = 0; adj[u][i] != -1; i++) {
            int v = adj[u][i];
            graus[v] += 1;
        }
    }

    return graus;
}


int main()
{
    // Grafo orientado da figura 22-2 do livro do Cormen.
    // Usamos -1 para denotar o fim da lista de adjacência.
    int* adj[6] = {
        (int[]) { 1, 3, -1 },
        (int[]) { 4, -1 },
        (int[]) { 5, 4, -1 },
        (int[]) { 1, -1 },
        (int[]) { 3, -1 },
        (int[]) { 5, -1 },
    };
    int N = 6;

    // Testa a função graus_de_saida

    int* gsaida = graus_de_saida(adj, N);

    assert(gsaida != NULL);
    assert(gsaida[0] == 2);
    assert(gsaida[1] == 1);
    assert(gsaida[2] == 2);
    assert(gsaida[3] == 1);
    assert(gsaida[4] == 1);
    assert(gsaida[5] == 1);

    free(gsaida);

    printf("Função graus_saida: ok\n");


    // Testa a função graus_de_entrada

    int* gentrada = graus_de_entrada(adj, N);

    assert(gentrada != NULL);
    assert(gentrada[0] == 0);
    assert(gentrada[1] == 2);
    assert(gentrada[2] == 0);
    assert(gentrada[3] == 2);
    assert(gentrada[4] == 2);
    assert(gentrada[5] == 2);

    free(gentrada);

    printf("Função graus_entrada: ok\n");
}
