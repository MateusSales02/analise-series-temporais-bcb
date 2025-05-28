
# 📊 Análise de Séries Temporais - Dados do Banco Central

Este projeto tem como objetivo analisar visualmente indicadores econômicos fornecidos pelo Banco Central do Brasil, utilizando gráficos de séries temporais para observar tendências como o endividamento e o comprometimento de renda das famílias brasileiras ao longo do tempo.

A aplicação foi desenvolvida em **Python** com o framework **Flask**, utilizando **Pandas** para tratamento de dados e **Matplotlib** para geração dos gráficos.

---

## 🚀 Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- HTML + CSS puro (sem frameworks externos)

---

## 📷 Funcionalidades

- 📈 **Gráfico individual** da série 29038 (endividamento exceto crédito habitacional)
- 📊 **Gráfico comparativo** com as séries:
  - 29038 – Endividamento exceto crédito habitacional
  - 29034 – Comprometimento com serviço da dívida
  - 29036 – Comprometimento com juros da dívida
  - 29037 – Endividamento total com crédito habitacional
- ✅ Interface web com explicação do gráfico + interpretação da tendência

---

## 📁 Estrutura do Projeto

```
N2_Camargo/
├── app.py                 # Código principal com Flask
├── dataset/               # Arquivos .csv das séries
│   ├── bcdata.sgs.29034.csv
│   ├── bcdata.sgs.29036.csv
│   ├── bcdata.sgs.29037.csv
│   └── bcdata.sgs.29038.csv
├── static/
│   └── plots/             # Gráficos gerados (.png)
├── templates/
│   └── index.html         # Template HTML com layout visual
└── requirements.txt       # Lista de dependências do projeto
```

---

## 🧪 Como Executar Localmente

### 1. Clone este repositório

```bash
git clone https://github.com/MateusSales02/analise-series-temporais-bcb.git
cd analise-series-temporais-bcb
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação

```bash
python app.py
```

### 4. Acesse no navegador

```
http://127.0.0.1:5000
```

---

## 🗃️ Fontes dos Dados

Os dados utilizados neste projeto foram obtidos no portal oficial de [Dados Abertos do Banco Central do Brasil](https://dadosabertos.bcb.gov.br/):

| Código | Descrição |
|--------|-----------|
| 29038  | Endividamento exceto crédito habitacional |
| 29034  | Comprometimento com serviço da dívida |
| 29036  | Comprometimento com juros da dívida |
| 29037  | Endividamento total com crédito habitacional |

Os arquivos foram baixados no formato `.csv` e tratados automaticamente pelo sistema.

---

## 🖼️ Exemplo da Interface

### Gráfico 1 — Endividamento exceto crédito habitacional

> Exibe a evolução do endividamento das famílias sem considerar o crédito habitacional, com interpretação automatizada da tendência.

### Gráfico 2 — Comparativo entre as séries

> Compara quatro séries temporais no mesmo gráfico, permitindo observar discrepâncias e correlações ao longo do tempo.

---

## 📜 Licença

Projeto acadêmico desenvolvido para fins educacionais, sem fins comerciais.  
Distribuição e uso livre com atribuição.

---

## 👨‍💻 Autor

**Mateus Oliveira**  
Projeto desenvolvido para a disciplina de **Análise de Séries Temporais**.
