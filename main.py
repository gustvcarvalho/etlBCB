import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQLite, salvarMySQL


dadosBcb = requestApiBcb("20191")

# salvarCsv(dadosBcb, "src/datasets/meiosPagamentosTri.csv", ";", ".")
# ####print(dadosBcb)
# ####dadosBcb.to_csv("meiosPagamentosTri.csv", sep=';', decimal='.')

# salvarSQLite(dadosBcb, "src/datasets/etlbcb.db", "meios_pagamentos_tri")

salvarMySQL(dadosBcb, "root", "root", "localhost", "elebcb", "meios_pagamentos_tri")
