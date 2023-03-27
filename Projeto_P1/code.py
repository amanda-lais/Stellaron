import os
import xml.etree.ElementTree as ET

# Define o nome do arquivo
filename = "grafo.xml"

# faz a checagem se o arquivo existe e o cria, caso n
if not os.path.isfile(filename):
    raiz = ET.Element("grafo")
    arvore = ET.Elementarvore(raiz)
    arvore.write(filename)

# Faz a leitura dos dados do arquivo
def leia_dados():
    arvore = ET.parse(filename)
    raiz = arvore.getroot()
    return ET.destring(raiz, encoding="unicode")

# Faz a gravacao de dados no arquivo 
def grava_dados(data):
    arvore = ET.parse(filename)
    raiz = arvore.getroot()
    if data.tag not in [filho.tag for filho in raiz]:
        raiz.append(data)
    arvore.write(filename)

# Insere um vertice no grafo
def insere_vertice(vertice):
    raiz = ET.Element("vertice", {"name": vertice})
    grava_dados(raiz)

# Insere arestas no grafo
def insere_aresta(vertice1, vertice2):
    raiz = ET.Element("aresta", {"para": vertice1, "de": vertice2})
    grava_dados(raiz)

# Remove vertice do grafo
def remove_vertice(vertice):
    arvore = ET.parse(filename)
    raiz = arvore.getroot()
    for filho in raiz:
        if filho.tag == "vertice" and filho.attrib["name"] == vertice:
            raiz.remove(filho)
    arvore.write(filename)

# Remove arestas do grafo
def remove_aresta(vertice1, vertice2):
    arvore = ET.parse(filename)
    raiz = arvore.getroot()
    for filho in raiz:
        if filho.tag == "aresta" and filho.attrib["para"] == vertice1 and filho.attrib["de"] == vertice2:
            raiz.remove(filho)
        elif filho.tag == "aresta" and filho.attrib["para"] == vertice2 and filho.attrib["de"] == vertice1:
            raiz.remove(filho)
    arvore.write(filename)

# Mostra o contedo do arquivo 
def Exibe_cont_arquivo():
    print(leia_dados())

# Exibe o Grafo
def show_grafo():
    arvore = ET.parse(filename)
    raiz = arvore.getroot()
    grafo = {}
    for filho in raiz:
        if filho.tag == "vertice":
            grafo[filho.attrib["name"]] = []
    for filho in raiz:
        if filho.tag == "aresta":
            grafo[filho.attrib["para"]].append(filho.attrib["de"])
            grafo[filho.attrib["de"]].append(filho.attrib["para"])
    print(grafo)

# Encerra a aplicação
def close_app():
    exit()

# Main loop
while True:
    print("1. Digite o vértice")
    print("2. Digite a aresta")
    print("3. Remove o vértice")
    print("4. Remove a aresta")
    print("5. Exibe o conteúdo do arquivo")
    print("6. Exibe o grafo")
    print("7. Encerra a aplicação")
    choice = int(input("Digite sua escolha: "))
    if choice == 1:
        vertice = input("Digite o vertice a ser inserido: ")
        insere_vertice(vertice)
    elif choice == 2:
        vertice1 = input("Digite o primeiro vertice: ")
        vertice2 = input("Digite o segundo vertice: ")
        insere_aresta(vertice1, vertice2)
    elif choice == 3:
        vertice = input("Digite o vertice para ser removido: ")
        remove_vertice(vertice)
    elif choice == 4:
        vertice1 = input("Digite o primeiro vertice: ")
        vertice2 = input("Digite o segundo vertice: ")
        remove_aresta(vertice1, vertice2)
    elif choice == 5:
        Exibe_cont_arquivo()
