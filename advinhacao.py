import random

print("********************************")
print("Bem vindo ao Jogo de Advinhação!")
print("********************************")

numero_secreto = random.randrange(1,101)
total_tentativas = 3
tentativa=0

while(tentativa < total_tentativas):

    tentativa = tentativa + 1

    print(f"Tentativa {tentativa} de {total_tentativas}")

    numero_advinhado = int(input("Digite um número entre 1 e 100:"))

    if(numero_advinhado < 1 or numero_advinhado > 100):
        print("Valor inválido!")
        continue

    acertou = numero_advinhado == numero_secreto
    maior = numero_advinhado > numero_secreto
    menor = numero_advinhado < numero_secreto

    if (acertou):
        print("UAU! Você acertou!!")
        break

    elif (maior):
        print("Você errou! Seu chute foi maior do que o número secreto!")

    elif (menor):
        print("Você errou! Seu chute foi menor do que o número secreto!")

    else:
        print("Que pena! Você errou!!")

print("Fim de Jogo!")