public class Grafo {
    Vertice[] vertices;

    public Grafo(int n) {
        vertices = new Vertice[n];
        for (int i = 0; i < n; i++) {
            vertices[i] = new Vertice(i);
        }
    }

    public void addAresta(int u, int v) {
        vertices[u].adj.add(vertices[v]);
    }
}
