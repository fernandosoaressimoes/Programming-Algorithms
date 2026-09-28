"""Exercício 28 — É possível formar um triângulo?

Cada lado deve ser menor que a soma dos outros dois (as três desigualdades).
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


def forma_triangulo(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a < b + c and b < a + c and c < a + b


def main() -> None:
    a = ler_float("Lado 1: ")
    b = ler_float("Lado 2: ")
    c = ler_float("Lado 3: ")
    resultado = "FORMAM UM TRIÂNGULO" if forma_triangulo(a, b, c) else "NÃO FORMAM UM TRIÂNGULO"
    print(f"\nLados: {formatar_auto(a)}, {formatar_auto(b)} e {formatar_auto(c)}")
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
