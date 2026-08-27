"""
Jogo de Adivinhação

O computador sorteia um número inteiro entre 1 e 100. O jogador
tenta adivinhar o número, e a cada tentativa recebe uma dica
("Muito alto!" ou "Muito baixo!") até acertar.

Pratica: laços de repetição (while), condicionais (if/elif/else)
e funções.
"""

import random


def sortear_numero(minimo=1, maximo=100):
    """Sorteia e retorna um número inteiro entre minimo e maximo."""
    return random.randint(minimo, maximo)


def ler_palpite():
    """Lê um palpite do jogador, garantindo que seja um número inteiro."""
    while True:
        entrada = input("Seu palpite: ")
        if entrada.isdigit():
            return int(entrada)
        print("Digite apenas números inteiros. Tente novamente.")


def jogar(minimo=1, maximo=100):
    """Executa uma partida completa do jogo de adivinhação."""
    numero_secreto = sortear_numero(minimo, maximo)
    tentativas = 0

    print(f"Pensei em um número entre {minimo} e {maximo}. Tente adivinhar!")

    while True:
        palpite = ler_palpite()
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            print()
            print(f"Parabéns! Você acertou o número {numero_secreto} "
                  f"em {tentativas} tentativa(s).")
            break


def perguntar_jogar_novamente():
    """Pergunta ao jogador se ele quer jogar outra rodada."""
    resposta = input("Quer jogar novamente? (s/n): ").strip().lower()
    return resposta == "s"


def main():
    print("=== JOGO DE ADIVINHAÇÃO ===")
    print()

    continuar = True
    while continuar:
        jogar()
        print()
        continuar = perguntar_jogar_novamente()
        print()

    print("Obrigado por jogar!")


if __name__ == "__main__":
    main()
