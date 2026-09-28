"""Exercício 26 — Reajuste por faixa salarial.

Até R$ 1.500,00 -> 15% | de R$ 1.500,01 até R$ 3.000,00 -> 10% | acima de R$ 3.000,00 -> 5%
Mostra o percentual, o valor do aumento e o novo salário.
"""


def formatar_moeda(valor: float) -> str:
    """Formata em reais: 1725 -> 'R$ 1.725,00'."""
    texto = f"{valor:,.2f}"  # 1,725.00
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


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


def percentual_reajuste(salario: float) -> int:
    if salario <= 1500.00:
        return 15
    elif salario <= 3000.00:
        return 10
    else:
        return 5


def calcular_reajuste(salario: float) -> tuple[int, float, float]:
    """Retorna (percentual, aumento, novo_salario)."""
    percentual = percentual_reajuste(salario)
    aumento = round(salario * percentual / 100, 2)
    return percentual, aumento, round(salario + aumento, 2)


def main() -> None:
    salario = ler_float("Salário atual: ")
    percentual, aumento, novo = calcular_reajuste(salario)
    print(f"\nPercentual aplicado: {percentual}%")
    print(f"Valor do aumento: {formatar_moeda(aumento)}")
    print(f"Novo salário: {formatar_moeda(novo)}")


if __name__ == "__main__":
    main()
