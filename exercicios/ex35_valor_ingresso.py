"""Exercício 35 — Valor do ingresso.

Ingresso: R$ 30,00. Meia-entrada (50%) para menores de 12 anos, estudantes
ou pessoas com 60 anos ou mais. O desconto NÃO é acumulativo.
"""


def formatar_moeda(valor: float) -> str:
    """Formata em reais: 1725 -> 'R$ 1.725,00'."""
    texto = f"{valor:,.2f}"  # 1,725.00
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


def ler_int(mensagem: str) -> int:
    """Lê um número inteiro, repetindo a pergunta enquanto a entrada for inválida."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


PRECO_INTEIRA = 30.00


def tem_meia_entrada(idade: int, estudante: bool) -> bool:
    return idade < 12 or estudante or idade >= 60


def valor_ingresso(idade: int, estudante: bool) -> float:
    # Um único "or": mesmo que várias condições sejam verdadeiras,
    # o desconto de 50% é aplicado uma vez só.
    return PRECO_INTEIRA / 2 if tem_meia_entrada(idade, estudante) else PRECO_INTEIRA


def ler_sim_nao(mensagem: str) -> bool:
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in ("S", "SIM"):
            return True
        if resposta in ("N", "NAO", "NÃO"):
            return False
        print("Responda SIM ou NÃO.")


def main() -> None:
    idade = ler_int("Idade: ")
    estudante = ler_sim_nao("Estudante (SIM/NÃO): ")
    print(f"\nValor do ingresso: {formatar_moeda(valor_ingresso(idade, estudante))}")


if __name__ == "__main__":
    main()
