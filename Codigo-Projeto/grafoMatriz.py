import math
from util import Pilha
from queue import PriorityQueue

# CLASSES
# grafo nao direcionado -- rotulado ou não

class TGrafoND:
    TAM_MAX_DEFAULT = 100
    def __init__(self, n=TAM_MAX_DEFAULT, rotulado=False):
        self.n = n #vertices
        self.m = 0 #arestas
        self.rotulado = False
        self.visitados = []
        if rotulado:
            self.rotulado = True
            self.adj = [[math.inf for i in range(n)] for j in range(n)]
        else:
            self.adj = [[0 for i in range(n)] for j in range(n)]

    def insere_v(self):
        self.n += 1
        if self.rotulado:
            for linha in self.adj:
                linha.append(math.inf)
            self.adj.append([math.inf for i in range(self.n)])
        else:
            self.adj.append([0 for i in range(self.n)])

    def insere_a(self, v, w, valor: float = 1):
        if self.rotulado and self.adj[v][w] == math.inf:
            self.adj[v][w], self.adj[w][v] = valor, valor
            self.m += 1
        if not self.rotulado and self.adj[v][w] == 0:
            self.adj[v][w], self.adj[w][v] = valor, valor
            self.m += 1

    def remove_a(self, v, w):
        if self.rotulado and self.adj[v][w] != math.inf:
            self.adj[v][w], self.adj[w][v] = math.inf, math.inf
            self.m -= 1
        if not self.rotulado and self.adj[v][w] != 0:
            self.adj[v][w], self.adj[w][v] = 0, 0
            self.m -= 1

    def show(self):
        if self.rotulado:
            print(f"\n n: {self.n:2d} ", end="")
            print(f"m: {self.m:2d}\n")
            for i in range(self.n):
                for w in range(self.n):
                    if self.adj[i][w] != math.inf:
                        print(f"Adj[{i:2d},{w:2d}] = ", self.adj[i][w], end=" ")
                    else:
                        print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
                print("\n")
            print("\nfim da impressao do grafo.")
        else:
            print(f"\n n: {self.n:2d} ", end="")
            print(f"m: {self.m:2d}\n")
            for i in range(self.n):
                for w in range(self.n):
                    if self.adj[i][w] == 1:
                        print(f"Adj[{i:2d},{w:2d}] = 1 ", end="")
                    else:
                        print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
                print("\n")
            print("\nfim da impressao do grafo.")

    def show_min(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.rotulado:
                    if self.adj[i][w] != math.inf:
                        print(" ", self.adj[i][w], end=" ")
                    else:
                        print(" 0 ", end="")
                else:
                    if self.adj[i][w] == 1:
                        print(" 1 ", end="")
                    else:
                        print(" 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo.")

    def in_degree(self, v: int) -> int:
        return len([linha for linha in self.adj if linha[v] != 0 and linha[v] != math.inf])

    def out_degree(self, v: int) -> int:
        return len([sai for sai in self.adj[v] if sai != 0 and sai != math.inf])

    def is_fonte(self, v: int) -> int:
        if self.in_degree(v) == 0 and self.out_degree(v) > 0:
            return 1
        return 0

    def is_sorvedouro(self, v: int) -> int:
        if self.in_degree(v) > 0 and self.out_degree(v) == 0:
            return 1
        return 0

    @staticmethod
    def is_simetrico() -> int:
        return 1

    def remover(self, v: int) -> int:
        if v < self.n:
            # Remove as arestas
            for _ in range(0, len(self.adj[v])):
                self.remove_a(v, _)
                self.remove_a(_, v)
            # Remove os vértices
            for linha in self.adj:
                del linha[v]
            del self.adj[v]
            self.n -= 1
            return 1
        else:
            return 0

    def completo(self) -> int:  # dei ctrl c ctrl v
        checa = 1
        for i in range(self.n):
            for w in range(self.n):
                if i != w:
                    if self.adj[i][w] != 0 and self.adj[i][w] != math.inf:
                        continue
                    else:
                        checa = 0
                        break
        if checa == 1:
            return 1
        else:
            return 0

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

    def is_adjac(self, i, j) -> int:
        if (self.adj[i][j] != 0 or self.adj[j][i] != 0) == True:
            return True

    def is_adjacto(self, i):
        vertices = []
        for x in range(self.n):
            if self.adj[i][x] or self.adj[x][i] > 0:
                vertices.append(x)
        return(vertices)

    def percurso_profundidade(self, v_inicio):
        marcados = []
        visita = []
        p = Pilha()
        visita.append(v_inicio)
        marcados = self.marcar_no(marcados, v_inicio)
        p.push(v_inicio)
        while not p.is_empty():
            no_atual = p.pop()
            no_seguinte = self.no_adjacente(no_atual, marcados)
            while no_seguinte != -1:
                visita.append(no_seguinte)
                p.push(no_atual)
                self.marcar_no(marcados, no_seguinte)
                no_atual = no_seguinte
                no_seguinte = self.no_adjacente(no_seguinte, marcados)
        return visita

    def dijkstra(self, grafo, no_inicial):
        D = {n:float('inf') for n in range(grafo.n)}
        D[no_inicial] = 0
        pq = PriorityQueue()
        pq.put((0, no_inicial))
        while not pq.empty():
            (dist, no_atual) = pq.get()
            grafo.adj.append(no_atual)
            for vizinho in range(grafo.n):
                if grafo.adj[no_atual][vizinho] != -1:
                    dist = grafo.adj[no_atual][vizinho]
                    if vizinho not in grafo.visitados:
                        custo_antigo = D[vizinho]
                        novo_custo = D[no_atual] + dist
                        if novo_custo < custo_antigo:
                            pq.put((novo_custo, vizinho))
                            D[vizinho] = novo_custo
        print(D)

    def conexidade(self, grafo, no_inicial):
        if len(self.percurso_profundidade(no_inicial)) == self.n:
            return "\nÉ CONEXO  ˗ˏˋ ★ ˎˊ˗"
        else:
            return "\nÉ DESCONEXO  ˗ˏˋ ★ ˎˊ˗"

    def constelacao(self, num_const):
        match num_const:
            case 0:
                return "TERRA"
            case 1:
                return "ARIES"
            case 2:
                return "TOURO"
            case 3:
                return "GEMEOS"
            case 4:
                return "CANCER"
            case 5:
                return "LEAO"
            case 6:
                return "VIRGEM"
            case 7:
                return "LIBRA"
            case 8:
                return "ESCORPIAO"
            case 9:
                return "SAGITARIO"
            case 10:
                return "CAPRICORNIO"
            case 11:
                return "AQUARIO"
            case 12:
                return "PEIXES"

    def percurso_feito(self, num_const):
        for i in num_const:
            msg = ""
            if i == 0:
                msg += "Partindo de "
            else:
                print(" ★ ° ☾ ☆ ¸. ¸ 　★　 :.　 . • ¸ *　:. \n")
                msg += "¸ * . • ¸　. • ¸ :. Agora em "
            msg += self.constelacao(i)
            if i == 0:
                msg += "¸ *　:. . • ¸"
            print(msg)			
        print("\n\nPercurso CONCLUÍDO ˗ˏˋ ★ ˎˊ˗")
