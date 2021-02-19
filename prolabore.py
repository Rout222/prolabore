from glob import glob
arquivoAssociados = glob("./associados/*.xlsx")
arquivosDados = glob("./dados/*.xlsx")

# Validação dos associados
if(len(arquivoAssociados) > 1):
    print("Só deve existir um arquivo mais atualizado com a lista dos associados")
    input("Aperte qualquer tecla pra sair...")
    exit()

if(len(arquivoAssociados) == 0):
    print("Deve existir um arquivo xlsx dentro da pasta associados contendo a versão mais atualizada dos associados")
    input("Aperte qualquer tecla pra sair...")
    exit()

# Validação dos dados
if(len(arquivosDados) != 2):
    print("Dentro da pasta dados deve existir apenas os dois arquivos do prolabore a ser calculado")
    input("Aperte qualquer tecla pra sair...")
    exit()

import pandas as pd

associados = pd.read_excel(
    arquivoAssociados[0],
)
print("Essas são as colunas que foram lidas do arquivo (unnamed são colunas sem título)")
for i, coluna in enumerate(associados.columns):
    print(f'[{i}] - {coluna}')

associadosNomeColuna = int(input("Digite o número da coluna dos nomes dos associados: "))
associadosPAColuna = int(input("Digite o número da coluna dos PA: "))

import funcoes
PAS = funcoes.prepararPAS(associados, associadosPAColuna)
associados = funcoes.pegarDados(associados, associadosNomeColuna, associadosPAColuna)

for arquivo in arquivosDados:
    print(f'Essas são as colunas que foram lidas do arquivo {arquivo} (unnamed são colunas sem título)')
    arquivo = pd.read_excel(arquivo)
    for i, coluna in enumerate(arquivo.columns):
        print(f'[{i}] - {coluna}')

    arquivoNomeColuna = int(input("Digite o número da coluna dos nomes dos associados: "))
    arquivoProlaboreColuna = int(input("Digite o número da valor a ser somado do prolabore: "))
    arquivo = funcoes.pegarDados(arquivo, arquivoNomeColuna, arquivoProlaboreColuna)

    for pessoa in arquivo:
        pa = 'RATEIO'
        for associado in associados:
            if(funcoes.processaNome(pessoa[0]) == funcoes.processaNome(associado[0])):
                pa = associado[1]
        try:
            PAS[pa] += pessoa[1]
        except:
            pass

print("...")
print("...")
print("...")
print("PROCESSADO")
for pa in PAS:
    print(f'3096_{pa} = {PAS[pa]}')
input("Aperte enter pra sair")