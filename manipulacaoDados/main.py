import json

# Abrir o arquivo JSON
with open('dados.json', 'r') as arquivo:
    dados_json = json.load(arquivo)

# Obter a lista de vendas
vendas = dados_json['vendas']

produtoMaisVendido = None
maiorTotalVendas = 0

for venda in vendas:
    produto = venda['produto']
    quantidade = venda['quantidade']
    preco = venda['preço']
    totalVendas = quantidade * preco

    if totalVendas > maiorTotalVendas:
        produtoMaisVendido = produto
        maiorTotalVendas = totalVendas

print(f"O produto mais vendido é: {produtoMaisVendido}")