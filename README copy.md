# ETL com dados do Banco Central - Projeto de Data Science

Durante o semestre 2025.2, desenvolvi este projeto como parte da disciplina de Data Science no curso de Análise e Desenvolvimento de Sistemas do Senac-PE, sob a orientação do professor Marcos Mialaret.

O objetivo do projeto foi praticar e aprofundar conceitos de ETL (Extract, Transform, Load) utilizando dados reais de meios de pagamento trimestrais fornecidos pela API do Banco Central do Brasil, incluindo informações sobre PIX, cartões, entre outros.

---

## Tecnologias e Ferramentas

- **Linguagem:** Python 3.x  
- **Bibliotecas:** pandas, requests, sqlalchemy, sqlite3, pymysql  
- **Ambiente virtual:** venv  
- **Banco de dados:** SQLite (local) e MySQL (opcional)  
- **Outros:** Jupyter Notebooks para análise exploratória e relatórios  

---

## Estrutura do Repositório

├── aulas/ # Material e exercícios introdutórios sobre pandas
├── src/ # Código-fonte do projeto
│ ├── init.py
│ ├── pycash.py # Funções de Extract e Transform
│ ├── load.py # Funções para salvar dados em CSV, SQLite e MySQL
│ └── datasets/ # Dados transformados e base para carga
├── notebooks/ # Jupyter Notebooks com análises e relatórios
│ ├── uso_cartoes.ipynb
│ └── analise_pix.ipynb
├── .gitignore
├── LICENSE
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
└── venv/ # Ambiente virtual (não versionado)


---

## Funcionalidades principais

### Extract & Transform
- A função `requestApiBcb(data: str) -> pd.DataFrame` realiza a extração dos dados da API do Banco Central para um trimestre específico.
- Os dados extraídos são convertidos em DataFrames pandas e têm suas colunas ajustadas, incluindo conversão de datas.

### Load
- `salvarCsv()` grava DataFrames em arquivos CSV com separadores e formatos configuráveis.
- `salvarSQLite()` insere dados em um banco SQLite local.
- `salvarMySQL()` possibilita carga em banco MySQL remoto, usando SQLAlchemy e pymysql.

---

## Como usar

1. Clone este repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DIRETORIO>

2. Crie e ative o ambiente virtual:

python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Execute o script de extração e transformação para obter os dados do trimestre desejado:

from src.pycash import requestApiBcb
dados = requestApiBcb("20221")  # Exemplo: primeiro trimestre de 2022

5. Salve os dados no formato desejado, por exemplo CSV ou SQLite:

from src.load import salvarCsv, salvarSQLite

salvarCsv(dados, "src/datasets/meiosPagamentosTri.csv", ";", ".")
salvarSQLite(dados, "src/datasets/etlbcb.db", "meios_pagamentos_tri")

6. Use os notebooks para análises exploratórias e geração de relatórios.

## Considerações finais

Este projeto serviu como uma experiência prática para fixar conceitos de ETL e manipulação de dados com Python e pandas, além de fornecer uma base para aplicações futuras envolvendo integração de APIs e análise de dados financeiros.

## Dicionário de Dados

### Meios de Pagamentos Trimestrais
Conjunto de informações sobre operações com cartões de pagamento e de transferências de crédito (boletos bancários, cartões de crédito e débito, transferências bancárias). Dados ficam disponíveis 90 dias após o final do trimestre.

### Parâmetros

| Nome         | Tipo     | Título   | Descrição                                                                 |
|--------------|----------|----------|---------------------------------------------------------------------------|
| trimestre    | texto    | Trimestre| Os dados serão trazidos a partir do tri forn como parâmetro no form AAAAT. |
| $format      | texto    | $format  | Tipo de conteúdo que será retornado.                                      |
| $select      | texto    | $select  | Propriedades que serão retornadas.                                        |
| $filter      | texto    | $filter  | Filtro de seleção de entidades. Exemplo: Nome eq 'João'.                  |
| $orderby     | texto    | $orderby | Propriedades para ordenação das entidades. Exemplo: Nome asc, Idade desc. |
| $skip        | inteiro  | $skip    | Índice (maior ou igual a zero) da primeira entidade que será retornada.   |
| $top         | inteiro  | $top     | Número máximo (maior que zero) de entidades que serão retornadas.        |


### Resultado

