import math

# 4) Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na tela o valor do índice de massa corporal desta pessoa (IMC). Fórmula: IMC = peso / altura2 - Obs: peso em quilos e altura em metros

print("Me diga o seu peso em quilos e a sua altura em metros e farei o seu IMC")
kg = float(input("Digite o seu peso em quilos: \n"))
m = float(input("Digite a sua altura em metros: \n"))

imc = kg / math.pow(m,2)

print(f"O seu IMC é {imc}")