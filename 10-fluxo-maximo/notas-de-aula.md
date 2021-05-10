---
# vim: set spell spelllang=pt_br:
title: Fluxo máximo
---


## Problema

A empresa de discos de _hockey_ Lucky Puck tem uma fábrica em Vancouver e um armazém em Winnipeg. \pause A Luck Puck aluga espaços em caminhões para levar os discos da fábrica até o armazém. \pause As rotas e capacidades dos caminhões são pré determinadas e não podem ser alteradas pela Luck Puck. \pause Sabendo que todos os dias estão disponíveis os mesmos caminhões com as mesmas rotas e capacidades, a Luck Puck quer determinar a quantidade diária máxima de caixas de disco que podem ser enviadas para o armazém em Winnipeg. \pause

Como resolver esse problema?


## Modelagem

Vamos modelar o problema com um grafo \pause

- Cada cidade é representada por um vértice; \pause
- Dois vértices são especiais, um representa onde os discos são produzidas e outro onde os discos são armazenados; \pause
- Uma aresta entre as cidades $u$ e $v$ com uma capacidade $c(u, v)$ representa a capacidade de todos os caminhões que podem ser contratados para levar os discos de $u$ para $v$.


## Exemplo

\includegraphics[trim=0pt 0pt 1650pt 0pt,clip,height=3.5cm]{imagens/Fig-26-1.pdf}

\pause

\small

Como seria uma resposta para o problema, apenas o número máximo de caixas? \pause Não, também precisamos determinar a quantidade de caixas que vai ser transportada entre cada par de cidades. \pause


A solução precisa respeitar alguma regra? \pause Sim! \pause \vspace{-1em}

- A capacidade de cada aresta; \pause
- A mesma quantidade de caixas que chega em uma cidade também deve sair da cidade (exceto para a origem e destino).


## Exemplo de solução

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 100pt 1650pt 0pt,clip,width=6cm]{imagens/Fig-26-1.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1850pt 650pt 0pt 650pt,clip,width=5.6cm]{imagens/Fig-26-6-R.pdf}
</div>
</div>

\pause

Observações \pause

- A quantidade transportada de uma cidade para a outra respeita a capacidade; \pause
- Para os vértices $v_1, v_2, v_3$ e $v_4$ as quantidades de caixas que chegam e saem são as mesmas; \pause
- A quantidade de caixas que sai de Vancouver e a mesma que chega em Winnipeg.

\pause

Considerando que esta forma de transportar as caixas é ótima, qual a quantidade máxima de caixas que podem ser transportadas de Vancouver para Winnipeg diariamente? \pause $12 + 11 = 23$.


## Outros problemas

Existem diversos outro problemas que podem ser modelados de forma similar \pause

- Transporte de aguá em dutos \pause
- Redes de distribuição de energia elétrica \pause
- Fluxo de nutrientes em ecossistemas \pause
- Etc \pause

Vamos formalizar alguns conceitos relacionados a estes tipos de problemas.


## Conceitos

Uma **rede** $G = (V, E)$ é um grafo orientado no qual cada aresta $(u, v) \in E$ tem uma capacidade $c(u, v) \ge 0$. \pause

- Se $G$ contém a aresta $(u, v)$ ele não pode conter $(v, u)$; \pause

- Se $(u, v) \not \in E$, então $c(u, v) = 0$; \pause

- Destacamos dois vértice $s$ (**fonte**) e $t$ (**sumidouro**); \pause

- Para cada vértice $v \in V$, temos $s \leadsto v \leadsto t$.


## Conceitos

Um **fluxo** em $G$ é uma função $f: V \times V \rightarrow \mathbb{R}$ que satisfaz as seguintes propriedades: \pause

- **Restrição de capacidade**: Para todo $u, v \in V$,
  $$0 \le f(u, v) \le c(u,v)$$ \pause
