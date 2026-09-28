# Exercicio 1 - Validacao de strings e parametros

def valida_string(texto, minimo=1, maximo=100):
    tamanho = len(texto)
    if tamanho >= minimo and tamanho <= maximo:
        return True
    else:
        return False


# testando a funcao
print(valida_string("Fernando"))
print(valida_string(""))
print(valida_string("Python", 3, 5))
print(valida_string("SQL", 3, 5))

nome = input("Digite um nome: ")
resultado = valida_string(nome, 3, 50)

if resultado == True:
    print("Nome valido")
else:
    print("Nome invalido, precisa ter entre 3 e 50 letras")
