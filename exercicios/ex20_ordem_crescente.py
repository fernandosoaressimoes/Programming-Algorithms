"""Exercício 20 — Três valores em ordem crescente.

Ordena três inteiros com trocas (sem sorted), aceitando valores repetidos.
Entrada numa linha só: "9, 2, 5" ou "9 2 5".
"""


def ordenar_tres(a: int, b: int, c: int) -> tuple[int, int, int]:
    # Três comparações com troca bastam para ordenar três valores.
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c


def ler_tres_inteiros(texto: str) -> tuple[int, int, int]:
    partes = texto.replace(",", " ").split()
    if len(partes) != 3:
        raise ValueError("Informe exatamente três valores.")
    a, b, c = (int(p) for p in partes)
    return a, b, c


def main() -> None:
    while True:
        try:
            a, b, c = ler_tres_inteiros(input("Valores: "))
            break
        except ValueError:
            print("Entrada inválida. Exemplo: 9, 2, 5")
    x, y, z = ordenar_tres(a, b, c)
    print(f"\nOrdem crescente: {x}, {y}, {z}")


if __name__ == "__main__":
    main()