- **Conservação do fluxo**: Para todo $u \in V -\{s, t\}$
  $$\sum_{v \in V} f(v, u) = \sum_{v \in V} f(u, v)$$ \pause

A quantidade $f(u, v)$ é chamada de fluxo entre $u$ e $v$. Quando $(u, v) \not \in E$, não pode haver fluxo de $u$ para $v$ e portanto $f(u, v) = 0$.


## Conceitos

O **valor** $|f|$ do fluxo $f$ é definido como
$$|f| = \sum_{v \in V} f(s, v) - \sum_{v \in V} f(v, s)$$
ou seja, o fluxo total que saí de $s$ menos o fluxo total que entra em $s$.


## Exemplo

\includegraphics[trim=1900pt 0pt 0pt 0pt,clip,height=3.5cm]{imagens/Fig-26-1.pdf}

\pause

Quais são os valores \vspace{-1em}

- $c(v_3, t)$? \pause 20 \pause
- $c(v_1, v_4)$? \pause 0 \pause
- $f(v_2, v_4)$? \pause 11 \pause
- $f(v_1, t)$? \pause 0 \pause
- $|f|$? \pause 19


## Ajustando o modelo

Arestas antiparalelas

- Suponha que a firma de caminhões oferecesse para Lucky Puck a oportunidade de transportar 10 caixas nos caminhões indo de Edmonton para Calgary

- Parecesse uma boa oportunidade, o problema é que isto viola a restrição de que se $(v_1, v_2) \in E$, então $(v_2, v_1) \not \in E$ (as arestas $(v_1, v_2)$ e $(v_2, v_1)$ são chamadas de **antiparalelas**)

\pause

- Transformamos em uma rede equivalente

    - Escolhemos uma aresta, neste caso $(v_1, v_2)$, e a dividimos adicionando um $v'$ substituindo a aresta $(v_1, v_2)$ pelas arestas $(v_1, v')$ e $(v', v_2)$


## Ajustando o modelo

![](imagens/Fig-26-2.pdf)


## Ajustando o modelo

Redes com múltiplas fontes e sumidouros

- A empresa poderia ter mais que uma fábrica e mais que um depósito

- Não está de acordo com a definição de rede

\pause

- Transformamos em uma rede equivalente

    - Adicionamos uma super fonte $s$ e arestas com capacidade $\infty$ de $s$ para cada fonte original

    - Adicionamos um super sumidouro e arestas com capacidade $\infty$ de cada sumidouro original para o super sumidouro


## Ajustando o modelo

![](imagens/Fig-26-3.pdf){width=10cm}


## Problema do fluxo máximo

Dado uma rede $G$, uma fonte $s$ e um sumidouro $t$, o **problema do fluxo máximo** consiste em encontrar um fluxo em $G$ de valor máximo. \pause

Como resolver este problema? \pause Quais técnicas de projeto de algoritmos podemos tentar? \pause

- Algoritmos gulosos

- Programação dinâmica

- Melhoramento iterativo

- Etc


## Algoritmo guloso

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 100pt 1650pt 0pt,clip,width=6cm]{imagens/Fig-26-1.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1850pt 650pt 0pt 650pt,clip,width=5.6cm]{imagens/Fig-26-6-R.pdf}
</div>
</div>

Como construir a solução ótima usando um algoritmo guloso? \pause

- Qual é a escolha gulosa? \pause

- O problema tem subestrutura ótima?


## Programação dinâmica

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 100pt 1650pt 0pt,clip,width=6cm]{imagens/Fig-26-1.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1850pt 650pt 0pt 650pt,clip,width=5.6cm]{imagens/Fig-26-6-R.pdf}
</div>
</div>

Como construir a solução ótima usando um algoritmo de programação dinâmica? \pause

- Quais são os subproblemas? \pause

- O problema tem subestrutura ótima?