| Nome                         | Tipo     | Título                        | Descrição                                                                                                           |
|------------------------------|----------|-------------------------------|---------------------------------------------------------------------------------------------------------------------|
| datatrimestre                | texto    | Trimestre                     |                                                                                                                     |
| valorPix                     | decimal  | Valor Pix                     | Volume financeiro (R$ milhões) de transações Pix liquidadas trimestralmente no SPI e fora do SPI, considerando ordens de pagamento e devoluções no período. |
| valorTED                     | decimal  | Valor TED                     | Montante financeiro (R$ milhões) trimestral transferido por meio de TED.                                           |
| valorTEC                     | decimal  | Valor TEC                     | Montante financeiro (R$ milhões) trimestral transferido por meio de TEC.                                           |
| valorCheque                  | decimal  | Valor Cheque                  | Montante financeiro (R$ milhões) de cheques interbancários e intrabancários compensados trimestralmente.           |
| valorBoleto                  | decimal  | Valor Boleto                  | Montante financeiro (R$ milhões) de boletos interbancários e intrabancários compensados trimestralmente.           |
| valorDOC                     | decimal  | Valor DOC                     | Montante financeiro (R$ milhões) trimestral transferido por meio de DOC.                                           |
| valorCartaoCredito           | decimal  | Valor Cartão de Crédito       | Valor (R$ milhões) de transações realizadas com cartão de crédito.                                                 |
| valorCartaoDebito            | decimal  | Valor Cartão de Débito        | Valor (R$ milhões) de transações realizadas com cartão de débito trimestralmente.                                  |
| valorCartaoPrePago           | decimal  | Valor Cartão Pré-pago         | Valor (R$ milhões) de transações realizadas com cartão pré-pago trimestralmente.                                    |
| valorTransIntrabancaria      | decimal  | Valor Transferência Intrabancária | Montante financeiro (R$ milhões) de transferências realizadas trimestralmente entre contas de clientes da Instituição. |
| valorConvenios               | decimal  | Valor Convênio                | Montante financeiro (R$ milhões) referente a arrecadações trimestrais governamentais e não-governamentais.          |
| valorDebitoDireto            | decimal  | Valor Débito Direto           | Montante financeiro (R$ milhões) trimestral referente a débitos previamente autorizados pelo cliente em sua conta corrente. |
| valorSaques                  | decimal  | Valor Saque                   | Montante sacado (R$ milhões) nos caixas eletrônicos trimestralmente.                                                |
| quantidadePix                | decimal  | Quantidade Pix                | Quantidade (em milhares) de transações Pix liquidadas trimestralmente no SPI e fora do SPI.                        |
| quantidadeTED                | decimal  | Quantidade TED                | Quantidade (em milhares) de TED realizadas trimestralmente.                                                        |
| quantidadeTEC                | decimal  | Quantidade TEC                | Quantidade (em milhares) de TEC realizadas trimestralmente.                                                        |
| quantidadeCheque             | decimal  | Quantidade Cheque             | Quantidade (em milhares) de cheques interbancários e de cheques intrabancários compensados trimestralmente.        |
| quantidadeBoleto             | decimal  | Quantidade Boleto             | Quantidade (em milhares) de cheques interbancários e intrabancários compensados trimestralmente.                   |
| quantidadeDOC                | decimal  | Quantidade DOC                | Quantidade (em milhares) de DOC realizados trimestralmente.                                                        |
| quantidadeCartaoCredito      | decimal  | Quantidade Cartão de Crédito  | Quantidade (em milhares) de transações realizadas com cartão de crédito trimestralmente.                           |
| quantidadeCartaoDebito       | decimal  | Quantidade Cartão de Débito   | Quantidade (em milhares) de transações realizadas com cartão de débito trimestralmente.                            |
| quantidadeCartaoPrePago      | decimal  | Quantidade Cartão Pré-pago    | Quantidade (em milhares) de transações realizadas com cartão pré-pago trimestralmente.                             |
| quantidadeTransIntrabancaria | decimal  | Quantidade de Transferência Intrabancária | Quantidade (em milhares) de transferências realizadas trimestralmente entre contas de clientes da Instituição.    |
| quantidadeConvenios          | decimal  | Quantidade Convênio           | Quantidade (em milhares) de transações realizadas referentes a arrecadações trimestrais governamentais e não-governamentais. |
| quantidadeDebitoDireto       | decimal  | Quantidade Débito Direto      | Quantidade (em milhares) de transações trimestrais referente a débitos previamente autorizados pelo cliente.       |
| quantidadeSaques             | decimal  | Quantidade de Saque           | Quantidade (em milhares) de saques realizados nos caixas eletrônicos trimestralmente.                              |



