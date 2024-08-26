'''Faça um script em Python para calcular quantas ferraduras são necessárias para equipar todos os cavalos comprados para um haras.'''
def ferradura(cavalos):
    qts_ferraduras = cavalos * 4
    return qts_ferraduras

cavalos = int(input('Indique a quantidade comprada de cavalos: '))

ferraduras = ferradura(cavalos)

print(f'A quantidade de ferraduras necessárias é {ferraduras}')
