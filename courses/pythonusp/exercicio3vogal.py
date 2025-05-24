def vogal(letra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    return letra.lower() in vogais
letra = input("Digite uma letra: ")
if len(letra) != 1:
    print("Por favor, insira apenas uma única letra.")
else:
    resultado = vogal(letra)
    if resultado:
        print(f"'{letra}' é uma vogal (True).")
    else:
        print(f"'{letra}' não é uma vogal (False).")