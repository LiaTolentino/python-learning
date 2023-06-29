import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("\n(1) Fácil \n(2) Médio \n(3) Difícil \n")

    nivel = int(input("Defina o nível de dificuldade desejada: \n"))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"\nTentativa {rodada} de {total_de_tentativas}")    
        chute = int(input("Digite um número entre 1 e 100: \n"))

        print(f"\nVocê digitou o número: {chute}")

        if chute < 1 or chute > 100:
            print(f"Você deve digitar um número entre 1 e 100. Você dogitou o número {chute}\n")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou :
            print(f"\nVocê acertou e fez {pontos} pontos!")
            break
        else:
            if maior:
                print("\nVocê errou! O seu chute foi maior do que o número secreto")
            elif menor:
                print("\nVocê errou! O seu chute foi menor do que o número secreto")
            
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("\nFim de Jogo!")

if(__name__ == "__main__"):
    jogar()
    