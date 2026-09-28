"""Exercício 24 — Ano bissexto.

Bissexto: divisível por 400, OU divisível por 4 e não divisível por 100.
"""


def ler_int(mensagem: str) -> int:
    """Lê um número inteiro, repetindo a pergunta enquanto a entrada for inválida."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def eh_bissexto(ano: int) -> bool:
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)


def main() -> None:
    ano = ler_int("Ano: ")
    resultado = "ANO BISSEXTO" if eh_bissexto(ano) else "ANO NÃO BISSEXTO"
    print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    main()
