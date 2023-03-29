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


# Referências

-   [CLRS3] - Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 26.
