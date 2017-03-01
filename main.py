import numpy as np
from pprint import pprint

objetivo = ''
criterios = []
alternativas = []
criteriosComp = []
alternativasComp = []

entrada = input("Digite os critérios, separados por espaços: ")
criterios = entrada.split()
criteriosComp = np.zeros((len(criterios), len(criterios)))


entrada = input("Digite as alternativas, separadas por espaços: ")
alternativas = entrada.split()
alternativasComp = np.zeros((len(alternativas), len(alternativas)))
pprint(criteriosComp)
pprint(alternativasComp)
