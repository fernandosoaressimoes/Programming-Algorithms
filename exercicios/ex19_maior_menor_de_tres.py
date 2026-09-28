"""Exercício 19 — Maior e menor de três números.

Resolvido só com comparações (sem max/min prontos), para treinar a lógica.
Funciona com valores repetidos.
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


def maior_e_menor(a: float, b: float, c: float) -> tuple[float, float]:
    maior = a
    menor = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return maior, menor


def main() -> None:
    a = ler_float("Valor 1: ")
    b = ler_float("Valor 2: ")
    c = ler_float("Valor 3: ")
    maior, menor = maior_e_menor(a, b, c)
    print(f"\nMaior: {formatar_auto(maior)}")
    print(f"Menor: {formatar_auto(menor)}")


if __name__ == "__main__":
    main()
