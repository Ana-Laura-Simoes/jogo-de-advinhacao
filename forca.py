
def jogar():
    print("********************************")
    print("Bem vindo ao Jogo da Forca!")
    print("********************************")

    palavra_secreta = "banana".upper()
    enforcou = False
    acertou = False
    erros = 0
    letras_acertadas = []

    for letra in palavra_secreta:
        letras_acertadas.append(" _ ")

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = " _ " not in letras_acertadas
        print(letras_acertadas)

    print("Fim de jogo!")




if (__name__ == "__main__"):
    jogar()