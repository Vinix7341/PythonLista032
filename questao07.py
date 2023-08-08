
# 7) A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das prestações

print("Me diga o valor do produto que você deseja fazer e em quantas prestações deseja parcelar que lhe direi qual o valor de cada prestação")
v = float(input("Digite o valor do produto:\n"))
p = int(input("Digite o número de parcelas até 10 vezes:\n"))

vp = v /p

print(f"O valor de cada parcela é de {vp:.2f}")
