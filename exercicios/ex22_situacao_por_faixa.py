"""Exercício 22 — Situação do aluno por faixa.

Média < 5,0 -> REPROVADO | 5,0 <= média < 7,0 -> RECUPERAÇÃO | >= 7,0 -> APROVADO.
"""


def formatar_numero(valor: float, casas: int = 1) -> str:
    """Formata com vírgula decimal: 7.0 -> '7,0'."""
    return f"{valor:.{casas}f}".replace(".", ",")


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


def media(nota1: float, nota2: float) -> float:
    return (nota1 + nota2) / 2


def situacao_por_faixa(media_final: float) -> str:
    # Testando do menor para o maior limite, cada elif já sabe que as faixas
    # anteriores falharam: nenhum valor fica sem classificação nem cai em duas.
    if media_final < 5.0:
        return "REPROVADO"
    elif media_final < 7.0:
        return "RECUPERAÇÃO"
    else:
        return "APROVADO"


def main() -> None:
    n1 = ler_float("Nota 1: ")
    n2 = ler_float("Nota 2: ")
    m = media(n1, n2)
    print(f"\nMédia: {formatar_numero(m)}")
    print(f"Situação: {situacao_por_faixa(m)}")


if __name__ == "__main__":
    main()