## Melhoramento iterativo

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 100pt 1650pt 0pt,clip,width=6cm]{imagens/Fig-26-1.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1850pt 650pt 0pt 650pt,clip,width=5.6cm]{imagens/Fig-26-6-R.pdf}
</div>
</div>

Como construir a solução ótima usando um algoritmo de melhoramento iterativo? \pause

- Como construir um fluxo inicial? \pause $f(u, v) = 0$ para todos os pares $(u, v) \in V \times V$. \pause

- Como melhorar o fluxo? \pause Achar um caminho "viável" qualquer de $s$ para $t$ e alterar o fluxo ao longo do caminho.


## Melhoramento iterativo

\includegraphics[trim=0pt 0pt 1650pt 0pt,clip,height=3.0cm]{imagens/Fig-26-1.pdf}

\pause

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 1400pt 1650pt 0pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}

\pause
\footnotesize Qual o fluxo máximo que podemos "enviar" ao longo desse caminho? \pause 4.
</div>
<div class="column" width="50%">
\pause
\includegraphics[trim=1750pt 1400pt 0pt 0pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
</div>


## Melhoramento iterativo

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 1400pt 1650pt 0pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1750pt 1400pt 0pt 0pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
</div>

\pause
Porque o fluxo resultante é válido? \pause

Restrição de capacidade: \pause escolhemos "enviar" ao longo do caminho um fluxo que é válido para cada aresta do caminho. \pause

Conservação do fluxo: \pause para um vértice $v$ ao longo do caminho, diferente de $s$ e $t$, existe apenas um fluxo que entra em $v$ e um fluxo que saí de $v$ e eles têm o mesmo valor.


## Melhoramento iterativo

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 1400pt 1650pt 0pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1750pt 1400pt 0pt 0pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
</div>

Procurar uma forma de aumentar o fluxo nulo é simples, mas como fazer isso se o fluxo na rede não é nulo? \pause Como garantir que as capacidades das arestas não serão violadas? Como garantir a conservação do fluxo? \pause \vspace{-1em}

- Vamos criar uma rede nova (com fluxo nulo) que representa a forma que o fluxo atual pode ser alterado \pause
- Depois procuramos um caminho de $s$ para $v$ na nova rede e criamos um fluxo por este caminho, como fizemos anteriormente \pause
- Por fim, "juntamos" o fluxo na nova rede com o fluxo atual aumentado o seu valor


## Melhoramento iterativo

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 1400pt 1650pt 0pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1750pt 1400pt 0pt 0pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
</div>

\pause

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 700pt 1650pt 700pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
<div class="column" width="50%">
\pause
\includegraphics[trim=1750pt 700pt 0pt 700pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
</div>


## Melhoramento iterativo

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 700pt 1650pt 700pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1750pt 700pt 0pt 700pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
</div>

\pause

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 0pt 1650pt 1400pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
<div class="column" width="50%">
\pause
\includegraphics[trim=1750pt 0pt 0pt 1400pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
</div>


## Melhoramento iterativo

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 0pt 1650pt 1400pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1750pt 0pt 0pt 1400pt,clip,height=5cm]{imagens/Fig-26-6-L.pdf}
</div>
</div>

\pause

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 1400pt 1650pt 0pt,clip,height=5cm]{imagens/Fig-26-6-R.pdf}
</div>
<div class="column" width="50%">
\pause
\includegraphics[trim=1750pt 1400pt 0pt 0pt,clip,height=5cm]{imagens/Fig-26-6-R.pdf}
</div>
</div>


## Melhoramento iterativo

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 1400pt 1650pt 0pt,clip,height=5cm]{imagens/Fig-26-6-R.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1750pt 1400pt 0pt 0pt,clip,height=5cm]{imagens/Fig-26-6-R.pdf}
</div>
</div>

\pause

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 700pt 1650pt 700pt,clip,height=5cm]{imagens/Fig-26-6-R.pdf}
</div>
<div class="column" width="50%">
\pause
\includegraphics[trim=1750pt 700pt 0pt 700pt,clip,height=5cm]{imagens/Fig-26-6-R.pdf}
</div>
</div>


