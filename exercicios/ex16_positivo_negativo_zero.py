"""Exercício 16 — Positivo, negativo ou zero.

Lê um número real e informa se ele é POSITIVO, NEGATIVO ou ZERO.
"""


def para_float(texto: str) -> float:
    """Converte texto em float aceitando vírgula decimal e "R$".

    >>> para_float("8,5")
    8.5
    >>> para_float("R$ 1.500,00")
    1500.0
    """
    limpo = texto.strip().replace("R$", "").replace(" ", "")
    if "," in limpo:
        limpo = limpo.replace(".", "").replace(",", ".")
    return float(limpo)


def ler_float(mensagem: str) -> float:
    """Lê um número real, repetindo a pergunta enquanto a entrada for inválida."""
    while True:
        try:
            return para_float(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 7,5).")


def classificar_sinal(numero: float) -> str:
    if numero > 0:
        return "POSITIVO"
    elif numero < 0:
        return "NEGATIVO"
    else:
        return "ZERO"  # único caso restante: o zero não é positivo nem negativo


def main() -> None:
    numero = ler_float("Digite um número: ")
    print(f"\nResultado: {classificar_sinal(numero)}")


if __name__ == "__main__":
    main()
