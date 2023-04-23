# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023
@author: icalc
"""
import math

class Fila:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class GrafoMatriz:
    TAM_MAX_DEFAULT = 100  # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT, rotulado=False):
        self.n = n  # número de vértices
        self.m = 0  # número de arestas
        self.rotulado = False  # servirá de verificação nos métodos abaixo
        # matriz de adjacência
        if rotulado:
            self.rotulado = True
            self.adj: list[list[float]] = [[math.inf for i in range(n)] for j in range(n)]
        else:
            self.adj = [[0 for i in range(n)] for j in range(n)]

    # Insere uma aresta no Grafo tal que
    # v é adjacente a w
    def insere_a(self, v, w, rotulo=-1):  # rotulo -1 é para quando não se sabe o peso daquela aresta
        if self.rotulado and self.adj[v][w] == math.inf:
            self.adj[v][w] = rotulo
            self.m += 1
        if not self.rotulado and self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.m += 1  # atualiza qtd arestas

    def insere_v(self):
        self.n += 1
        if self.rotulado:
            for linha in self.adj:
                linha.append(math.inf)
            self.adj.append([math.inf for i in range(self.n)])
        else:
            self.adj.append([0 for i in range(self.n)])

    # remove uma aresta v->w do Grafo
    def remove_a(self, v, w):
        # testa se temos a aresta
        if not self.rotulado and self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.m -= 1  # atualiza qtd arestas
        if self.rotulado and self.adj[v][w] != math.inf:
            self.adj[v][w] = math.inf
            self.m -= 1

    def show(self):
        print(f"\n n: {self.n:2d} m: {self.m:2d} r: {self.rotulado}\n")
        for i in range(self.n):
            for w in range(self.n):
                print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]} | ", end="")
            print("\n")
        print("\nfim da impressao do grafo.")

    def in_degree(self, v: int) -> int:
        return len([linha for linha in self.adj if linha[v] != 0 and linha[v] != math.inf])

    def is_fonte(self, v: int) -> int:
        if self.in_degree(v) == 0 and self.out_degree(v) > 0:
            return 1
        return 0

    @staticmethod
    def visitar_no(no: int):
        print(f"Estamos visitando o nó {no}")

    @staticmethod
    def marcar_no(marcados, no):
        marcados.append(no)
        return marcados

    def no_adjacente(self, no, marcados):
        adjs = self.adj[no]
        for _ in range(self.n):
            if (adjs[_] != 0 and adjs[_] != math.inf) and _ not in marcados:
                return _
        return -1

    def nos_adjacentes(self, no, marcados):
        return [index for index, valor in enumerate(self.adj[no]) if (valor != 0 and valor != math.inf) and marcados]

    def show_min(self):
        print(f"\n n: {self.n:2d} m: {self.m:2d} r: {self.rotulado}\n")
        for i in range(self.n):
            for w in range(self.n):
                print(f" {self.adj[i][w]} |", end="")
            print("\n")
        print("\nfim da impressao do grafo.")

    def is_adjac(self, i, j) -> int:
        if (self.adj[i][j] != 0 or self.adj[j][i] != 0) == True:
            return True

    def is_adjacto(self, i):
        vertices = []
        for x in range(self.n):
            if self.adj[i][x] or self.adj[x][i] > 0:
                vertices.append(x)
        return(vertices)
    
    def ordenacao_topologica(self, vInicio):
        visitados = []
        ge = [None]*self.n
        pos = 0
        for i in range(self.n):
            ge[pos] = self.in_degree(i)
            pos += 1
        f = Fila()
        for i in range(len(ge)):
            if ge[i] == 0:
                f.enqueue(i)
                ge[i] = -1
        while f.is_empty() == False:
            n = f.dequeue()
            self.visitar_no(n)
            visitados.append(n)
            j = self.is_adjacto(n)
            for i in j:
                if ge[i] == -1:
                    continue
                ge[i] -= 1
            for i in range(len(ge)):
                if ge[i] == 0:
                    f.enqueue(i)
                    ge[i] = -1
        return visitados
