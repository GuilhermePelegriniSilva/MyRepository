def maximo(n1, n2):
    if n1 == n2:
        print("Os números são iguais, não dá para comparar")
    elif n1 > n2:
        print(f"{n1} é maior que {n2}")
    else:
        print(f"{n2} é maior que {n1}")
    return 0
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
maximo(n1, n2)
