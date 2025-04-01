import pandas as pd 

def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    """
    Função para salvar um DataFrame em um arquivo CSV.

    Parâmetros:
    DataFrame - string - string - string 
    (Exemplo: dadosBcb, "etlBCB/src/datasets/meiosPagamentosTri.csv", ";", ".")
    
    Saída:
    A função apenas salva o arquivo e não retorna valor.
    """

    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return