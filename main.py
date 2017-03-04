import numpy as np

objetivo = ''
criterios = []
alternativas = []

objetivo = input("Decisão a ser tomada: ")

# Critérios
entrada = input("Critérios considerados, separados por espaços: ").split()
for crit in entrada:
    criterios.append({
        'nome': crit,
        'peso': float(input("Peso do critério %s na decisão: " % crit))
    })

# Alternativas
entrada = input("Alternativas disponíveis, separadas por espaços: ").split()
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
matrizAltCrit = np.array(matrizAltCrit).T
for coluna in matrizAltCrit:
    coluna /= sum(coluna)
matrizAltCrit = matrizAltCrit.T

# Critérios normalizadas
rankingCriterios = [crit['peso'] for crit in criterios]
rankingCriterios = np.array(rankingCriterios)
rankingCriterios /= sum(rankingCriterios)

# RESULTADO: ranking de alternativas
rankingAlternativas = matrizAltCrit.dot(rankingCriterios)
rankingAlternativas = zip([a['nome'] for a in alternativas], rankingCriterios)
rankingAlternativas = sorted([(pontos,alt)
                        for (alt,pontos) in rankingAlternativas],
                        reverse=True)

print("Ranking de alternativas para %s: " % objetivo)
for pontos, alt in rankingAlternativas:
    print("%s: %.1f%%" % (alt, pontos * 100))
