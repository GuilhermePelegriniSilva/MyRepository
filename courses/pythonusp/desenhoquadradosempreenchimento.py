largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))
for i in range(altura):
    for j in range(largura):
        if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()