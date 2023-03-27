from grafoMatriz import GrafoMatriz
from grafoLista import GrafoLista

# GLOBALS -------------------------------------------------
NOME_ARQ = "sim.txt"


# FUNÇÕES -------------------------------------------------
################################
##  main.py: exes 7, 13 e 18  ##
################################
# grafoLista.py: exes 12, 14, 15, 16, 17, 20
# grafoMatriz.py: exes 1, 2, 3, 4, 5, 6, 8, 9, 10, 11

# EX7 e EX18 --- Ler de um arquivo e criar o grafo - ry
def arq_grafo(n_aqr: str, tipo=0):
    with open(n_aqr, 'r') as arq:
        v, a = arq.readline(), arq.readline()
        data = arq.readlines()
    if tipo == 0:  # para matriz
        grafo = GrafoMatriz(int(v))
    if tipo == 1:  # para lista
        grafo = GrafoLista(int(v))
    for linha in data:
        v, a = linha.split()
        v, a = int(v), int(a)
        grafo.insere_a(v, a)
    return grafo


# EX13 --- Converte grafo - ry
def converter_ml(original: GrafoMatriz) -> GrafoLista:
    gl = GrafoLista(original.n)

    for v in range(0, original.n):
        for w in range(0, original.n):
            if original.adj[v][w] == 1:
                gl.insere_a(v, w)
    return gl


# MAIN ----------------------------------------------------
if __name__ == "__main__":
    g = arq_grafo(NOME_ARQ)
    g.show()
