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


# Encontra o "número de Erdős" de cada pessoa usando pares como uma lista de
# cooperação. Num é um dicionário que associa cada pessoa com seu número.
# A pessoa inicial (representando o Erdős) deve iniciar com o número 0.
def enumera(pares, num):
    for d in range(0, len(pares)):
        # Encontra pessoas que não tem número e estão ligadas a pessoas com
        # número d e atribuí número d + 1 a elas
        for (p1, p2) in pares:
            if num[p1] == d and num[p2] == None:
                num[p2] = d + 1
            elif num[p1] == None and num[p2] == d:
                num[p1] = d + 1


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

    # Dicionário (tabela hash) que associa cada nome com um número. None é
    # usado para indicar que a pessoa não tem número
    num = {
        "babai": None,
        "bondy": None,
        "chvatal": None,
        "deng": None,
        "erdos": None,
        "gates": None,
        "harary": None,
        "hell": None,
        "imrich": None,
        "lovasz": None,
        "murty": None,
        "papadimitriou": None,
        "watkins": None,
        "white": None,
    }

    num["erdos"] = 0

    enumera(pares, num)

    assert num["babai"] == 1
    assert num["bondy"] == 2
    assert num["chvatal"] == 1
    assert num["deng"] == 2
    assert num["erdos"] == 0
    assert num["gates"] == 4
    assert num["harary"] == 1
    assert num["hell"] == 1
    assert num["imrich"] == 2
    assert num["lovasz"] == 1
    assert num["murty"] == 3
    assert num["papadimitriou"] == 3
    assert num["watkins"] == 2
    assert num["white"] == 2

    print("Testes executados com sucesso.")


####################################
# Extra: leitura a partir de arquivo

# Lê os pares de nomes a partir de arquivo e enumera as pessoas a partir da
# pessoa como nome inicio
def run(arquivo, inicio):
    pares = le_pares(arquivo)
    nomes = sorted(set(nome for par in pares for nome in par))
    num = {nome: None for nome in nomes}

    if inicio not in num:
        print(f"Nome inicial não está na lista de pares: {inicial}", file=sys.stderr)
        sys.exit(1)
    else:
        num[inicio] = 0

    enumera(pares, num)

    for nome in nomes:
        print(f"{nome} = {num[nome]}")


# Lê uma sequência de pares de um arquivo
def le_pares(arquivo):
    pares = list(open(arquivo).read().split())
    if len(pares) % 2 != 0:
        print("Arquivo inválido: número impares de pessoas", file=sys.stderr)
        sys.exit(1)
    return list((pares[i], pares[i + 1]) for i in range(0, len(pares), 2))


# Chama a função principal
if __name__ == "__main__":
    main()
