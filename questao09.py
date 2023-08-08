
# 9) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias

print("Me diga a sua idade em anos, meses e dias e lhe direi a sua idade apenas em dias aproximadamente")
ano = int(input("Quantos anos você tem:\n"))
mes = int(input("Quantos meses você tem:\n"))
dia = int(input("Quantos dias você tem:\n"))

ad = ano * 365
md = mes * 30
dias = ad + md + dia

print(f"A sua idade em dias é de aproximadamente {dias} dias")
