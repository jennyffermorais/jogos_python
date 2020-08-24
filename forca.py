def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra?")        
        chute = chute.strip() #para tirar os espaço do início e do final do que for digitado no input

        index = 0

        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}.".format(letra, index))

            index = index + 1

        print("Jogando...")

    print("Fim do jogo!")

# se executar o forca como programa principal a
# variável name recebe o valor main
if(__name__ == "__main__"):
    jogar()