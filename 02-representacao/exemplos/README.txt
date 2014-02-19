Este projeto contém exemplos simples da implementação de grafos usando lista
de adjacências.

Características implementadas
    - adição de vértice e aresta (exemplo 2)
    - atributos de vértices

Características não implementadas
    - remoção de vértices
    - remoção de arestas
    - atributos de arestas
    - testar se dois vértices são adjacentes
    - muitas outras coisas...

Cada exemplo foi implementado em Java e Python. Como o propósito dos exemplos é
dar uma ideia de como a estrutura de um grafo pode ser implementada questões de
encapsulamento foram desconsideradas.

Exemplo 1 (int)
    - os vértices são representados por inteiros de 0 .. |V|-1
    - um grafo é presentado por um arranjo (adj) de arranjos de inteiros
    - cada posição v do arranjo adj contém a lista de adjacência de v
    - uma propriedade p é representada por um arranjo p[0..|V|-1], onde p[v]
      representa o atributo v.p
    - vantagens
        * implementação simples
        * rápido para fazer testes
        * atributos podem ser criados sobre demanda
    - desvantagens
        * baixo nível de abstração
        * o código é mais difícil de ler

Exemplo 2 (class)
    - os vértices são representados pela classe Vertice. A classe Vertice tem
      um campo num (número do vértice), um campo adj (lista de adjacências) e
      todos os outros atributos necessários para resolver o problema em questão
    - um grafo é representado pela classe Grafo. A classe Grafo contém a lista
      de vértices
    - vantagens
        * o código é mais fácil de ler
    - desvantagens
        * implementação mais trabalhosa no início
        * cada atributo necessário deve ser declarado na classe
          Vertice (no caso do Java)
