
# 5) Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão do primeiro pelo segundo número.

print("Me diga dois números e lhe mostrarei algumas contas com eles")
v1 = float(input("Digite o primeiro número: \n"))
v2 = float(input("Digite o segundo número: \n"))

soma = v1 + v2
sub1 = v1 - v2
sub2 = v2 - v1
mult = v1 * v2
div = v1 / v2
rest = v1 % v2

print(f"A soma dos dois números: {soma}")
print(f"A subtração do primeiro pelo segundo número: {sub1}")
print(f"A subtração do segundo pelo primeiro número: {sub2}")
print(f"A multiplicação entre os dois números: {mult}")
print(f"A divisão do primeiro pelo segundo número: {div}")
print(f"A resto da divisão do primeiro pelo segundo número: {rest}")
