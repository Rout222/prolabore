import re
def pegarDados(associados, nome, pa):
    colunas = associados.columns
    df = associados[[colunas[nome], colunas[pa]]]
    return df.values.tolist()

def prepararPAS(associados, pa):
    colunas = associados.columns
    PAS = {'RATEIO' : 0.0}
    for x in associados[colunas[pa]].unique().tolist():
        PAS[x] = 0.0
    return PAS

def processaNome(nome):
    try:
        return re.sub("\d", "", nome).strip().upper()
    except E:
        return ""

    