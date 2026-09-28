"""Exercício 29 — Tipo de triângulo.

Primeiro verifica se as medidas formam um triângulo (reaproveita o Ex. 28);
depois classifica em EQUILÁTERO, ISÓSCELES ou ESCALENO.
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


def forma_triangulo(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a < b + c and b < a + c and c < a + b


def tipo_triangulo(a: float, b: float, c: float) -> str:
    if not forma_triangulo(a, b, c):
        return "NÃO FORMA TRIÂNGULO"
    if a == b == c:
        return "EQUILÁTERO"
    elif a == b or a == c or b == c:
        return "ISÓSCELES"
    else:
        return "ESCALENO"


def main() -> None:
    a = ler_float("Lado 1: ")
    b = ler_float("Lado 2: ")
    c = ler_float("Lado 3: ")
    print(f"\nResultado: {tipo_triangulo(a, b, c)}")


if __name__ == "__main__":
    main()
