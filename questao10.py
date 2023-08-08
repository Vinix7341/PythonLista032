
# 10) Escreva um algoritmo pergunte o número total de eleitores de um município, o número de votos brancos, nulos e válidos e apresente como resposta o percentual que cada um representa em relação ao total de eleitores.

print("Me diga o total de eleitores do seu município e votos brancos, nulos e válidos que lhe direi o percentual de cada um dos votos")
e1 = int(input("Número de eleitores:\n"))
b1 = int(input("Número de votos brancos:\n"))
n1 = int(input("Número de votos nulos:\n"))
v1 = int(input("Número de votos válidos:\n"))

b2 = (b1 * 100) / e1
n2 = (n1 * 100) / e1
v2 = (v1 * 100) / e1

print("O percentual de votos é")
print(f"Brancos: {b2}%")
print(f"Nulos: {n2}%")
print(f"Válidos: {v2}%")
