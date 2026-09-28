"""Exercício 34 — Quantidade de dias do mês.

31 dias: 1, 3, 5, 7, 8, 10, 12 | 30 dias: 4, 6, 9, 11 | fevereiro: 28 ou 29 (bissexto).
Mês fora de 1 a 12 -> MÊS INVÁLIDO. Reaproveita a regra do Ex. 24.
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


MESES_31 = (1, 3, 5, 7, 8, 10, 12)
MESES_30 = (4, 6, 9, 11)


def dias_do_mes(mes: int, ano: int) -> int | None:
    """Retorna a quantidade de dias, ou None se o mês for inválido."""
    if mes in MESES_31:
        return 31
    elif mes in MESES_30:
        return 30
    elif mes == 2:
        return 29 if eh_bissexto(ano) else 28
    return None


def main() -> None:
    mes = ler_int("Mês: ")
    ano = ler_int("Ano: ")
    dias = dias_do_mes(mes, ano)
    print("\nResultado: " + ("MÊS INVÁLIDO" if dias is None else f"{dias} dias"))


if __name__ == "__main__":
    main()
