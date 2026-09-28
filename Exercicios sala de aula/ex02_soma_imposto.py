# Exercicio 2 - Calculo de imposto

def soma_imposto(taxa_imposto, custo):
    imposto = custo * taxa_imposto / 100
    valor_final = custo + imposto
    return valor_final


custo = float(input("Digite o custo do produto: "))
taxa = float(input("Digite a taxa de imposto (%): "))

total = soma_imposto(taxa, custo)

print("Valor final: R$ %.2f" % total)
