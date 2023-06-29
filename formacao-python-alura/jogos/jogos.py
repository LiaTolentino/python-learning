import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("\n(1) Jogo da Forca \n(2) Jogo de Adivinhação")

    jogo = int (input("\nQual o seu jogo? "))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
    