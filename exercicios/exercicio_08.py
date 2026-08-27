"""
Exercício 8 - Desconto no produto

Leia o preço de um produto. Calcule um desconto de 10% e mostre o
valor do desconto e o preço final.

Regra: Desconto = preço x 10%.
"""

preco = float(input("Preço: R$ "))

desconto = preco * 0.10
preco_final = preco - desconto

print()
print(f"Desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
