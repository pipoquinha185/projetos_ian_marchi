
import random

palavras_aleatorias = ["chapeu", "capeta", "canais", "enigma", "lazers"]
palavra_secreta = palavras_aleatorias[random.randint(0, 4)]
tentativas = 6
letras_restantes = len(list(palavra_secreta))
letras_usadas = []

print("Bem vindo a forca!")
input()
print("Quer dizer")
input()
print("...")
input()
print("Bem vindo ao jogo da forca")
input()
print("Adivinhe a palavra e tente não ser enforcado!")
input("Pressione qualquer tecla para começar para começar...")

while tentativas > 0:
    print("\n" + "-" * 30)

    
    Letra = input("Digite uma letra: ").lower()
    
    print("Palavra secreta:", " ".join([letra if letra in letras_usadas else "_" for letra in palavra_secreta]))#join junta os itens de um array em uma string, usando o espaço como separador
    

    if Letra in letras_usadas:
        print("\nVocê já tentou essa letra. Tente outra.")
        continue

    if Letra in palavra_secreta:
        print("Parabéns! Você acertou uma letra!")
        letras_restantes -= 1
    elif Letra in "aeiou":
        print("Ops! Essa vogal não está na palavra. Tente novamenente!")
        tentativas -= 1
    else:
        print("Ops! Essa letra não está na palavra. Tente novamente!")
        tentativas -= 1
        
    letras_usadas.append(Letra)#append adiciona itens a um array
    print("\nLetras usadas:", ", ".join(letras_usadas))#join junta os itens de um array em uma string, usando a vírgula como separador
    print(f"Você tem {tentativas} tentativas restantes.")
    if tentativas > 0:
        print(f"Você tem {tentativas} tentativas restantes.")
    else:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)
        letras_usadas.clear()
        break

    if letras_restantes == 0:
        print("Parabéns! Você ganhou! A palavra secreta era:", palavra_secreta)
        letras_usadas.clear()#clear limpa o array
        break

