from loopGame import jogo


while True:
    print("Bem-Vindo ao Jogo de Pedra Papel e Tesoura")
    print("[1] - Jogar\n[2] - Regras\n[3] - Sair")
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        jogo()
    elif opcao == 2:
        print("Regras do Jogo:")
        print("- Pedra ganha da Tesoura e perde para Papel\n- Papel ganha da Pedra e perde para Tesoura\n- Tesoura ganha do "
                "Papel e perde para o Papel\n")
    elif opcao == 3:
        break
