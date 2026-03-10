import random

#import random é a livraria para randomizar numeros ou valores
#
numero_secreto = random.randint(1,100)#randint é a propriedade re dandomiza numeros inteiros

while True:
    palpite = input("Digite seu palpite aqui: ")
    palpite_numero = int(palpite)
    if(palpite_numero == numero_secreto):
        print("Voce acertou!! Parabens")
        break
    elif(palpite_numero > numero_secreto):
        print("Muito alto!! chute mais baixo")
    else:
        print("Muito baixo!! Aumenta isso ai chefe")