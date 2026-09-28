# Q1 - Resolucao das expressoes passo a passo
# a = 15, b = 4, c = 2

a = 15
b = 4
c = 2

# res_1 = a / b - c ** b % a + a // b % 5
passo1 = c ** b          # 16
passo2 = a / b           # 3.75
passo3 = passo1 % a      # 16 % 15 = 1
passo4 = a // b          # 3
passo5 = passo4 % 5      # 3 % 5 = 3
passo6 = passo2 - passo3 # 3.75 - 1 = 2.75
res_1 = passo6 + passo5  # 2.75 + 3 = 5.75

print("res_1 passo a passo:", passo1, passo2, passo3, passo4, passo5, passo6, res_1)
print("res_1 direto:", a / b - c ** b % a + a // b % 5)

# res_2 = not (c % a == 0) and (b * c + 2 > a or a - b * c != 7)
p1 = c % a               # 2
p2 = p1 == 0             # False
p3 = not p2              # True
p4 = b * c + 2           # 10
p5 = p4 > a              # False
p6 = a - b * c           # 7
p7 = p6 != 7             # False
p8 = p5 or p7            # False
res_2 = p3 and p8        # False

print("res_2 passo a passo:", p1, p2, p3, p4, p5, p6, p7, p8, res_2)
print("res_2 direto:", not (c % a == 0) and (b * c + 2 > a or a - b * c != 7))
