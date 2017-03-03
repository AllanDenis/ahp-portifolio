import numpy as np
from collections import OrderedDict
from pprint import pprint
from itertools import combinations
from fractions import Fraction

def matrizComp(itens):
    numItens = len(itens)
    itensComp = np.ones((numItens, numItens))
    pares = combinations(range(numItens), 2)
    for p1,p2 in pares:
        entrada = input("Relação entre %s e %s: " % (itens[p1], itens[p2]))
        itensComp[p1][p2] = Fraction(entrada)

    # Preenchimento da matriz triangular
    itensComp = np.triu(itensComp, k=1) +\
                np.triu(np.reciprocal(itensComp)).T
    # Normalização das colunas
    itensComp /= itensComp.sum(axis=0)
    return itensComp

def vetorPrioridade(matriz):
    return matriz.mean(axis=1)

objetivo = ''
criterios = []
alternativas = []
criteriosComp = []
alternativasComp = []

# Critérios
entrada = input("Digite os critérios, separados por espaços: ")
criterios = entrada.split()
criteriosComp = matrizComp(criterios)

# Vetor de prioridade
prioridades = vetorPrioridade(criteriosComp)

for criterio,peso in zip(criterios, prioridades):
    print("Peso do critério %s: %d%%" % (criterio, int(peso * 100)))


# Alternativas
entrada = input("Digite as alternativas, separadas por espaços: ")
alternativas = enumerate(entrada.split())
alternativas = [(b,a) for a,b in alternativas]
alternativas = OrderedDict(alternativas)
for alt in alternativas:
    pprint(alt)
    for crit in criterios:
         alternativas[alt][crit] = input("\n%s quanto ao critério %s:" %\
                                        (alt, crit))
    # alternativasComp.append(matrizComp(alternativas))

pprint(alternativas)
