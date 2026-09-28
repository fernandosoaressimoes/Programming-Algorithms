"""Exercício 27 — Classificação de IMC (regras didáticas do exercício).

IMC = peso / (altura * altura)
< 18,5 ABAIXO DA FAIXA | < 25,0 FAIXA NORMAL | < 30,0 ACIMA DA FAIXA | >= 30,0 FAIXA ELEVADA
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


def calcular_imc(peso: float, altura: float) -> float:
    if altura <= 0:
        raise ValueError("A altura deve ser maior que zero.")
    return peso / (altura * altura)


def classificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "ABAIXO DA FAIXA"
    elif imc < 25.0:
        return "FAIXA NORMAL"
    elif imc < 30.0:
        return "ACIMA DA FAIXA"
    else:
        return "FAIXA ELEVADA"


def main() -> None:
    peso = ler_float("Peso (kg): ")
    altura = ler_float("Altura (m): ")
    try:
        imc = calcular_imc(peso, altura)
    except ValueError as erro:
        print(f"\n{erro}")
        return
    print(f"\nIMC: {formatar_numero(imc)}")
    print(f"Classificação: {classificar_imc(imc)}")


if __name__ == "__main__":
    main()
