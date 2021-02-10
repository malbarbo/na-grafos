import java.util.List;
import java.util.ArrayList;

/**
 * Um vértice de um grafo.
 */
public class Vertice {
    int num;
    ArrayList<Vertice> adj;
    int grauSaida;

    /**
     * Cria um novo vértice com o número num e uma lista de adjacências vazia.
     *
     * Em geral este construtor não é chamado diretamente mas é chamado pelo
     * construtor da classe Grafo.
     */
    public Vertice(int num) {
        this.num = num;
        this.adj = new ArrayList<Vertice>();
    }

    public String toString() {
        return "Vertice(" + num + ")";
    }
}
