# 1- Conversor de Moeda
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = round(valor_reais / taxa_dolar, 2)
valor_euro = round(valor_reais / taxa_euro, 2)

print("Conversor de Moeda:")
print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Valor em Dólares: $ {valor_dolar}")
print(f"Valor em Euros: € {valor_euro}")
print()