## Melhoramento iterativo

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 700pt 1650pt 700pt,clip,height=5cm]{imagens/Fig-26-6-R.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1750pt 700pt 0pt 700pt,clip,height=5cm]{imagens/Fig-26-6-R.pdf}
</div>
</div>

\pause

<div class="columns">
<div class="column" width="50%">
\includegraphics[trim=0pt 0pt 1650pt 1400pt,clip,height=5cm]{imagens/Fig-26-6-R.pdf}
</div>
<div class="column" width="50%">
\includegraphics[trim=1750pt 0pt 0pt 1400pt,clip,height=5cm]{imagens/Fig-26-6-R.pdf}
</div>
</div>


## O método de Ford-Fulkerson

<div class="columns">
<div class="column" width="37%">
Esta ideia de melhoramento iterativo é chamado de método de Ford-Fulkerson \pause

- Começamos com $f(u, v) = 0$ para todo $u, v \in G$ (portanto $|f| = 0$); \pause

- A cada iteração, aumentamos o valor do fluxo encontrando um "caminho de aumento" na "rede residual"; \pause

- O processo continua até que nenhum caminho de aumento seja encontrado; \pause

</div>
<div class="column" width="60%">

\begin{codebox}
    \Procname{$\proc{Ford-Fulkerson-Method}(G, s, t)$}
    \li Iniciar o fluxo $f$ com $0$
    \li \While existe um caminho de aumento $p$ na rede residual $G_f$ \Do
    \li     aumente $f$ ao longo de $p$
        \End
    \li \Return $f$
\end{codebox}

</div>
</div>


## O método de Ford-Fulkerson

Vamos definir alguns conceitos e ver alguns lemas e corolários necessários para a análise de corretude do método.


## Redes residuais

Intuitivamente, uma rede residual $G_f$ de uma rede $G$ e um fluxo $f$ consiste de arestas com capacidades que representam como o fluxo das arestas de $G$ podem ser alterados. \pause

Seja $G = (V, E)$ uma rede com fonte $s$ e sumidouro $t$, $f$ um fluxo em $G$ e $u, v \in V$, definimos \pause

- A **capacidade residual** $c_f(u, v)$ como \pause
  $$c_f(u, v) = \begin{cases}
        c(u, v) - f(u, v) & \text{se } (u, v) \in E \\
        f(v, u)           & \text{se } (v, u) \in E \\
        0                 & \text{caso contrário}
  \end{cases}$$ \pause
- A **rede residual** $G_f = (V, E_f)$ de $G$ induzida por $f$ onde
  $$E_f = \{(u, v) \in V \times V : c_f(u, v) > 0\} \text{ e } |E_f| \le 2 |E|$$


## Aumento do fluxo

Seja $f$ um fluxo em $G$ e $f'$ um fluxo na rede residual $G_f$, definimos $f \uparrow f'$, o **aumento** do fluxo $f$ por $f'$, como sendo a função $V \times V \rightarrow \mathbb{R}$ \pause

