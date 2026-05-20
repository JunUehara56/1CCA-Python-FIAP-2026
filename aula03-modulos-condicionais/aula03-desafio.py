# DESAFIO
idade = int(input("Digite a idade: "))
if idade < 16:
    print("Não vota")
elif idade >= 16 and idade < 18:
    print("Voto opcional")
elif idade >= 18 and idade < 70:
    print("Voto obrigatório")
else:
    print("Voto opcional")