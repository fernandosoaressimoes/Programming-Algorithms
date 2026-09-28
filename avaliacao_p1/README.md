# Avaliação Parcial 1 — Programming and Algorithms (SI)

**Data:** 15/09/2026  
**Linguagem:** Python

| Arquivo | Questão |
|---|---|
| [`q1_expressoes.py`](q1_expressoes.py) | Q1 — Resolução passo a passo das expressões |
| [`q2_montanha_russa.py`](q2_montanha_russa.py) | Q2 — Controle de acesso da montanha-russa |

---

## Q1 (3,0)

Demonstrar passo a passo a resolução das duas expressões abaixo.  
Considerar: `a = 15`, `b = 4` e `c = 2`.

```python
res_1 = a / b - c ** b % a + a // b % 5
res_2 = not (c % a == 0) and (b * c + 2 > a or a - b * c != 7)
```

### Resposta

Ordem de precedência: `()` → `**` → `*` `/` `//` `%` (da esquerda para a direita) → `+` `-` → comparações → `not` → `and` → `or`

#### res_1 = a / b - c ** b % a + a // b % 5

| Passo | Operação | Resultado | Expressão restante |
|:--:|---|---|---|
| 1 | `c ** b` = 2 ** 4 | 16 | 15 / 4 - 16 % 15 + 15 // 4 % 5 |
| 2 | `a / b` = 15 / 4 | 3.75 | 3.75 - 16 % 15 + 15 // 4 % 5 |
| 3 | `16 % 15` | 1 | 3.75 - 1 + 15 // 4 % 5 |
| 4 | `a // b` = 15 // 4 | 3 | 3.75 - 1 + 3 % 5 |
| 5 | `3 % 5` | 3 | 3.75 - 1 + 3 |
| 6 | `3.75 - 1` | 2.75 | 2.75 + 3 |
| 7 | `2.75 + 3` | **5.75** | **res_1 = 5.75** |

O resultado é `float` porque o operador `/` sempre devolve um número real.

#### res_2 = not (c % a == 0) and (b * c + 2 > a or a - b * c != 7)

| Passo | Operação | Resultado |
|:--:|---|---|
| 1 | `c % a` = 2 % 15 | 2 |
| 2 | `2 == 0` | False |
| 3 | `not False` | True |
| 4 | `b * c` = 4 * 2 | 8 |
| 5 | `8 + 2` | 10 |
| 6 | `10 > 15` | False |
| 7 | `a - b * c` = 15 - 8 | 7 |
| 8 | `7 != 7` | False |
| 9 | `False or False` | False |
| 10 | `True and False` | **res_2 = False** |

---

## Q2 (3,5)

Um parque de diversões moderno possui uma montanha-russa de alta velocidade com controle eletrônico de bilheteria e acesso. Para garantir a segurança, o sistema lê duas informações cruciais do cliente: a altura em metros e a idade em anos. As regras para permitir o acesso e o valor do ingresso são:

**a.** Visitantes com altura estritamente inferior a 1.40m estão impedidos de entrar no brinquedo, não importando a idade. O programa deve emitir a mensagem: *'Acesso negado por razões de segurança (altura mínima necessária: 1.40m)'*.

**b.** Visitantes autorizados (com altura maior ou igual a 1.40m) pagam ingressos de acordo com a faixa etária:

- Menores de 12 anos: pagam R$ 15,00.
- De 12 a 59 anos: pagam o valor cheio de R$ 30,00.
- Idosos (60 anos ou mais): pagam metade do valor, R$ 15,00.

Escreva um programa em Python que solicite as entradas de altura e idade, realize os testes lógicos estruturados sem aninhamentos desnecessários (escreva um código plano e legível) e exiba se o acesso foi autorizado e o valor do ingresso pago.

### Resposta

```python
altura = float(input("Digite a altura (m): "))
idade = int(input("Digite a idade: "))

if altura < 1.40:
    print("Acesso negado por razões de segurança (altura mínima necessária: 1.40m)")
elif idade < 12:
    print("Acesso autorizado. Valor do ingresso: R$ 15,00")
elif idade <= 59:
    print("Acesso autorizado. Valor do ingresso: R$ 30,00")
else:
    print("Acesso autorizado. Valor do ingresso: R$ 15,00")
```

O código não tem `if` dentro de `if`. A altura é testada primeiro; assim, todo `elif` seguinte só é avaliado para quem tem 1,40 m ou mais.

#### Testes de execução

| Altura | Idade | Saída |
|:--:|:--:|---|
| 1.39 | 30 | Acesso negado |
| 1.20 | 70 | Acesso negado (a idade não importa) |
| 1.40 | 11 | Autorizado, R$ 15,00 |
| 1.40 | 12 | Autorizado, R$ 30,00 |
| 1.80 | 59 | Autorizado, R$ 30,00 |
| 1.70 | 60 | Autorizado, R$ 15,00 |

## Como executar

```bash
python q1_expressoes.py
python q2_montanha_russa.py
```
