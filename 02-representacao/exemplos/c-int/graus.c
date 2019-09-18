#include <assert.h>
#include <stdlib.h>

int* graus_de_saida(int* adj[], size_t n)
{
    int* graus = calloc(n, sizeof(int));

    for (size_t u = 0; u < n; u += 1) {
        for (size_t i = 0; adj[u][i] != -1; i++) {
            graus[u] += 1;
        }
    }

    return graus;
}

int* graus_de_entrada(int* adj[], size_t n)
{
    int* graus = calloc(n, sizeof(int));

    for (size_t u = 0; u < n; u += 1) {
        for (size_t i = 0; adj[u][i] != -1; i++) {
            int v = adj[u][i];
            graus[v] += 1;
        }
    }

    return graus;
}

int main()
{
    // Grafo orientado da figura 22-2
    // Usamos -1 para denotar o fim da lista de adjacência
    int* adj[6] = {
        (int[]) { 1, 3, -1 },
        (int[]) { 4, -1 },
        (int[]) { 5, 4, -1 },
        (int[]) { 1, -1 },
        (int[]) { 3, -1 },
        (int[]) { 5, -1 },
    };
    const int N = 6;

    // Testa a função graus_de_saida

    int* gsaida = graus_de_saida(adj, N);

    assert(gsaida[0] == 2);
    assert(gsaida[1] == 1);
    assert(gsaida[2] == 2);
    assert(gsaida[3] == 1);
    assert(gsaida[4] == 1);
    assert(gsaida[5] == 1);

    free(gsaida);


    // Testa a função graus_de_entrada

    int* gentrada = graus_de_entrada(adj, N);

    assert(gentrada[0] == 0);
    assert(gentrada[1] == 2);
    assert(gentrada[2] == 0);
    assert(gentrada[3] == 2);
    assert(gentrada[4] == 2);
    assert(gentrada[5] == 2);

    free(gentrada);
}
