""""
Desenvolva um jogo da forca em Python, no qual o programa escolhe aleatoriamente uma palavra secreta de um conjunto pré-definido. 
O jogador deve tentar adivinhar a palavra digitando letras. Se a letra estiver na palavra secreta, ela deve ser revelada nas posições corretas.
 Caso contrário, o jogador perde uma vida. O jogo continua até que o jogador adivinhe corretamente a palavra secreta ou perca todas as vidas. 
 O número máximo de vidas deve ser definido pelo programador. O jogo deve exibir uma “representação” da forca conforme o jogador erra letras. 
 Ao final do jogo, o programa deve informar se o jogador venceu ou perdeu, e perguntar se deseja jogar novamente. 
"""
import random

palavras = ['abacaxi', 'banana', 'caju', 'damasco', 'figo', 'goiaba', 'laranja', 'manga', 'nectarina', 'pera']

palavra_secreta = random.choice(palavras)

vidas = 6

letras_digitadas = []

while True:
    print()
    letra = input("Digite uma letra: ")

    if letra in letras_digitadas:
        print("Você já digitou essa letra antes.")
        continue

    letras_digitadas.append(letra)

    if letra in palavra_secreta:
        print("Letra correta!")
    else:
        vidas -= 1
        print("Letra incorreta. Você perdeu uma vida.")
        if vidas == 0:
            print("Você perdeu! A palavra secreta era:", palavra_secreta)
            break

    palavra_atual = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_digitadas:
            palavra_atual += letra_secreta
        else:
            palavra_atual += "_"

    print(palavra_atual)

    if palavra_atual == palavra_secreta:
        print("Parabéns! Você ganhou!")
        break
