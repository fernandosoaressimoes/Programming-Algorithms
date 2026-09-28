"""Exercício 21 — Aprovado ou reprovado.

Média >= 7,0 -> APROVADO; abaixo de 7,0 -> REPROVADO.
"""


def formatar_numero(valor: float, casas: int = 1) -> str:
    """Formata com vírgula decimal: 7.0 -> '7,0'."""
    return f"{valor:.{casas}f}".replace(".", ",")


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


MEDIA_APROVACAO = 7.0


def media(nota1: float, nota2: float) -> float:
    return (nota1 + nota2) / 2


def situacao(media_final: float) -> str:
    return "APROVADO" if media_final >= MEDIA_APROVACAO else "REPROVADO"


def main() -> None:
    n1 = ler_float("Nota 1: ")
    n2 = ler_float("Nota 2: ")
    m = media(n1, n2)
    print(f"\nMédia: {formatar_numero(m)}")
    print(f"Situação: {situacao(m)}")


if __name__ == "__main__":
    main()
