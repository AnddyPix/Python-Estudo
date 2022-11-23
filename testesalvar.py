import random

terminar = False
contador = -1
print("\033[1;32m=\033[m"*30)
print(f"{'JOGO DE ADVINHAÇÃO':^30}")
print("\033[1;32m=\033[m"*30)
print("ESCOLHA UMA DIFÍCULDADE:\n1- FÁCIL\n2- MEDIO\n3- DÍFICIL\n0- SAIR")
menu = int(input("Qual a opção desejada: "))
while True:
    if menu == 0:
        print("Obrigado por JOGAR!!!")
        break
    elif menu == 1:
        computador = random.randint(1, 20)
        #print(computador)
        while not terminar:
            #print(contador)
            pessoa = int(input("Escolha um número de 1 a 20: "))
            contador += 1
            if contador == 7:
                print("Você \033[31mPERDEU\033[m")#COLORIR PERDEU
                terminar = True
            if pessoa < computador and contador != 7:
                print("Tente um valor maior!")
            elif pessoa > computador and contador != 7:
                print("Tente um valor menor!")
            elif pessoa == computador:
                print("PARABÉNS, você \033[34mVENCEU\033[m")#COLORIR VENCEU
                terminar = True
        fim = str(input("Deseja continuar \033[36m[S/N]\033[m? ")).strip().upper()[0]
        if fim == "S":
            terminar = False
            contador = -1
            print("ESCOLHA UMA DIFÍCULDADE:\n1- FÁCIL\n2- MEDIO\n3- DÍFICIL\n0- SAIR")
            menu = int(input("Qual a opção desejada: "))
        elif fim == "N":
            print("Obrigado por Jogar!")
            print("\033[1;32m=\033[m"*30)
            break
        else:
                print("Opção inválida. Tente novamente!")
                fim = str(input("Deseja continuar \033[36m[S/N]\033[m? ")).strip().upper()[0]
    elif menu == 2:
        computador = random.randint(1, 12)
        #print(computador)
        while not terminar:
            pessoa = int(input("Escolha um número de 1 a 12: "))
            contador += 1
            #print(contador)
            if contador == 4:
                print("Você \033[31mPERDEU\033[m")# COLORIR PERDEU
                terminar = True
            if pessoa < computador and contador != 4:
                print("Tente um valor maior!")
            elif pessoa > computador and contador != 4:
                print("Tente um valor menor!")
            elif pessoa == computador:
                print("PARABÉNS, você \033[34mVENCEU\033[m")# COLORIR VENCEU
                terminar = True
        fim = str(input("Deseja continuar \033[36m[S/N]\033[m? ")).strip().upper()[0]
        if fim == "S":
            terminar = False
            contador = -1
            print("ESCOLHA UMA DIFÍCULDADE:\n1- FÁCIL\n2- MEDIO\n3- DÍFICIL\n0- SAIR")
            menu = int(input("Qual a opção desejada: "))
        elif fim == "N":
            print("Obrigado por Jogar!")
            print("\033[1;32m=\033[m"*30)
            break
        else:
            print("Opção inválida. Tente novamente!")
            fim = str(input("Deseja continuar \033[36m[S/N]\033[m? ")).strip().upper()[0]
    elif menu == 3:
        computador = random.randint(1, 10)
        #print(computador)
        while not terminar:
            #print(contador)
            pessoa = int(input("Escolha um número de 1 a 10: "))
            contador += 1
            if contador == 3:
                print("Você \033[31mPERDEU\033[m")  # COLORIR PERDEU
                terminar = True
            if pessoa < computador and contador != 3:
                print("Tente um valor \033[31mmaior\033[m!")
            elif pessoa > computador and contador != 3:
                print("Tente um valor \033[34mmenor\033[m!")
            elif pessoa == computador:
                print("PARABÉNS, você \033[34mVENCEU\033[m")# COLORIR VENCEU
                terminar = True
        fim = str(input("Deseja continuar \033[36m[S/N]\033[m? ")).strip().upper()[0]
        if fim == "S":
            terminar = False
            contador = -1
            print("ESCOLHA UMA DIFÍCULDADE:\n1- FÁCIL\n2- MEDIO\n3- DÍFICIL\n0- SAIR")
            menu = int(input("Qual a opção desejada: "))
        elif fim == "N":
            print("Obrigado por Jogar!")
            print("\033[1;32m=\033[m"*30)
            break
        else:
            print("Opção inválida. Tente novamente!")
            fim = str(input("Deseja continuar \033[36m[S/N]\033[m?")).strip().upper()[0]
    else:
        print("Opçãp \033[33mINVÁLIDA\033[m. Tente novamente")#colorir invalida
        print("ESCOLHA UMA DIFÍCULDADE:\n1- FÁCIL\n2- MEDIO\n3- DÍFICIL\n0- SAIR")
        menu = int(input("Qual a opção desejada: "))


