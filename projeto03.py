"""
Projeto: Adivinhe o número

Descrição: Neste jogo, o programa escolhe aleatoriamente um número entre 1 e 100. O jogador deve tentar adivinhar o número correto dentro de um número limitado de tentativas.

Regras:

O programa escolhe um número aleatório entre 1 e 100.
O jogador tem no máximo 10 tentativas.
O jogador faz uma suposição fornecendo um número.
O programa informa ao jogador se o número correto é maior ou menor do que a suposição feita.
O jogador continua fazendo suposições até adivinhar corretamente o número ou esgotar o número de tentativas.
Funcionalidades adicionais:

No início do jogo, o programa exibe uma mensagem de boas-vindas e explica as regras do jogo.
O programa mantém um registro do número de tentativas do jogador.
Ao final do jogo, o programa informa se o jogador adivinhou corretamente o número ou não, e exibe o número de tentativas realizadas.
O programa pergunta se o jogador deseja jogar novamente.
Dicas:

Você pode usar a biblioteca random em Python para gerar o número aleatório.
Utilize estruturas de controle como loops e condicionais para implementar a lógica do jogo.
Lembre-se de validar a entrada do jogador, garantindo que seja um número dentro do intervalo correto."""

import random

def adivinhe_o_numero():
    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("O programa escolherá um número aleatório entre 1 e 100.")
    print("Você tem 10 tentativas para adivinhar o número correto.")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    while tentativas < 10:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1
        
        if palpite < numero_secreto:
            print("O número correto é maior do que o seu palpite.")
        elif palpite > numero_secreto:
            print("O número correto é menor do que o seu palpite.")
        else:
            print(f"Parabéns! Você adivinhou o número correto em {tentativas} tentativas.")
            break
    
    if tentativas == 10:
        print(f"Fim de jogo! Você esgotou todas as suas {tentativas} tentativas.")
    
    jogar_novamente = input("Deseja jogar novamente? (s/n) ")
    if jogar_novamente.lower() == "s":
        adivinhe_o_numero()
    else:
        print("Obrigado por jogar!")
        
adivinhe_o_numero()
