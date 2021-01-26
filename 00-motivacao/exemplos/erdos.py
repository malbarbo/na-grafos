from typing import Dict, List, Tuple

# Programa para calcular o Número de Erdős
#
# Este programa foi feito como exemplo para uma aula inicial de Algoritmos em
# Grafos. O programa não usa um algoritmo eficiente, mas sim um algoritmo
# ingênuo que é simples e direto.

import sys


def main():
    # Se nenhum argumento for especificado, executa os testes;
    # Senão é necessário dois argumentos, o nome do arquivo com os pares e o
    # nome da pessoal inicial.
    if len(sys.argv) == 1:
        test()
    elif len(sys.argv) == 3:
        run(sys.argv[1], sys.argv[2])
    else:
        print("Número de argumentos inválidos!")
        print(f"  use python3 {sys.argv[0]} arquivo-de-pares nome-pessoa-inicial")
        sys.exit(1)


# Encontra o "número de Erdős" de cada pessoa a partir de um vertices inicial
# (raiz) e uma lista de pares de cooperação (pares). A função produz um
# dicionário que associa cada pessoa com seu número.
def enumera(pares: List[Tuple[str, str]], raiz: str) -> Dict[str, int]:
    num = {raiz: 0}
    for d in range(0, len(pares)):
        # Encontra pessoas que não tem número e estão ligadas a pessoas com
        # número d e atribuí número d + 1 a elas
        for (p1, p2) in pares:
            if p1 in num and num[p1] == d and p2 not in num:
                num[p2] = d + 1
            if p2 in num and num[p2] == d and p1 not in num:
                num[p1] = d + 1
    return num


def test():
    pares = [
        ("babai", "imrich"),
        ("babai", "lovasz"),
        ("bondy", "murty"),
        ("chvatal", "bondy"),
        ("chvatal", "hell"),
        ("deng", "papadimitriou"),
        ("erdos", "babai"),
        ("erdos", "chvatal"),
        ("erdos", "harary"),
        ("erdos", "hell"),
        ("erdos", "lovasz"),
        ("harary", "hell"),
        ("harary", "white"),
        ("hell", "bondy"),
        ("hell", "deng"),
        ("hell", "watkins"),
        ("imrich", "watkins"),
        ("papadimitriou", "gates"),
        ("white", "bondy"),
    ]

    esperado = {
        "babai": 1,
        "bondy": 2,
        "chvatal": 1,
        "deng": 2,
        "erdos": 0,
        "gates": 4,
        "harary": 1,
        "hell": 1,
        "imrich": 2,
        "lovasz": 1,
        "murty": 3,
        "papadimitriou": 3,
        "watkins": 2,
        "white": 2,
    }

    num = enumera(pares, "erdos")

    assert num == esperado

    print("Testes executados com sucesso.")


####################################
# Extra: leitura a partir de arquivo

# Lê os pares de nomes a partir de arquivo e enumera as pessoas a partir da
# pessoa como nome inicio
def run(arquivo: str, inicio: str):
    pares = le_pares(arquivo)
    nomes = sorted(set(nome for par in pares for nome in par))

    if inicio not in nomes:
        print(f"Nome inicial não está na lista de pares: {inicio}", file=sys.stderr)
        sys.exit(1)

    num = enumera(pares, inicio)

    for nome in nomes:
        if nome in num:
            print(f"{nome} = {num[nome]}")


# Lê uma sequência de pares de um arquivo
def le_pares(arquivo: str) -> List[Tuple[str, str]]:
    pares = list(open(arquivo).read().split())
    if len(pares) % 2 != 0:
        print("Arquivo inválido: número impares de pessoas", file=sys.stderr)
        sys.exit(1)
    return list((pares[i], pares[i + 1]) for i in range(0, len(pares), 2))


# Chama a função principal
if __name__ == "__main__":
    main()
