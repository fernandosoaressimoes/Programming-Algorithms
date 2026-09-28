"""Exercício 25 — Preço conforme a forma de pagamento.

1 Dinheiro/Pix: -10% | 2 Débito: -5% | 3 Crédito à vista: sem alteração | 4 Crédito parcelado: +8%
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


def ler_int(mensagem: str) -> int:
    """Lê um número inteiro, repetindo a pergunta enquanto a entrada for inválida."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


# opção -> (descrição, fator multiplicador)
FORMAS_PAGAMENTO = {
    1: ("Dinheiro ou Pix", 0.90),
    2: ("Débito", 0.95),
    3: ("Crédito à vista", 1.00),
    4: ("Crédito parcelado", 1.08),
}


def valor_final(preco: float, opcao: int) -> float:
    if opcao not in FORMAS_PAGAMENTO:
        raise ValueError("Opção de pagamento inválida.")
    _, fator = FORMAS_PAGAMENTO[opcao]
    return round(preco * fator, 2)


def main() -> None:
    preco = ler_float("Preço: ")
    for numero, (descricao, _) in FORMAS_PAGAMENTO.items():
        print(f"  {numero} - {descricao}")
    opcao = ler_int("Opção: ")
    try:
        print(f"\nValor final: {formatar_moeda(valor_final(preco, opcao))}")
    except ValueError as erro:
        print(f"\n{erro}")


if __name__ == "__main__":
    main()
