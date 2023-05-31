# Projeto Callisto 🛰

## Introdução 🌌
  * [Apresentação](Documentacao/Apresentação_Intro.ppt)

## Código ⭐
  * [main.py](Codigo-Projeto/main.py)
  * [grafoMatriz.py](Codigo-Projeto/grafoMatriz.py)
  * [grafoLista.py](Codigo-Projeto/grafoLista.py)
  * [Testes.txt](Codigo-Projeto/Textes_txt)
  
## Vídeo ✨

[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/watch?v=IOfozrUjphk)

## Documentação 🌠
  * [Relatório 1 (apenas parte 1 do projeto)](Documentacao/Relatorio-1.md)
  * [Relatório 2 (completo)](Documentacao/Relatorio-2.md)
  * [Testagem ](Documentacao/Testagem.md)
 

## Descrição 🔭

Programa para analisar diversas constelações a partir de um input do usuário, observando quais suas características e padrões. Além disso, analisar rotas entre o planeta Terra e as constelações, inclusive calculando qual seria o caminho mínimo.

Nosso programa é capaz de receber um txt que contenha informações de grafos equivalentes às constelações ou às rotas, sendo eles invariavelmente Não-Direcionados e Rotulados.

Feito na linguagem Python.

## Objetivos do ODS 🪐

Propomos que a civilização humana, no futuro, visite outras galáxias e sistemas solares e, como um plano B caso não consigamos restaurar o planeta, vimos como uma opção nos instaurar em outras galáxias e quais constelações seriam melhores do que as tão conhecidas do zodíaco?

### ODS 9: Inovação infraestrutura – Construir infraestrutura resiliente, promover a industrialização inclusiva e sustentável, e fomentar a inovação.

* Nosso projeto atende os objetivos de infraestrutura resiliente e promove a industrialização inclusiva e sustentável. O quesito de infraestrutura é contemplado pela construção de meios de transporte que sejam capazes de realizar o percurso definido pelo nosso projeto, graças ao seu potencial de obrigar a indústria espacial a construir máquinas capazes de fazerem tais percursos atualmente impossíveis. Já na parte de infraestrutura, ao serem criadas essas máquinas atualmente inexistentes.

### ODS 4: Educação de qualidade – Assegurar a educação inclusiva, e equitativa e de qualidade, e promover oportunidades de aprendizagem ao longo da vida para todos.

* Propomos que as massas tenham uma melhor educação sobre os Cosmos, tendo um maior interesse pelas estrelas para que possamos criar novas gerações mais capacitadas e interessadas no assunto para que possa haver mais pesquisas no futuro, podendo, até, criar mais projetos que impulsionem a humanidade no futuro. Além disso, envisiona-se a identificação de padrões nas características de constelações, de maneira a aprender sobre os jeitos que as constelações foram definidas pelas culturas.

## As Constelações do Zodíaco ♈♊♌♎♐♒♉♋♍♏♑♓

![image](https://user-images.githubusercontent.com/80297158/227752344-90b05733-ed4e-45b7-9197-79259e3de308.png)

## Rotas Espaciais 🚀

**Todas as as distâncias entre as constelações variam em _X_ anos luz, aproximamos todas para facilitar**

- Transformamos as constelações em vértices de um grafo e colocamos as devidas distâncias de uma para outra como as arestas. Nosso objetivo central é criar uma rota onde uma missão poderia visitar todas as 12 principais do zodíaco da maneira mais rápida e barata possível. Para isso, foi utilizado o agoritmo [...]

- [Graph Online](http://graphonline.ru/en/?graph=UDoivsZZSeFRcSxj)

- - Distâncias entre elas e a Terra 🌎

![image](https://github.com/Thiago2204/Projeto-Callisto/assets/80297158/330f9326-82a8-43ef-9707-e6157dc6a0c2)

- - Rota Otimizada 🗺️

![image](https://github.com/Thiago2204/Projeto-Callisto/assets/80297158/2b0fe493-0f43-4713-b023-6fc2dd4f9aff)

- - Matriz da rota otimizada

![image](https://github.com/Thiago2204/Projeto-Callisto/assets/80297158/88f068ad-82c1-4bb3-8ff1-a347b918f519)

## Regras da Montagem 🌟

Constelações:
- Cada constelação deve conter todas as estrelas pertencentes a elas

Rotas:
- Todas as distâncias entre constelações foram implementadas como arestas para facilitar
- Transformamos os grafos de cada constelação em uma única aresta 
- Deve-se visitar todas as constelações ao menos uma vez
