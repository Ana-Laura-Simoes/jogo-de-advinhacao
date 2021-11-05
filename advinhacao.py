print("********************************")
print("Bem vindo ao Jogo de Advinhação!")
print("********************************")

numero_secreto = 42
numero_advinhado= int(input("Tente advinhar o número secreto:"))

if(numero_advinhado == numero_secreto):
    print("UAU! Você acertou!!")

else:
    print("Que pena! Você errou!!")
