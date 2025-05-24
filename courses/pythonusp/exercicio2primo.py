def eh_primo(k):
    if k < 2:
        return False
    for i in range(2, int(k**0.5) + 1):
        if k % i == 0:
            return False
    return True
def maior_primo(n):
    maior = 2
    for i in range(2, n + 1):
        if eh_primo(i):
            maior = i
    return maior
numero = int(input("Digite um número maior ou igual a 2: "))
print(f"O maior primo menor ou igual a {numero} é: {maior_primo(numero)}")