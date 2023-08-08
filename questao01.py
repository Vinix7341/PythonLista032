
# 1) Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o valor com o acréscimo dos 10% da gorjeta do garçom.

val = float(input("Me diga valor da sua conta e lhe direi qual o valor total com o acréscimo de 10% do garçom: \n"))

tot = val + val * 10 / 100

print(f"O valor total da conta com o acréscimo do garçom é {tot}")
