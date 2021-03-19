<!-- vim: set spell spelllang=pt_br: -->

# TODO


## Geral

- Adicionar os trabalhos a este repositório

- Escrever um script para gerar o Makefile?

- Juntar coloração de grafos, caixeiro viajante e localização de instalações em um único material sobre problemas NP-difíceis em grafos.

- Usar menos listas (preferir parágrafos sem itemização)

- Atualizar os termos utilizando a tradução da 3a. edição

- Os atributos devem ser escritos em português ou inglês?

- Adicionar links para vídeo aulas

- Colocar exercícios em todos os slides! Em 01 tem bastante, nos outros muito
  poucos.

- Trocar o termo acessível por atingível

- Escrever os códigos usando o pacote clrscode3e (só falta caixeiro viajante)

- Adicionar mais exercícios resolvidos

- Permitir a reordenação dos capítulos

- Adicionar números as figuras (mesmo da original)

- Adicionar versão curta para respostas (a longa é mais didática)

- Juntar em tópico "Busca e Aplicações"?


## 00 - Motivação

- Usar figuras vetorial (tikz)
- Exemplos mais motivantes (alguns onde os vértices e arestas representam coisas reais e outros em que são abstrações)


## 01 - Conceitos e Definições

- Dizer que as definições para orientado e não orientado podem ser um pouco diferentes
- Deixar claro qual é a ideia de cada conceito
- Citar o termo arco?
- Expandir a parte de caminhos e ciclos para incluir passeio, circuito e trilha?
- Simplificar as definições (veja o livro Algorithm Design)
    - Evitar o termo classe de equivalência
- Nó (nodes) usado para vértice por muito autores
- Extremos (ends)
- Cabeça e cauda
- Sumidouros e fontes


## 03 - Busca em Largura

- Falar do conceito de busca de forma abstrata
- Usar o termo árvore BFS como sinônimo de árvore da busca em largura
- Simplificar a análise (uma análise semelhante ao do BFS já aparece no Dijkstra)


## 04 - Busca em Profundidade

- Deixar a parte inicial semelhante ao BFS
- Simplificar a análise?
- Colocar a figura 22-5-c como exemplo para tipos de arestas
- Adicionar Teorema do caminho branco?
- Revisar o uso do termo árvore DFS
- Simplificar atribuição cc (na lista de exercícios)


## 05 - Ordenação Topológica

- Destacar que as abordagens são semelhantes: sumidouros vs fontes.


## 06 - Componentes Fortemente Conexas

- Destacar as aplicações


## 07 - Árvores Geradoras Mínimas

- O termo subconjunto acíclico é estranho
- A análise do Prim está esquisita, tem tempo de insert e create
- Adicionar exercícios
- Mostrar de forma explícita que os algoritmos funcionam


## 08 - Caminhos Mínimos de Única Origem

- Aplicações e problemas reais?


## 09 - Caminhos Mínimos de Todos os Pares

- Aplicações e problemas reais?

- Falar do algoritmos baseado em multiplicação de matrizes (quem é o autor?) e fazer um contraste com o algoritmo de Floyd-Warshall

## 10 - Fluxo em Redes

- Uma demonstração do livro está errada, tem que ver na errata
- Destacar a técnica de projeto utilizada:
  - Greedy techniques iteratively construct an optimal solution by building optimal solutions from smaller problems.
  - Iterative improvement techniques build an optimal solution by iterative refinement of a feasible solution for the complete problem.
- Usar provas usando somatórios implícitos como em
  https://www.youtube.com/watch?v=VYZGlgzr_As


## 11 - Ciclos Eulerianos

- Colocar um exemplo com mais ciclos intermediários
- Mostrar a execução do algoritmo hierholzer-2


