
# 6) Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final do mês

print("Me informe algumas coisas sobre você e lhe farei uma lista com essas informações")
nome = str(input("Diga seu nome:\n"))
sal = float(input("Diga seu salário:\n"))
ven = int(input("Diga seu total de vendas esse mês em dinheiro:\n"))

com = ven + ven * 15 / 100
tot = sal + com

print(f"Nome: {nome}")
print(f"Salário fixo: {sal}")
print(f"Comissão: {com}")
print(f"Salário completo: {tot}")
