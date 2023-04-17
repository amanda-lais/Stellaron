# -*- coding: utf-8 -*-

# Grafo como uma lista de adjacência
class GrafoLista:
    TAM_MAX_DEFAULT = 100  # qtde de vértices máxima default

    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n  # número de vértices
        self.m = 0  # número de arestas
        # lista de adjacência
        self.listaAdj = [[] for i in range(self.n)]

    # Insere uma aresta no Grafo tal que
    # v é adjacente a w
    def insere_a(self, v, w):
        self.listaAdj[v].append(w)
        self.m += 1

    # remove uma aresta v->w do Grafo
    def remove_a(self, v, w):
        self.listaAdj[v].remove(w)
        self.m -= 1

    # Apresenta o Grafo contendo
    # número de vértices, arestas
    # e a LISTA de adjacência obtida
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            print(f"\n{i:2d}: ", end="")
            for w in range(len(self.listaAdj[i])):
                val = self.listaAdj[i][w]
                print(f"{val:2d}", end="")

        print("\n\nfim da impressao do grafo.")

    ###############################################################################
    ##      Exercícios neste arquivo (grafoLista.py): 12, 14, 15, 16, 17, 19, 20 ##
    ###############################################################################

    # EX12 --- se dois grafos direcionados sao iguais ||Amanda
    def compara(self, o):
        if self.listaAdj == o.listaAdj:
            print("Sao iguais")
            return True
        else:
            print("Nao sao iguais")
            return False

    # EX14 --- recebe um grafo em lista de adjacência e inverta a lista de adjacência de todos os vértices || Amanda
    def inverte_lista(self, u):
        self.listaAdj[u].reverse()

    # EX15 - se é fonte ou não \\amanda -- usa os in e out degree pra fazer esse
    def out_degree(self, v: int) -> int:
        return len(self.listaAdj[v])

    def in_degree(self, v: int) -> int:
        aparicoes = 0
        for vertice in self.listaAdj:
            for v2 in vertice:
                if v2 == v:
                    aparicoes += 1
        return aparicoes

    def is_fonte(self, v):
        if self.in_degree(v) == 0 and self.out_degree(v) > 0:
            return 1
        return 0

    # EX16
    def is_sorvedouro(self, v: int) -> int:
        if self.in_degree(v) > 0 and self.out_degree(v) == 0:
            return 1
        return 0

    # EX17 --- receba um grafo dirigido e retorna 1 se o grafo for simétrico ou 0 || Amanda
    def is_symm(self):
        j = 0
        for i in self.listaAdj:
            if len(i) == 0:
                continue
            for w in i:
                if j not in self.listaAdj[w]:
                    return 0
            j += 1
        return 1

    # EX19 --- remover vértices de um grafo direcionado e não direcionado
    def remover(self, v: int) -> int:
        if v < self.n:
            for vertice in range(len(self.listaAdj) - 1):
                if v in self.listaAdj[vertice]:
                    self.remove_a(vertice, v)
                if v == vertice:
                    for a in self.listaAdj[v]:
                        self.remove_a(v, a)
            del self.listaAdj[v]
            self.n -= 1
            return 1
        return 0

    # EX20
    def completo(self, v):
        checa = 1
        for i in range(self.n):
            if v in self.listaAdj[i] == 1:
                continue
            else:
                checa = 0
                break
        if checa == 1:
            return 1
        else:
            return 0
