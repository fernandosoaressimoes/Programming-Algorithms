"""Exercício 33 — Dia da semana.

Número de 1 a 7 -> dia correspondente; qualquer outro valor -> OPÇÃO INVÁLIDA.
Usa match/case (Python 3.10+), o equivalente ao "escolha/caso" do Portugol
e ao switch do Java/C.
"""


def ler_int(mensagem: str) -> int:
    """Lê um número inteiro, repetindo a pergunta enquanto a entrada for inválida."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def dia_da_semana(numero: int) -> str:
    match numero:
        case 1:
            return "SEGUNDA-FEIRA"
        case 2:
            return "TERÇA-FEIRA"
        case 3:
            return "QUARTA-FEIRA"
        case 4:
            return "QUINTA-FEIRA"
        case 5:
            return "SEXTA-FEIRA"
        case 6:
            return "SÁBADO"
        case 7:
            return "DOMINGO"
        case _:
            return "OPÇÃO INVÁLIDA"


def main() -> None:
    numero = ler_int("Número (1 a 7): ")
    print(f"\nResultado: {dia_da_semana(numero)}")


if __name__ == "__main__":
    main()
