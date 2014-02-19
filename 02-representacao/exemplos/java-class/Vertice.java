import java.util.List;
import java.util.LinkedList;

public class Vertice {
    int num;
    List<Vertice> adj;
    int grauSaida;

    public Vertice(int num) {
        this.num = num;
        this.adj = new LinkedList<Vertice>();
    }

    public String toString() {
        return "Vertice(" + num + ")";
    }
}
