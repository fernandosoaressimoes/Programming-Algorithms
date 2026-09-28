"""Exercício 30 — Aprovação de empréstimo.

Prestação = valor do imóvel / (anos * 12).
Aprovado quando a prestação não ultrapassa 30% do salário.
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


PERCENTUAL_LIMITE = 0.30


def calcular_prestacao(valor_imovel: float, anos: int) -> float:
    if anos <= 0:
        raise ValueError("O prazo deve ser de pelo menos 1 ano.")
    meses = anos * 12  # converte o prazo para meses ANTES de dividir
    return round(valor_imovel / meses, 2)


def limite_prestacao(salario: float) -> float:
    return round(salario * PERCENTUAL_LIMITE, 2)


def analisar_emprestimo(valor_imovel: float, salario: float, anos: int) -> tuple[float, float, str]:
    """Retorna (prestacao, limite, resultado)."""
    prestacao = calcular_prestacao(valor_imovel, anos)
    limite = limite_prestacao(salario)
    # Arredondar os dois em centavos evita erro de ponto flutuante
    # no caso exato do limite (ex.: 600,00 contra 600,00).
    resultado = "APROVADO" if prestacao <= limite else "NEGADO"
    return prestacao, limite, resultado


def main() -> None:
    valor = ler_float("Valor do imóvel: ")
    salario = ler_float("Salário: ")
    anos = ler_int("Prazo (anos): ")
    try:
        prestacao, limite, resultado = analisar_emprestimo(valor, salario, anos)
    except ValueError as erro:
        print(f"\n{erro}")
        return
    print(f"\nPrestação: {formatar_moeda(prestacao)}")
    print(f"Limite: {formatar_moeda(limite)}")
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
