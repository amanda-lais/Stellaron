import util

grafo = util.arq_grafo("grafo.txt", 1)
grafo.show_min()
print(grafo.ordenacao_topologica(0))
