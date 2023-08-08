
# 8) Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

print("Me diga o valor do produto que você deseja comprar para revender e a porcentagem que você deseja lucrar com a venda e lhe direi o valor da venda do produto")
prod = float(input("Valor do produto comprado:\n"))
por = float(input("Porcentagem que deseja lucrar:\n"))

res = prod + prod * por / 100

print(f"O valor da venda para conseguir o lucro pedido deve ser de {res}")
