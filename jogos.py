import forca
import advinhacao

def escolhe_jogo():
    print("********************************")
    print("        Jogos em Python         ")
    print("********************************")
    print("(1) Forca \n(2)Advinhaçao")

    jogo = int(input("Qual jogo você gostaria?"))

    if (jogo == 1):
        forca.jogar()

    elif (jogo == 2):
        advinhacao.jogar()

    else:
        print("Opcao Inválida!!")

if (__name__ == "__main__"):
    escolhe_jogo()