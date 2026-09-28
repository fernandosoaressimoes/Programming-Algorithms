"""Exercício 17 — Par ou ímpar.

Um número é par quando o resto da divisão por 2 é igual a zero.
"""


def ler_int(mensagem: str) -> int:
    """Lê um número inteiro, repetindo a pergunta enquanto a entrada for inválida."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def par_ou_impar(numero: int) -> str:
    # Comparar com 0 (e não com 1) funciona também para negativos em qualquer
    # linguagem: em Java/C, -7 % 2 vale -1, e não 1.
    return "PAR" if numero % 2 == 0 else "ÍMPAR"


def main() -> None:
    numero = ler_int("Digite um número: ")
    print(f"\nResultado: {par_ou_impar(numero)}")


if __name__ == "__main__":
    main()
