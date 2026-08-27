"""
Exercício 9 - Reajuste salarial

Leia o salário atual de um funcionário. Calcule um aumento de 15%
e mostre o valor do aumento e o novo salário.

Regra: Aumento = salário atual x 15%.
"""

salario = float(input("Salário atual: R$ "))

aumento = salario * 0.15
novo_salario = salario + aumento

print()
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
