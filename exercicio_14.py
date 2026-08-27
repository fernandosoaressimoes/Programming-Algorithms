"""
Exercício 14 - Troca de valores

Leia dois valores inteiros, armazene-os em A e B e troque seus
conteúdos. Ao final, mostre os valores depois da troca.

Requisito: faça a troca utilizando uma variável auxiliar.
"""

a = int(input("A: "))
b = int(input("B: "))

aux = a
a = b
b = aux

print()
print("Depois da troca:")
print(f"A: {a}")
print(f"B: {b}")
