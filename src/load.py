import pandas as pd
import sqlite3
from sqlalchemy import create_engine


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


def salvarSQLite(df: pd.DataFrame, nome_banco: str, nome_tabela: str):

    Conn = sqlite3.connect(nome_banco)

    df.to_sql(nome_tabela, Conn, if_exists="replace", index=False)

    Conn.close()
    return


def salvarMySQL(
    df: pd.DataFrame,
    usuario: str,
    senha: str,
    host: str,
    nome_banco: str,
    nome_tabela: str,
):

    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{nome_banco}")

    df.to_sql(nome_tabela, con=engine, if_exists="replace", index=False)

    return
