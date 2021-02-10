// Este programa calcula os graus de saída dos vértices um grafo.
public class Graus {

    public static void main(String[] args) {
        // Grafo da figura 22-2 do livro do Cormen.
        Grafo g = new Grafo(6);
        g.addAresta(0, 1);
        g.addAresta(0, 3);
        g.addAresta(1, 4);
        g.addAresta(2, 4);
        g.addAresta(2, 5);
        g.addAresta(3, 1);
        g.addAresta(4, 3);
        g.addAresta(5, 5);

        calculaGrausDeSaida(g);

        // Lembre-se de usar a opção -ea para o Java executar os asserts.
        assert g.vertices[0].grauSaida == 2;
        assert g.vertices[1].grauSaida == 1;
        assert g.vertices[2].grauSaida == 2;
        assert g.vertices[3].grauSaida == 1;
        assert g.vertices[4].grauSaida == 1;
        assert g.vertices[5].grauSaida == 1;

        System.out.println("Testes executados com sucesso!");
    }

    /**
     * Calcula os grau de saída de cada vértice de g.
     */
    public static void calculaGrausDeSaida(Grafo g) {
       for (Vertice v : g.vertices) {
           v.grauSaida = 0;
       }

       for (Vertice v : g.vertices) {
           for (Vertice u : v.adj) {
               v.grauSaida += 1;
           }
       }
    }
}
