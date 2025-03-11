# 2- Calculadora de Desconto
produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

valor_desconto = round(preco_original * (percentual_desconto / 100), 2)
preco_final = round(preco_original - valor_desconto, 2)

print("Calculadora de Desconto:")
print(f"Produto: {produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {percentual_desconto}%")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")
print()