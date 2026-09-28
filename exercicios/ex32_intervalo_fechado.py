"""Exercício 32 — Número dentro do intervalo fechado [10, 20].

Os limites 10 e 20 pertencem ao intervalo.
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


INICIO, FIM = 10, 20


def dentro_do_intervalo(numero: float) -> str:
    return "DENTRO" if INICIO <= numero <= FIM else "FORA"


def main() -> None:
    numero = ler_float("Digite um número: ")
    print(f"\nResultado: {dentro_do_intervalo(numero)}")


if __name__ == "__main__":
    main()
