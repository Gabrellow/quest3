import json

# Lê o arquivo JSON com o valor de faturamento diário de uma distribuidora
with open('faturamento.json') as f:
    faturamento_diario = json.load(f)

# Inicializa as variáveis para calcular o menor valor, o maior valor e a média mensal
menor_valor = faturamento_diario[0]
maior_valor = faturamento_diario[0]
soma_valores = 0
dias_com_faturamento = 0

# Calcula o menor valor, o maior valor e a soma dos valores
for valor in faturamento_diario:
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor
    soma_valores += valor
    if valor > 0:
        dias_com_faturamento += 1

# Calcula a média mensal considerando apenas os dias com faturamento
media_mensal = soma_valores / dias_com_faturamento
# Inicializa a variável para contar o número de dias com faturamento superior à média
dias_com_faturamento_acima_media = 0

# Verifica em quantos dias o faturamento foi superior à média mensal
for valor in faturamento_diario:
    if valor > media_mensal:
        dias_com_faturamento_acima_media += 1

# Imprime os resultados
print("Menor valor de faturamento ocorrido em um dia do mês:", menor_valor)
print("Maior valor de faturamento ocorrido em um dia do mês:", maior_valor)
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal:", dias_com_faturamento_acima_media)

