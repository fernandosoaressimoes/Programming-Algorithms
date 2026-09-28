"""Exercício 23 — Categoria de votação (regras didáticas).

< 16 -> NÃO PODE VOTAR | 16-17 -> VOTO OPCIONAL | 18-69 -> VOTO OBRIGATÓRIO | 70+ -> VOTO OPCIONAL
"""


def ler_int(mensagem: str) -> int:
    """Lê um número inteiro, repetindo a pergunta enquanto a entrada for inválida."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def categoria_votacao(idade: int) -> str:
    if idade < 16:
        return "NÃO PODE VOTAR"
    elif idade < 18:
        return "VOTO OPCIONAL"
    elif idade < 70:
        return "VOTO OBRIGATÓRIO"
    else:
        return "VOTO OPCIONAL"


def main() -> None:
    idade = ler_int("Idade: ")
    print(f"\nCategoria: {categoria_votacao(idade)}")


if __name__ == "__main__":
    main()
