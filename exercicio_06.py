"""
Exercício 6 - Área e perímetro do retângulo

Leia a largura e a altura de um retângulo. Mostre a área e o
perímetro.

Regra:
Área = largura x altura.
Perímetro = 2 x (largura + altura).
"""

largura = float(input("Largura: "))
altura = float(input("Altura: "))

area = largura * altura
perimetro = 2 * (largura + altura)

print()
print(f"Área: {area}")
print(f"Perímetro: {perimetro}")
