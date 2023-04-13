---
# vim: set spell spelllang=pt_br:
title: 10 - Fluxo em redes
---

#. (CLRS3 26.1-7) Suponha que, além das capacidades da arestas, uma rede tenha capacidade nos vértices. Isto é, cada vértices tem um limite $l(v)$ de quanto fluxo pode passar através de $v$. Mostre como transformar uma rede $G = (V, E)$ com capacidades nos vértices em um rede $G' = (V', E')$ sem capacidades nos vértices, de maneira que o fluxo máximo em $G'$ tenha o mesmo valor que o fluxo máximo em $G$. Quantos vértices e arestas $G'$ têm?

#. (CLRS3 26.2-2) Na figura abaixo, qual é o fluxo através do corte $(\{ s, v_2, v_4 \}, \{ v_1, v_3, t \})$? Qual é a capacidade desse corte?

    \includegraphics[trim=1850pt 180pt 0pt 0pt,clip,scale=0.1]{imagens/Fig-26-1.pdf}

#. (CLRS3 26.2-3) Mostre a execução do algoritmo de Edmonds-Karp para a rede da figura abaixo

    \includegraphics[trim=0pt 180pt 1750pt 0pt,clip,scale=0.1]{imagens/Fig-26-1.pdf}

#. (CLRS3 26.2-4) Na figura abaixo, qual é o corte mínimo correspondente ao fluxo máximo?

    \includegraphics[trim=1850pt 700pt 0pt 700pt,clip,scale=0.1]{imagens/Fig-26-6-R.pdf}

#. (CLRS3 26.2-8) Suponha que redefinamos a rede residual para não permitir arestas que entrem em $s$, Argumente que o procedimento \proc{Ford-Fulkerson} ainda computa um fluxo máximo corretamente.

#. (CLRS3 26.2-9) Suponha que $f$ e $f'$ sejam fluxos em uma rede $G$ e que computemos o fluxo $f \uparrow f'$. O fluxo aumentado satisfaz a propriedade de conversação de fluxo? E a restrição de capacidade?

#. Para cada afirmação a seguir diga se ela é verdadeira ou falsa. Se ela for verdadeira justifique com uma argumentação lógica (você pode utilizar os teoremas vistos nas aulas na argumentação). Se ela for falsa, justifique mostrando e explicando um contra exemplo.

    a) Seja $G = (V, E)$ uma rede de fluxo onde $c(u, v) \ge 0$ é a capacidade entre cada par de vértices de $G$ e $f: V \times V \rightarrow R$ um fluxo de valor máximo em $G$. Se $(u, v)$ é uma aresta de $G$ tal que $c(u,v) = f(u,v)$, então se diminuirmos a capacidade $c(u, v)$, o valor do fluxo máximo de $G$ diminui.

#. Em uma rede, uma aresta azul é aquela que quando a sua capacidade diminui o valor do fluxo máximo da rede diminui. Dado uma rede com um fluxo máximo, como podemos encontrar todas as arestas azuis sem executar o algoritmo de \proc{Ford-Fulkerson}? Não é necessário mostrar o pseudocódigo, apenas descrever o algoritmo em alto nível, argumentar porque ele funciona e fazer a análise do tempo de execução. Note que o algoritmo de \proc{Ford-Fulkerson} não pode ser usado como um todo, mas as ideias que formam o algoritmo podem ser usadas.

# Referências

-   [CLRS3] - Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 26.
