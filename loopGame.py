import random
import time
from colorama import Fore

maos = ["Pedra", "Papel", "Tesoura"]

def jogo():
    pontos = 0
    pontosIni = 0
    suaEscolha = ''

    while True:
        # Verificar vitória:
        if pontos >= 3:
            time.sleep(1.5)
            print("🎉 VOCÊ GANHOU O JOGO🎉")
            time.sleep(1.5)
            print("\n" * 15)
            break
        elif pontosIni >= 3:
            time.sleep(1.5)
            print("😞 VOCÊ PERDEU O JOGO😞")
            time.sleep(1.5)
            print("\n" * 15)
            break

        # Menu do Jogo
        time.sleep(1.5)
        print(f"\nSeus Pontos: {pontos}\nPontos Oponente: {pontosIni}\n")
        print("Faça sua escolha: ")
        print("[1] - Pedra\n[2] - Papel\n[3] - Tesoura")
        suaMao = int(input("Faça sua escolha: "))
        if suaMao > 3:
            print("Opção errada!\nTente novamente")
            continue
        BotMao = random.choice(maos)

        if suaMao == 1:
            suaEscolha = "Pedra"
        elif suaMao == 2:
            suaEscolha = "Papel"
        elif suaMao == 3:
            suaEscolha = "Tesoura"

        print(f"Você jogou: {Fore.BLUE}{suaEscolha}{Fore.RESET}!\nSeu inimigo: {Fore.RED}{BotMao}{Fore.RESET}!")
        time.sleep(0.5)

        # Verificação dos Pontos
        if BotMao == "Pedra" and suaMao == 2:
            print(Fore.GREEN + "✅ Você ganhou!" + Fore.RESET)
            pontos += 1
            continue
        elif BotMao == "Papel" and suaMao == 2:
            print(Fore.WHITE + "🤝 Empate" + Fore.RESET)
            continue
        elif BotMao == "Tesoura" and suaMao == 2:
            print(Fore.RED + "❌ Você Perdeu!" + Fore.RESET)
            pontosIni += 1
            continue

        elif BotMao == "Papel" and suaMao == 1:
            print(Fore.RED + "❌ Você Perdeu!" + Fore.RESET)
            pontosIni += 1
            continue
        elif BotMao == "Pedra" and suaMao == 1:
            print(Fore.WHITE + "🤝 Empate" + Fore.RESET)
            continue
        elif BotMao == "Tesoura" and suaMao == 1:
            print(Fore.GREEN + "✅ Você ganhou!" + Fore.RESET)
            pontos += 1
            continue

        elif BotMao == "Papel" and suaMao == 3:
            print(Fore.GREEN + "✅ Você ganhou!" + Fore.RESET)
            pontos += 1
            continue
        elif BotMao == "Pedra" and suaMao == 3:
            print(Fore.RED + "❌ Você Perdeu!" + Fore.RESET)
            pontosIni += 1
            continue
        elif BotMao == "Tesoura" and suaMao == 3:
            print(Fore.WHITE + "🤝 Empate" + Fore.RESET)
            continue