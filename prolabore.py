from glob import glob
arquivoAssociados = glob("./associados/*.xlsx")
arquivosDados = glob("./dados/*.xlsx")

# Validação dos associados
if(len(arquivoAssociados) > 1):
    print("Só deve existir um arquivo mais atualizado com a lista dos associados")
    exit()

if(len(arquivoAssociados) == 0):
    print("Deve existir um arquivo xlsx dentro da pasta associados contendo a versão mais atualizada dos associados")
    exit()

# Validação dos dados
if(len(arquivosDados) != 2):
    print("Dentro da pasta dados deve existir apenas os dois arquivos do prolabore a ser calculado")
    exit()

import pandas as pd