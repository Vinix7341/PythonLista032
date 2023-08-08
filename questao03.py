
# 3) Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.

print("Me diga o seu peso em quilos e a sua altura em metros e converterei o peso para gramas e a altura para centímetros")
kg = float(input("Digite o seu peso em quilos: \n"))
m = float(input("Digite a sua altura em metros: \n"))

g = kg * 1000
cm = m * 100

print(f"O seu peso em gramas é de {g}g e a sua altura em centímetros é de {cm}cm")
