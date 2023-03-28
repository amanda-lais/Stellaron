from grafoMatriz import GrafoMatriz, TGrafoND
from grafoLista import GrafoLista
import time

# GLOBALS -------------------------------------------------
NOME_ARQ = "grafo.txt"


# FUNÇÕES -------------------------------------------------

# Lê o arquivo txt e cria um grafo definido pelo seu tipo
# tipo -> se o grafo é orientado ou não
# t -> se for 0 é sem peso, 1 é com peso
# n -> quantidade de vértices
# m -> quantidade de arestas
def arq_grafo(n_aqr: str, tipo=0):
    with open(n_aqr, 'r') as arq:
        # le as duas primeiras linhas para
        # definir o tipo (t) e a quantidade de vertices (n)
        # assim como quantidade de arestas (m)
        t, n, m = arq.readline(), int(arq.readline()), int(arq.readline())

        # Instancia o Grafo
        if tipo == 0 and t == '0':
            grafo = TGrafoND(n, False)
        elif tipo == 0 and t == '1':
            grafo = TGrafoND(n, True)
        elif tipo == 1 and t == '0':
            grafo = GrafoMatriz(n, False)
        else:
            grafo = GrafoMatriz(n, True)

        data = arq.readlines()

    if t == '1':  # para os rotulados
        for linha in data:
            v, w, valor = linha.split()
            v, w, valor = int(v), int(w), int(valor)
            grafo.insere_a(v, w, valor)

    if t == '0':  # para não rotulados
        for linha in data:
            v, w = linha.split()
            v, w = int(v), int(w)
            grafo.insere_a(v, w)

    return grafo


def grafo_arq(n_arq="grafo.txt"):
    pass


def converter_ml(original: GrafoMatriz) -> GrafoLista:
    gl = GrafoLista(original.n)

    for v in range(0, original.n):
        for w in range(0, original.n):
            if original.adj[v][w] == 1:
                gl.insere_a(v, w)
    return gl


def saudacoes():
    print(" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ")
    print(" 00-----1- -- BEM VINDO -- ----1- 0- 0---* - ")
    print(" ---||-, -PROJETO CALLISTO--- 8*)==-  - ---* ")
    print(" -----4242--**& -- - -  - --00 --000  ** 9-( ")
    print(" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ")
    print("\n")


def show_opcoes():
    print("|  --------------  Opções  ---------------- -")
    print("|  1) Ler dados de um arquivo txt           |")
    print("|  2) Gravar dados no arquivo txt           |")
    print("|  3) Inserir vértice                       |")
    print("|  4) Inserir aresta                        |")
    print("|  5) Remover vértice                       |")
    print("|  6) Remover aresta                        |")
    print("|  7) Mostrar conteúdo do arquivo           |")
    print("|  8) Mostrar grafo                         |")
    print("|  9) Encerrar a aplicação            x.x   |")


def recebe() -> int:
    return int(input("| - Escolha uma das opções acima: "))


# 1 -> grafo; 2 -> 1; 3 -> 1/-1; 4 -> 1/-1; 5 -> 1/-1
def menu(grafo=None):
    saudacoes()
    show_opcoes()
    escolha = recebe()
    if escolha == 1:
        nome_arq = str(input("Qual o nome do arquivo?  "))
        return arq_grafo(nome_arq)
    elif escolha == 2:
        grafo_arq()
        return 1
    elif escolha == 3:
        if not grafo:
            print("ERROR Z_Z  --- Não há grafo existente")
            return -1
        grafo.insere_v()
        return grafo
    elif escolha == 4:
        if not grafo:
            print("ERROR Z_Z  --- Não há grafo existente")
            return -1
        print("Informe quais vértices serão ligados: ")
        v, w = int(input())
        if grafo.rotulado:
            valor = float(input("Qual o peso desta ligação?   "))
            grafo.insere_a(v, w, valor)
        else:
            grafo.insere_a(v, w)
        return grafo
    elif escolha == 5:
        if not grafo:
            print("ERROR Z_Z  --- Não há grafo existente")
            return -1
        v = int(input("Qual vértice será removido:  "))
        grafo.remover(v)
        return grafo
    elif escolha == 6:
        if not grafo:
            print("ERROR Z_Z  --- Não há grafo existente")
            return -1
        v, w = int(input("Qual aresta será removida (informe um par):  "))
        grafo.remove_a(v, w)
        return grafo
    elif escolha == 7:
        print(" | A IMPRESSÃO DO ARQUIVO É COMO SE SEGUE | ")
        with open(NOME_ARQ, 'r') as arq:
            for line in arq:
                print(f"{line}", end="")
        return 1
    elif escolha == 8:
        if not grafo:
            print("ERROR Z_Z  --- Não há grafo existente")
            return -1
        grafo.show_min()
    elif escolha == 9:
        print("Até mais, estrelinha -w-")
        exit()


# MAIN ----------------------------------------------------
if __name__ == "__main__":
    retorno = menu()
    grafo_existe = False
    while True:
        if type(retorno) == TGrafoND or type(retorno) == GrafoMatriz:
            grafo_existe = True
        if grafo_existe:
            retorno = menu(retorno)
        else:
            retorno = menu()



