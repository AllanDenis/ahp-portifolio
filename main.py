import numpy as np
from pprint import pprint   

objetivo = ''
criterios = []
alternativas = []

objetivo = input("Decisão a ser tomada: ")

# Critérios
entrada = input("\nCritérios considerados, separados por espaços: ").split()
for crit in entrada:
    criterios.append({
        'nome': crit,
        'peso': float(input("Peso do critério %s na decisão: " % crit))
    })

# Alternativas
entrada = input("\nAlternativas disponíveis, separadas por espaços: ").split()
for alt in entrada:
    alternativas.append({
        'nome': alt,
        'pesos': [
            float(input("%s de %s: " % (crit['nome'], alt)))
            for crit in criterios
        ]
    })


# Matriz alternativa x critério com colunas normalizadas
matrizAltCrit = [alt['pesos'] for alt in alternativas]
matrizAltCrit = np.array(matrizAltCrit)
matrizAltCrit /= matrizAltCrit.sum()

# Critérios normalizadas
rankingCriterios = [crit['peso'] for crit in criterios]
rankingCriterios = np.array(rankingCriterios)
rankingCriterios /= rankingCriterios.sum()
assert(np.sum(rankingCriterios) == 1)

# RESULTADO: ranking de alternativas
rankingAlternativas = matrizAltCrit.dot(rankingCriterios)
rankingAlternativas /= rankingAlternativas.sum()
rankingAlternativas = zip([a['nome'] for a in alternativas], rankingAlternativas)
rankingAlternativas = sorted([(pontos,a)
                        for (a,pontos) in rankingAlternativas],
                        reverse=True)

print("_" * 50 + "\nRanking de alternativas para %s: " % objetivo)
for pontos, alt in rankingAlternativas:
    print("%s: %.1f%%" % (alt, pontos * 100))
