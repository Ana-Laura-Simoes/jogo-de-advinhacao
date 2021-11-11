
def jogar():
    print("********************************")
    print("Bem vindo ao Jogo da Forca!")
    print("********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou= False
    letras_acertadas = []

    for letra in palavra_secreta:
        letras_acertadas.append(" _ ")

    while (not enforcou and not acertou):
        chute = input("Qual letra? ")
        #tirando os espaços do chute(se tiver)
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)




if (__name__ == "__main__"):
    jogar()