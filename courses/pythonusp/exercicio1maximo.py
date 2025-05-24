def maximo(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return n1
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
resultado = maximo(n1, n2)
print(f"O maior número entre {n1} e {n2} é: {resultado}")