"""Exercício 31 — Divisível por 3 e por 5.

A condição mais específica (divisível pelos dois) é testada primeiro.
"""


def ler_int(mensagem: str) -> int:
    """Lê um número inteiro, repetindo a pergunta enquanto a entrada for inválida."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def divisibilidade(numero: int) -> str:
    por3 = numero % 3 == 0
    por5 = numero % 5 == 0
    if por3 and por5:
        return "DIVISÍVEL POR 3 E 5"
    elif por3:
        return "DIVISÍVEL APENAS POR 3"
    elif por5:
        return "DIVISÍVEL APENAS POR 5"
    else:
        return "NÃO DIVISÍVEL POR 3 NEM 5"


def main() -> None:
    numero = ler_int("Digite um número: ")
    print(f"\nResultado: {divisibilidade(numero)}")


if __name__ == "__main__":
    main()
