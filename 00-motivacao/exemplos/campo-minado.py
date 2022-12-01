from dataclasses import dataclass
from enum import Enum


class Item(Enum):
    BOMBA = 0
    NENHUM = 1


class Estado(Enum):
    ABERTO = 0
    FECHADO = 1


@dataclass
class Casa:
    item: Item
    estado: Estado


Campo = list[list[Casa]]


def CampoMinado(nlin: int, ncol: int) -> Campo:
    """
    Cria um campo minado com nlin linhas e ncol colunas com todas as casas sem
    nenhum item e fechada.
    """
    return [[Casa(Item.NENHUM, Estado.FECHADO) for _ in range(ncol)] for _ in range(nlin)]


def coloca_bomba(campo: Campo, lin: int, col: int):
    """
    Coloca uma bomba no campo na casa (lin, col).
    """
    campo[lin][col].item = Item.BOMBA


def abre(campo: Campo, lin: int, col: int):
    """
    Abre a casa (lin, col) de campo, se a casa estiver aberta, não faz nada.
    Se a casa (lin, col) tiver uma bomba abre a casa e para, senão abre a casa
    com abre_.
    """
    if campo[lin][col].estado == Estado.ABERTO or \
            campo[lin][col].item == Item.BOMBA:
        campo[lin][col].estado = Estado.ABERTO
    else:
        abre_(campo, lin, col)


def abre_(campo: Campo, lin: int, col: int):
    """
    Abre a casa (lin, col) de campo e se não tiver bombas ao redor da casa abre
    todas ao redor, senão para.

    Requer que a casa (lin, col) esteja fechada.
    """
    campo[lin][col].estado = Estado.ABERTO
    if numero_bombas(campo, lin, col) == 0:
        for vlin, vcol in vizinhos(campo, lin, col):
            if campo[vlin][vcol].estado == Estado.FECHADO:
                abre_(campo, vlin, vcol)


def rep(campo: Campo) -> list[str]:
    """
    Cria uma representação de campo criando uma string para cada linha de campo da seguinte forma:
    casa fechada -> "⬛"
    casa aberta com bomba -> "💥"
    casa aberta sem bomba ao redo -> "  "
    casa aberta com n bombas ao redor -> "n"
    """
    r = []
    for lin, linha in enumerate(campo):
        s = ""
        for col, casa in enumerate(linha):
            if casa.estado == Estado.FECHADO:
                s += "⬛"
            elif casa.item == Item.BOMBA:
                s += "💥"
            else:
                n = numero_bombas(campo, lin, col)
                s += "  " if n == 0 else f"{n:>02}"
        r.append(s)
    return r


def vizinhos(campo: Campo, lin: int, col: int) -> list[tuple[int, int]]:
    """
    Produz uma lista com as casas vizinhas da casa (lin, col) de campo.
    """
    v = []
    for dl in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            vlin = lin + dl
            vcol = col + dc
            if (vlin, vcol) != (lin, col) and \
                    0 <= vlin < len(campo) and \
                    0 <= vcol < len(campo[0]):
                v.append((vlin, vcol))
    return v


def numero_bombas(campo: Campo, lin: int, col: int) -> int:
    """
    Devolve o número de bombas ao redor da casa (lin, col) de campo.
    """
    n = 0
    for vlin, vcol in vizinhos(campo, lin, col):
        if campo[vlin][vcol].item == Item.BOMBA:
            n += 1
    return n


def tests():

    #    0  1  2  3
    # 0 01 💥 01 00
    # 1 01 01 02 01
    # 2 00 00 01 💥
    # 3 00 00 01 01
    # 4 00 00 00 00

    campo = CampoMinado(5, 4)
    coloca_bomba(campo, 0, 1)
    coloca_bomba(campo, 2, 3)

    abre(campo, 0, 1)

    assert rep(campo) == ["⬛💥⬛⬛",
                          "⬛⬛⬛⬛",
                          "⬛⬛⬛⬛",
                          "⬛⬛⬛⬛",
                          "⬛⬛⬛⬛"]

    abre(campo, 0, 0)

    assert numero_bombas(campo, 0, 3) == 0
    assert numero_bombas(campo, 0, 0) == 1
    assert numero_bombas(campo, 1, 2) == 2

    assert rep(campo) == ["01💥⬛⬛",
                          "⬛⬛⬛⬛",
                          "⬛⬛⬛⬛",
                          "⬛⬛⬛⬛",
                          "⬛⬛⬛⬛"]

    abre(campo, 2, 1)
    assert rep(campo) == ["01💥⬛⬛",
                          "010102⬛",
                          "    01⬛",
                          "    0101",
                          "        "]


tests()
