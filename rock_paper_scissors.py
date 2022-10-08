''' Neste projeto irei trabalhar com estruturas de condicionais com mais de uma condição, 
estrutura de listas em python e novos operados lógicos.'''

import random 

user_points = 0 
computer_points = 0 

options = ["r", "t", "p"]

while True:
    user_choice = input("Escolha R(Pedra) /T(Tesoura /P(Papel) ou Q para sair. ") .lower()  # essa função permite que todas as strings digitas retornem em formato minusculos, isso  # ajuda na verificação do input do usuário , que poderá digitar caracteres em ambos  #  formatos, sem que com isso apresente erro .

    if user_choice == 'q':
        break

    if user_choice not in options:
        continue

    computer_choice = random.randint(0, 2)

    computer_option = options[computer_choice]

    print("O computador escolheu {}".format(computer_option))

    if user_choice == computer_option:
        print("Empate!")

    elif user_choice == "r" and computer_option =="t":
        print("Você ganhou!")
        user_points = user_points + 1

    elif user_choice == "p" and computer_option =="r":
        print("Você ganhou!")
        user_points = user_points + 1
 
    elif user_choice == "t" and computer_option =="p":
        print("Você ganhou!")
        user_points = user_points + 1

    else:
        print("Você perdeu!")
        computer_points = computer_points + 1 

    print("Sua pontuação: {}" .format(user_points))
    print("Pontuação do computador: {}".format(computer_points))

    if computer_points > user_points:
        print("Derrota!")
    elif computer_points == user_points:
        print("Empate!")
    else:
        print("Vitoria!")

print('Goodbye!')