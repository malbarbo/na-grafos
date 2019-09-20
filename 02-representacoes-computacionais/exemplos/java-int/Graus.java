public class Graus {
    public static void main(String[] args) {
        int[][] adj = {
            {1, 3},
            {4},
            {5, 4},
            {1},
            {3},
            {5}
        };

        int[] grauSaida = calcularGrausDeSaida(adj);
        mostrarGrausDeSaida(grauSaida);
    }

    public static int[] calcularGrausDeSaida(int[][] adj) {
        int[] grauSaida = new int[adj.length];

        for (int v = 0; v < adj.length; v++) {
            for (int u : adj[v]) {
                grauSaida[v] += 1;
            }
        }
        return grauSaida;
    }

    public static void mostrarGrausDeSaida(int[] grauSaida) {
        for (int v = 0; v < grauSaida.length; v++) {
            System.out.printf("Vertice(%d).grauSaida = %d\n", v, grauSaida[v]);
        }
    }
}
