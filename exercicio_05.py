"""
Exercício 5 - Conversão de medidas

Leia uma medida em metros e mostre o valor equivalente em
centímetros e milímetros.

Regra: 1 metro = 100 centímetros = 1.000 milímetros.
"""

metros = float(input("Metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print()
print(f"Centímetros: {centimetros:.0f}")
print(f"Milímetros: {milimetros:.0f}")
