public class Graus {
    public static void main(String[] args) {
        Grafo g = new Grafo(6);
        g.addAresta(0, 1);
        g.addAresta(0, 3);
        g.addAresta(1, 4);
        g.addAresta(2, 4);
        g.addAresta(2, 5);
        g.addAresta(3, 1);
        g.addAresta(4, 3);
        g.addAresta(5, 5);

        calcularGrausDeSaida(g);
        mostrarGrausDeSaida(g);
    }

    public static void calcularGrausDeSaida(Grafo g) {
       for (Vertice v : g.vertices) {
           v.grauSaida = 0;
       }

       for (Vertice v : g.vertices) {
           for (Vertice u : v.adj) {
               v.grauSaida += 1;
           }
       }
    }

    public static void mostrarGrausDeSaida(Grafo g) {
       for (Vertice v : g.vertices) {
           System.out.printf("%s.grauSaida = %d\n", v, v.grauSaida);
       }
    }
}
