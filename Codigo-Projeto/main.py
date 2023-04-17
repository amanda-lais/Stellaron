from grafoMatriz import GrafoMatriz, TGrafoND
from grafoLista import GrafoLista
import time
import os

# GLOBALS -------------------------------------------------
NOME_ARQ = "grafo.txt"

# FUNÇÕES -------------------------------------------------
# Lê o arquivo txt e cria um grafo definido pelo seu tipo
# tipo -> se o grafo é orientado ou não
# t -> se for 0 é sem peso, 1 é com peso
# n -> quantidade de vértices
# m -> quantidade de arestas

def arq_grafo(n_aqr: str, tipo=0):
    # le as duas primeiras linhas para
    # definir o tipo (t) e a quantidade de vertices (n)
    # assim como quantidade de arestas (m)
    try:
        arq = open(n_aqr, 'r')
    except OSError:
        print("O arquivo informado não existe !!")
        return None
    t, n, m = int(arq.readline()), int(arq.readline()), int(arq.readline())
    # Instancia o Grafo
    if tipo == 0 and t == 0:
        grafo = TGrafoND(n, False)
    elif tipo == 0 and t == 1:
        grafo = TGrafoND(n, True)
    elif tipo == 1 and t == 0:
        grafo = GrafoMatriz(n, False)
    else:
        grafo = GrafoMatriz(n, True)
    data = arq.readlines()
    arq.close()
    if t == 1:  # para os rotulados
        for linha in data:
            v, w, valor = linha.split()
            v, w, valor = int(v), int(w), int(valor)
            grafo.insere_a(v, w, valor)
    if t == 0:  # para não rotulados
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
    time.sleep(0.3)
    print(" 00-----1- -- BEM VINDO -- ----1- 0- 0---* - ")
    time.sleep(0.3)
    print(" ---||-, -PROJETO CALLISTO--- 8*)==-  - ---* ")
    time.sleep(0.3)
    print(" -----4242--**& -- - -  - --00 --000  ** 9-( ")
    time.sleep(0.3)
    print(" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* ")
    time.sleep(0.3)
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


def falha():
    print("FALHA NA OPERAÇÃO!! - Grafo inexistente.")


def sucesso():
    print("SUCESSO NA OPERAÇÃO :D")


def op1():
    return str(input("Digite o nome do arquivo: "))


def op2(grafo=None):
    if not grafo:
        return False
    grafo_arq()
    return True


def op3(grafo=None):
    if not grafo:
        return False
    grafo.insere_v(grafo)
    return grafo


def op4(grafo=None):
    if not grafo:
        return False
    v, w = int(input("Informe os vértices que serão interligados (Utilize de espaço para delimitar):\n"))
    if grafo.rotulado:
        p = float(input("Informe o custo da ligação (pode ser em ponto flutuante): "))
        grafo.insere_a(v, w, p)
        return grafo
    grafo.insere_a(v, w)
    return grafo


def op5(grafo):
    if not grafo:
        return False
    v = int(input("Informe qual vértice será removido: "))
    grafo.remover(v)
    return grafo


def op6(grafo):
    if not grafo:
        return False
    v, w = int(input("Informe qual ligação será removida: "))
    grafo.remove_a(v, w)
    return grafo


def op7():
    with open(op1()) as file:
        print(file.read())


def op8(grafo):
    if not grafo:
        return False
    grafo.show()


def menu():
    grafo = None
    saudacoes()
    while True:
        input("\n\n Precione qualquer tecla para continuar...")
        os.system('cls')
        show_opcoes()
        escolha = recebe()
        if escolha == 9:
            print("Até mais, estrelinha *-*")
            return True
        elif escolha == 1:
            grafo = arq_grafo(op1())
            if grafo:
                print("Grafo recuperado de um arquivo")
        elif escolha == 2:
            if not op2(grafo):
                falha()
                continue
            sucesso()
        elif escolha == 3:
            if not grafo:
                falha()
                continue
            grafo = op3(grafo)
            sucesso()
        elif escolha == 4:
            if not grafo:
                falha()
                continue
            grafo = op4(grafo)
        elif escolha == 5:
            if not grafo:
                falha()
                continue
            grafo = op5(grafo)
        elif escolha == 6:
            if not grafo:
                falha()
                continue
            grafo = op6(grafo)
        elif escolha == 7:
            op7()
        elif escolha == 8:
            if not grafo:
                falha()
                continue
            op8(grafo)

# MAIN ----------------------------------------------------
if __name__ == "__main__":
    menu()
