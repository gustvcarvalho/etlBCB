# 📊 Análise de Meios de Pagamento no Brasil — Projeto Data Science (2025.2)

Este projeto foi desenvolvido como parte da disciplina de Data Science do curso de Análise e Desenvolvimento de Sistemas do Senac-PE, sob orientação do professor Marcos Mialaret, no semestre 2025.2.

O foco principal foi construir um pipeline de ETL (Extract, Transform, Load) utilizando Python e dados abertos do Banco Central do Brasil, com o objetivo de entender a evolução trimestral de meios de pagamento como PIX, cartões, boletos e outros, além de aplicar técnicas de modelagem preditiva e visualização.

## 📁 Estrutura do Projeto

```
ETLBCB/
├── assets/                  # Dashboards
├── materials/               # Slides da aula e material de apoio
├── notebooks/               # Jupyter Notebooks com as análises
├── reports/powerbi/        # Análises Power BI
├── src/                    # Código-fonte principal do projeto
│   ├── datasets/           # Arquivos de dados brutos e processados
│   ├── extractTransform.py # Extração e transformação dos dados
│   ├── load.py             # Carregamento dos dados
├── main.py                 # Script principal de execução
├── requirements.txt        # Bibliotecas Python necessárias
├── README.md               # Este arquivo
```

## 🚀 Tecnologias Utilizadas

- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- scikit-learn, prophet
- SQLite
- Power BI
- Jupyter Notebook

## 📊 Fontes de Dados

Os dados foram obtidos por meio da [API do Banco Central do Brasil (BCB)](https://dadosabertos.bcb.gov.br/), especificamente do conjunto **Meios de Pagamento Trimestrais**, que contém informações sobre:

- Transações com Pix, boletos, cartões (crédito, débito, pré-pago), cheques, TED, DOC, TEC, etc.
- Volume financeiro (em milhões de reais)
- Quantidade de transações (em milhares)

## 📌 Etapas Desenvolvidas

1. **Coleta de Dados**:
   - Através da API OData do BCB, com filtros e seleções específicas.

2. **ETL** (`src/`):
   - Scripts `extractTransform.py` e `load.py` realizam a limpeza, transformação e carregamento dos dados.

3. **Análise Exploratória** (`notebooks/`):
   - Identificação de tendências, sazonalidades e mudanças nos meios de pagamento.

4. **Modelagem Preditiva**:
   - Previsões com `Prophet` e `Random Forest` para tendências em pagamentos eletrônicos.

5. **Relatórios**:
   - Visualizações em Power BI e gráficos em Jupyter Notebook.

## ▶️ Como Executar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ETLBCB.git
   cd ETLBCB
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate   # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script principal:
   ```bash
   python main.py
   ```

5. Explore os notebooks na pasta `notebooks/`.

## 🗂️ Dicionário de Dados

### Meios de Pagamentos Trimestrais

Conjunto de informações sobre operações com cartões de pagamento e de transferências de crédito (boletos bancários, cartões de crédito e débito, transferências bancárias). Dados ficam disponíveis 90 dias após o final do trimestre.

### Parâmetros da API

| Nome         | Tipo     | Título   | Descrição |
|--------------|----------|----------|-----------|
| trimestre    | texto    | Trimestre| AAAAT (ex: 2023T1) |
| $format      | texto    | $format  | Tipo de conteúdo retornado |
| $select      | texto    | $select  | Propriedades desejadas |
| $filter      | texto    | $filter  | Filtro de entidades |
| $orderby     | texto    | $orderby | Ordenação |
| $skip        | inteiro  | $skip    | Índice inicial |
| $top         | inteiro  | $top     | Nº máx. de registros |

### Campos do Resultado

| Nome                         | Tipo     | Descrição |
|------------------------------|----------|-----------|
| datatrimestre                | texto    | Trimestre (AAAAT) |
| valorPix                     | decimal  | Volume financeiro de transações Pix (R$ milhões) |
| valorTED                     | decimal  | Volume TED (R$ milhões) |
| valorTEC                     | decimal  | Volume TEC (R$ milhões) |
| valorCheque                  | decimal  | Volume de cheques compensados |
| valorBoleto                  | decimal  | Volume de boletos compensados |
| valorDOC                     | decimal  | Volume DOC |
| valorCartaoCredito           | decimal  | Valor em cartão de crédito |
| valorCartaoDebito            | decimal  | Valor em cartão de débito |
| valorCartaoPrePago           | decimal  | Valor em cartão pré-pago |
| valorTransIntrabancaria      | decimal  | Transferências dentro da mesma instituição |
| valorConvenios               | decimal  | Arrecadações de convênios |
| valorDebitoDireto            | decimal  | Débitos autorizados (R$ milhões) |
| valorSaques                  | decimal  | Saques em caixas eletrônicos |
| quantidadePix                | decimal  | Quantidade de transações Pix (milhares) |
| quantidadeTED                | decimal  | Quantidade de TED |
| quantidadeTEC                | decimal  | Quantidade de TEC |
| quantidadeCheque             | decimal  | Quantidade de cheques compensados |
| quantidadeBoleto             | decimal  | Quantidade de boletos compensados |
| quantidadeDOC                | decimal  | Quantidade DOC |
| quantidadeCartaoCredito      | decimal  | Qtd. de transações cartão crédito |
| quantidadeCartaoDebito       | decimal  | Qtd. de transações cartão débito |
| quantidadeCartaoPrePago      | decimal  | Qtd. de transações cartão pré-pago |
| quantidadeTransIntrabancaria | decimal  | Qtd. de transferências intrabancárias |
| quantidadeConvenios          | decimal  | Qtd. de convênios |
| quantidadeDebitoDireto       | decimal  | Qtd. de débitos diretos |
| quantidadeSaques             | decimal  | Qtd. de saques |

---

Desenvolvido por Gustavo Carvalho · Senac-PE · 2025.2 · Data Science
