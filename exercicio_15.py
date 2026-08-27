"""
Exercício 15 - Custo final da compra

Leia o preço unitário de um produto, a quantidade comprada e o
valor do frete. Mostre o subtotal dos produtos e o valor total da
compra.

Regra:
Subtotal = preço unitário x quantidade.
Total = subtotal + frete.
"""

preco_unitario = float(input("Preço unitário: R$ "))
quantidade = int(input("Quantidade: "))
frete = float(input("Frete: R$ "))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print()
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Total: R$ {total:.2f}")
