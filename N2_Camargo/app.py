from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

DATASET_PATH = 'dataset'
PLOTS_PATH = 'static/plots'

datasets = {
    "Endividamento exceto crédito habitacional (29038)": "bcdata.sgs.29038.csv",
    "Comprometimento com serviço da dívida (29034)": "bcdata.sgs.29034.csv",
    "Comprometimento com juros da dívida (29036)": "bcdata.sgs.29036.csv",
    "Endividamento total com crédito habitacional (29037)": "bcdata.sgs.29037.csv"
}

explicacoes = {
    "29038": "Este dataset mostra a porcentagem de endividamento das famílias com o Sistema Financeiro Nacional, excluindo crédito habitacional.",
    "29034": "Refere-se ao comprometimento da renda familiar com o serviço total da dívida, incluindo amortização e juros.",
    "29036": "Indica quanto da renda das famílias está comprometida apenas com os juros da dívida.",
    "29037": "Este dataset inclui o crédito habitacional no cálculo do endividamento total das famílias com o SFN."
}

interpretacoes = {
    "29038": "Observa-se uma tendência crescente, indicando que as famílias estão se endividando mais fora do crédito habitacional.",
    "29034": "Há um crescimento constante no comprometimento com o serviço da dívida, sugerindo maior pressão financeira.",
    "29036": "A linha demonstra oscilações com leve tendência de crescimento, refletindo aumento na carga de juros.",
    "29037": "Confirma o padrão de aumento geral do endividamento quando incluímos o crédito habitacional."
}

def gerar_graficos():
    if os.path.exists(PLOTS_PATH) and not os.path.isdir(PLOTS_PATH):
        os.remove(PLOTS_PATH)
    os.makedirs(PLOTS_PATH, exist_ok=True)

    #EX1
    try:
        arquivo = datasets["Endividamento exceto crédito habitacional (29038)"]
        caminho = os.path.join(DATASET_PATH, arquivo)
        df = pd.read_csv(caminho, sep=';', parse_dates=['data'], dayfirst=True)
        df.columns = ['Data', 'Valor']
        df['Valor'] = df['Valor'].str.replace(',', '.').astype(float)
        df = df.sort_values('Data')

        plt.figure(figsize=(10, 4))
        plt.plot(df['Data'], df['Valor'], label="Endividamento exceto crédito habitacional (29038)")
        plt.title("Endividamento exceto crédito habitacional (29038)")
        plt.xlabel('Ano')
        plt.ylabel('Percentual (%)')
        plt.grid(True)
        plt.tight_layout()
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(PLOTS_PATH, 'grafico_29038.png'))
        plt.close()
        print("Gráfico individual 29038 salvo.")

    except Exception as e:
        print(f"Erro ao gerar gráfico individual 29038: {e}")

    # Ex2
    plt.figure(figsize=(12, 5))
    for nome, arquivo in datasets.items():
        codigo = arquivo.split('.')[2]
        try:
            caminho = os.path.join(DATASET_PATH, arquivo)
            df = pd.read_csv(caminho, sep=';', parse_dates=['data'], dayfirst=True)
            df.columns = ['Data', 'Valor']
            df['Valor'] = df['Valor'].str.replace(',', '.').astype(float)
            df = df.sort_values('Data')

            plt.plot(df['Data'], df['Valor'], label=f'{codigo}')
        except Exception as e:
            print(f"Erro ao carregar {arquivo}: {e}")
            continue

    plt.title("Comparativo: Endividamento e Comprometimento de Renda")
    plt.xlabel("Ano")
    plt.ylabel("Percentual (%)")
    plt.legend(title="Códigos das Séries")
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(PLOTS_PATH, 'grafico_comparativo.png'))
    plt.close()
    print("Gráfico comparativo salvo.")

@app.route("/")
def index():
    gerar_graficos()

    graficos = [ {
        'titulo': "Endividamento exceto crédito habitacional (29038)",
        'codigo': "29038",
        'explicacao': explicacoes["29038"],
        'interpretacao': interpretacoes["29038"],
        'imagem': '/static/plots/grafico_29038.png'},
        {
        'titulo': "Comparativo: Endividamento e Comprometimento (29038, 29034, 29036, 29037)",
        'codigo': "comparativo",
        'explicacao': "Este gráfico compara quatro séries temporais: endividamento total, endividamento exceto crédito habitacional, comprometimento com serviço da dívida e com juros.",
        'interpretacao': "A comparação evidencia diferenças nas tendências, com destaque para o crescimento acelerado do endividamento total pós-2020.",
        'imagem': '/static/plots/grafico_comparativo.png'
    }]

    return render_template("index.html", graficos=graficos)


if __name__ == "__main__":
    app.run(debug=True)
