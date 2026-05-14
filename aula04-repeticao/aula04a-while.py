# cp = 0
# while cp < 3:
#     print(f"Produto {cp}")
#     cp += 1
#
# # while decrescente de 4 a 1 (incluindo)
# i = 4
# while 1 > 0:
#     print(i)
#     i -= 1
#
# repeticao com entrada do usuario
jogar = "Sim"

while jogar.lower() == "sim":
    print("Inicia ou repete o jogo")
    jogar = input("Deseja jogar novamente? ")

# Modificadores de fluxo
i = 0
while 1 < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 7:
        break

    print(f"Produto {i}")
print("FIM")