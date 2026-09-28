"""Exercício 18 — Maior de dois números.

Mostra o maior de dois números reais; se forem iguais, informa VALORES IGUAIS.
"""


def formatar_auto(valor: float) -> str:
    """Mostra inteiros sem casas decimais (12.0 -> '12') e reais com vírgula (-0.5 -> '-0,5')."""
    if float(valor).is_integer():
        return str(int(valor))
    return f"{valor:g}".replace(".", ",")


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


def maior_de_dois(a: float, b: float) -> float | None:
    """Retorna o maior valor, ou None quando os dois são iguais."""
    if a > b:
        return a
    elif b > a:
        return b
    return None


def main() -> None:
    a = ler_float("Primeiro valor: ")
    b = ler_float("Segundo valor: ")
    maior = maior_de_dois(a, b)
    if maior is None:
        print("\nVALORES IGUAIS")
    else:
        print(f"\nMaior valor: {formatar_auto(maior)}")


if __name__ == "__main__":
    main()