$$(f \uparrow f')(u, v) = \begin{cases}
  f(u, v) + f'(u, v) - f'(v, u) & \text{se } (u, v) \in E \\
  0                             & \text{caso contrário}
\end{cases}$$

\pause

Esta definição reflete o propósito da forma que fizemos a definição de rede residual: descrever como o fluxo pode ser alterado em uma aresta. O fluxo entre $(u, v)$ aumenta por $f'(u, v)$ mas diminui por $f'(v, u)$.


## Lema 26.1

**Lema 26.1**

Seja $G = (V, E)$ uma rede com fonte $s$ e sumidouro $t$ e seja $f$ um fluxo em $G$. Seja $G_f$ uma rede residual de $G$ induzida por $f$ e seja $f'$ um fluxo em $G_f$. Então a função $f \uparrow f'$ definida na equação (26.4) é um fluxo em $G$ com valor $|f \uparrow f'| = |f| + |f'|$.


## Caminho de aumento e capacidade residual

Dado uma rede $G = (V, E)$ e um fluxo $f$, um **caminho de aumento** $p$ é um caminho simples de $s$ para $t$ na rede residual $G_f$. \pause

O valor máximo que pode ser aumentado no fluxo de cada aresta no caminho de aumento $p$ é chamado **capacidade residual** de $p$, e é dado por
$$c_f(p) = \min \{c_f(u, v): (u, v) \text{ está em } p\}$$


## Lema 26.2

**Lema 26.2**

Seja $G = (V, E)$ uma rede, $f$ um fluxo em $G$ e $p$ um caminho de aumento em $G_f$. Seja a função $f_p: V \times V \rightarrow \mathbb{R}$, definida como

$$f_p(u, v) = \begin{cases}
  c_f(p) & \text{se } (u, v) \text{ está em } p \\
  0      & \text{caso contrário}
\end{cases}$$

Então, $f_p$ é um fluxo em $G_f$ com valor $|f_p| = c_f(p) > 0$.


## Corolário 26.3

**Corolário 26.3**

Seja $G = (V, E)$ uma rede, $f$ um fluxo em $G$ e $p$ um caminho de aumento em $G_f$. Seja a função $f_p$ como definido na equação (26.8) e suponha que nós aumentamos $f$ por $f_p$. Então a função $f \uparrow f_p$ é um fluxo em $G$ com valor $|f \uparrow f_p| = |f| + |f_p| > |f|$.

\pause

**Prova**

A partir dos lemas 26.1 e 26.2.


## Corretude do método

Os lemas e corolários que vimos até então mostram que o método constrói um fluxo válido, agora precisamos mostrar que o fluxo é máximo. \pause

Qual o critério de parada do método? \pause Não existir mais caminho de aumento na rede residual. \pause

Precisamos mostrar que a não existência de um caminho de aumento implica que o fluxo é máximo. \pause

Fazer isso diretamente é difícil, vamos ver um conceito novo que vai facilitar este processo.


## Corte de rede

Um corte em uma rede é uma separação dos vértices da rede em dois conjuntos de forma que $s$ e $t$ fiquem em conjuntos diferentes. \pause

![](imagens/Fig-26-5.pdf){width=7cm}


## Corte de rede

Um corte $(S, T)$ de uma rede $G = (V, E)$ é uma partição de $V$ em $S$ e $T = V - S$, tal que $s \in S$ e $t \in T$ \pause

- Se $f$ é um fluxo, então o **fluxo líquido** $f(S, T)$ através do corte $(S, T)$ é definido como
  $$f(S, T) = \sum_{u \in S} \sum_{v \in T} f(u, v) -  \sum_{u \in S} \sum_{v \in T} f(v, u)$$ \pause
- A **capacidade** do corte $(S, T)$ é
  $$c(S, T) = \sum_{u \in S} \sum_{v \in T} c(u, v)$$ \pause
- Um **corte mínimo** de uma rede é um corte que tem capacidade mínima entre todos os cortes da rede


## Exemplo de corte

![](imagens/Fig-26-5.pdf){width=7cm}

\pause

Qual o fluxo líquido $f(S, T)$? \pause 19. \pause

Qual a capacidade $c(S, T)$? \pause 26. \pause

Qual é um corte de capacidade mínima? \pause $S = \{s, v_1, v_2, v_4\}$ e $T = \{ v_3, t \}$ com capacidade 23.


## Lema 26.4

**Lema 26.4**

Seja $f$ um fluxo em uma rede $G$ com fonte $s$ e sumidouro $t$, e seja $(S, T)$ qualquer corte de $G$. Então o fluxo líquido através do corte $(S, T)$ é $f(S, T) = |f|$.


## Corolário 26.5

**Corolário 26.5**

O valor do fluxo $f$ em uma rede $G$ é limitado superiormente pela capacidade de qualquer corte de $G$.


## Teorema do fluxo máximo e corte mínimo

**Teorema 26.6**

O valor do fluxo máximo é igual a capacidade de um corte mínimo.

Seja $f$ um fluxo em uma rede $G = (V, E)$ com fonte $s$ e sumidouro $t$, então as seguintes condições são equivalentes:

1. $f$ é um fluxo máximo em $G$

2. A rede residual $G_f$ não contém nenhum caminho de aumento

3. $|f| = c(S, T)$ para algum corte $(S, T)$ de $G$


## Algoritmo básico de Ford-Fulkerson

Lembrando o método de Ford-Fulkerson...

Em cada iteração algum caminho de aumento $p$ é encontrado e utilizado para modificar o fluxo $f$.

O fluxo $f$ é ser substituído por $f \uparrow f_p$, gerando um novo fluxo com valor $|f| + |f_p|$.

Quando não existe mais caminho de aumento, $f$ é máximo


## Algoritmo básico de Ford-Fulkerson

Como atualizar o fluxo em cada arestas? \pause

- Cada aresta residual em $p$ é uma aresta na rede original ou uma aresta contrária na rede original

- Fluxo é adicionado se a aresta é a original

- Fluxo é removido se a aresta é contrária


## Algoritmo básico de Ford-Fulkerson

\begin{codebox}
    \Procname{$\proc{ford-fulkerson}(G, s, t)$}
    \li \For $(u, v) \in \attrib{G}{E}$ \Do
    \li     $\attrib{(u, v)}{f} = 0$
        \End
    \li \While existe um caminho $p$ de $s$ a $t$ em $G_f$ \Do
    \li     $c_f(p) = \min\{c_f(u, v): (u, v) \text{ está em } p\}$
    \li     \For $(u, v) \in p$ \Do
    \li         \If $(u, v) \in E$ \Do
    \li             $\attrib{(u, v)}{f} = \attrib{(u, v)}{f} + c_f(p)$
    \li         \Else
    \li             $\attrib{(v, u)}{f} = \attrib{(v, u)}{f} - c_f(p)$
                \End
            \End
        \End
    \li \Return $f$
\end{codebox}


## Algoritmo básico de Ford-Fulkerson

Análise do tempo de execução

- Depende de como o caminho $p$ é escolhido

- Vamos supor que todas as capacidades sejam inteiras


## Algoritmo básico de Ford-Fulkerson

\small

Análise do tempo de execução

- Seja $f^*$ o fluxo máximo na rede residual

- Então, o laço \While das linhas 3-8 executa no máximo $|f^*|$, isto porque o valor do fluxo aumenta em pelo menos uma unidade em cada iteração

- O conteúdo dentro do \While pode ser executado de forma eficiente se escolhermos a estrutura correta para representar a rede e se o caminho de aumento for encontrado em tempo linear

    - Manter um grafo $G' = (V, E')$, onde $E' = \{(u, v): (u, v) \in E \text{ ou } (v, u) \in E\}$

    - Encontrar o caminho de aumento com \proc{DFS} ou \proc{BFS}, tempo $O(V + E') = O(E)$

    - Cada iteração demora $O(E)$

- Portanto, o tempo de execução do algoritmo é $O(E |f^*|)$


## Exemplo ruim

![](imagens/Fig-26-7.pdf)


## Algoritmo de Edmonds-Karp

O algoritmo de Edmonds-Karp utiliza a busca em largura para encontrar o caminho de aumento $p$

- $p$ é um caminho entre $s$ e $t$ com o menor número de arestas

- Executa em $O(VE^2)$


## Referências

- Thomas H. Cormen et al. Introduction to Algorithms. \nth{3} edition. Capítulo 26.
