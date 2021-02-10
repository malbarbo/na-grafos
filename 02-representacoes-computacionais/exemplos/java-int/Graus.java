// Este programa calcula o grau de saída dos vértices de um grafo.
public class Graus {
    public static void main(String[] args) {
        // Grafo da figura 22-2 do livro do Cormen.
        int[][] adj = {
            {1, 3},
            {4},
            {5, 4},
            {1},
            {3},
            {5}
        };

        int[] grauSaida = calculaGrausDeSaida(adj);

        // Lembre-se de usar a opção -ea para o Java executar os asserts.
        assert grauSaida[0] == 2;
        assert grauSaida[1] == 1;
        assert grauSaida[2] == 2;
        assert grauSaida[3] == 1;
        assert grauSaida[4] == 1;
        assert grauSaida[5] == 1;

        System.out.println("Testes realizados com sucesso!");
    }

    /**
     * Calcula o grau de saida de cada vértice do grafo representado por adj.
     */
    public static int[] calculaGrausDeSaida(int[][] adj) {
        int[] grauSaida = new int[adj.length];

        for (int u = 0; u < adj.length; u++) {
            for (int v : adj[u]) {
                grauSaida[u] += 1;
            }
        }

        return grauSaida;
    }
}
