"""
Exercício 10 - Salário com comissão

Leia o salário fixo de um vendedor e o total vendido no mês.
Calcule uma comissão de 4% sobre as vendas e mostre a comissão e o
salário total.

Regra: Comissão = total vendido x 4%.
"""

salario_fixo = float(input("Salário fixo: R$ "))
total_vendido = float(input("Total vendido: R$ "))

comissao = total_vendido * 0.04
salario_total = salario_fixo + comissao

print()
print(f"Comissão: R$ {comissao:.2f}")
print(f"Salário total: R$ {salario_total:.2f}")
