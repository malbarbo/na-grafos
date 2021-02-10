/**
 * Representa um grafo orientado.
 */
public class Grafo {
    Vertice[] vertices;

    /**
     * Cria um novo grafo com n vértices enumerados de 0 a n - 1.
     */
    public Grafo(int n) {
        vertices = new Vertice[n];
        for (int i = 0; i < n; i++) {
            vertices[i] = new Vertice(i);
        }
    }

    /**
     * Adiciona a aresta (u, v) ao grafo.
     *
     * u e v precisam ser vértices válidos, isto é precisam ser um valor entre
     * 0 e n - 1, onde n é a quantidade de vértices do grafo.
     *
     * Este método não verifica se a aresta (u, v) já existe no grafo.
     */
    public void addAresta(int u, int v) {
        vertices[u].adj.add(vertices[v]);
    }
}
