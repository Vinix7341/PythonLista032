
# 2) Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor 09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta quantos minutos já se passaram desde às 00:00h deste dia.

print("Me diga as horas e os minutos de agora e lhe direi em minutos quanto tempo se passou desde 00:00")
hora = int(input("Digite a hora atual: \n"))
min = int(input("Digite o minuto atual: \n"))

hr = hora * 60
res = hr + min

print(f"Já se passaram {res} minutos desde 00:00")