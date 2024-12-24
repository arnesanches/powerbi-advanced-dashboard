import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel("Base Financeiro.xlsx")

# Exibir as primeiras linhas para entender a estrutura
print(df.head())

# Filtrar os dados apenas onde o Tipo é "Recebimento"
recebimentos = df[df["Tipo"] == "Recebimento"]

# Somar os valores da coluna "Valor da Movimentação"
receita_total = recebimentos["Valor da Movimentação"].sum()

print(f"Receita Total: R${receita_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Filtrar os dados apenas onde o Tipo é "Pagamento"
pagamentos = df[df["Tipo"] == "Pagamento"]

# Somar os valores absolutos da coluna "Valor da Movimentação"
custos_total = pagamentos["Valor da Movimentação"].abs().sum()

print(f"Custos Totais: R${custos_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Receita total (caso já tenha sido calculada)
# Receita_total = 1000  # Exemplo, substitua pelo valor real se necessário

# Calculando os impostos como 15% da receita total
impostos = receita_total * 0.15
print(f"Total de Impostos (15% da Receita): R${impostos:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Calculando o lucro
lucro = receita_total - custos_total - impostos

# Exibindo o lucro
print(f"Lucro Total: R${lucro:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Calculando a margem de lucro 
margem_lucro = (lucro / receita_total) * 100
# Exibindo o lucro
print(f"Margem de lucro: R${margem_lucro:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Cálculo do fluxo de caixa
# Filtrando os recebimentos e pagamentos
recebimentos_totais = df[df["Tipo"] == "Recebimento"]["Valor da Movimentação"].sum()
pagamentos_totais = df[df["Tipo"] == "Pagamento"]["Valor da Movimentação"].sum()

# Fluxo de caixa
fluxo_de_caixa = recebimentos_totais - pagamentos_totais
print(fluxo_de_caixa)

# Calculando o total de transações
total_transacoes = len(df)
print(f"Total de transações: {total_transacoes}")

# Total de transações via Pix
transacoes_pix = df[df['Forma Pagamento'] == 'Pix']['Forma Pagamento'].count()
print(f"Total de transações via Pix: {transacoes_pix}")

# Percentual de transações via Pix
percentual_pix = (transacoes_pix / total_transacoes) * 100
print(f"Percentual de transações via Pix: {percentual_pix:.2f}%")

# Dados das cidades e suas margens
cidades = {
    "São Paulo": 63.60,
    "Rio de Janeiro": 33.70,
    "Vitória": 26.32,
    "Belo Horizonte": 21.45
}

# Calcular o desvio da meta para cada cidade
desvios_meta = {cidade: margem - 30 for cidade, margem in cidades.items()}

# Exibir os resultados
print("Resultados de Desvio da Meta por Cidade:")
for cidade, desvio in desvios_meta.items():
    print(f"Cidade: {cidade}, Margem de Lucro: {cidades[cidade]:.2f}%, Desvio da Meta (%): {desvio:+.2f}")