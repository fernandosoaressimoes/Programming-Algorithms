# Q2 - Montanha-russa: controle de acesso e valor do ingresso

altura = float(input("Digite a altura (m): "))
idade = int(input("Digite a idade: "))

if altura < 1.40:
    print("Acesso negado por razões de segurança (altura mínima necessária: 1.40m)")
elif idade < 12:
    print("Acesso autorizado. Valor do ingresso: R$ 15,00")
elif idade <= 59:
    print("Acesso autorizado. Valor do ingresso: R$ 30,00")
else:
    print("Acesso autorizado. Valor do ingresso: R$ 15,00")
