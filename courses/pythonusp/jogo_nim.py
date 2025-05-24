def computador_escolhe_jogada(n, m):
    for i in range(1, m + 1):
        if (n - i) % (m + 1) == 0:
            return i
    return min(m, n)

def usuario_escolhe_jogada(n, m):
    jogada_valida = False
    while not jogada_valida:
        try:
            jogada = int(input("Quantas peças você vai tirar? "))
            if 1 <= jogada <= min(m, n):
                jogada_valida = True
            else:
                print("Oops! Jogada inválida! Tente de novo.")
        except ValueError:
            print("Por favor, digite um número válido.")
    return jogada

def partida():
    print("Quantas peças?")
    n = int(input("Digite o número total de peças: "))
    print("Limite de peças por jogada?")
    m = int(input("Digite o limite de peças por jogada: "))

    if n % (m + 1) == 0:
        print("\nVocê começa!")
        turno = "usuario"
    else:
        print("\nComputador começa!")
        turno = "computador"

    while n > 0:
        if turno == "usuario":
            jogada = usuario_escolhe_jogada(n, m)
            print(f"\nVocê tirou {jogada} peça(s).")
            turno = "computador"
        else:
            jogada = computador_escolhe_jogada(n, m)
            print(f"\nO computador tirou {jogada} peça(s).")
            turno = "usuario"
        
        n -= jogada
        if n > 0:
            print(f"Agora restam {n} peça(s) no tabuleiro.")
        else:
            print("Fim do jogo!")
            if turno == "usuario":
                print("O computador ganhou!")
                return "computador"
            else:
                print("Você ganhou!")
                return "usuario"

def jogo_nim():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    opcao = int(input("\nEscolha sua opção: "))

    numero_de_partidas = 1 if opcao == 1 else 3
    placar_computador = 0
    placar_jogador = 0

    for rodada in range(1, numero_de_partidas + 1):
        if numero_de_partidas == 3:
            print(f"\n**** Rodada {rodada} ****")

        vencedor = partida()
        if vencedor == "computador":
            placar_computador += 1
        else:
            placar_jogador += 1

    if placar_computador + placar_jogador == 3:
        print("\n**** Final do campeonato! ****")
        print(f"Placar: Você {placar_jogador} X {placar_computador} Computador")
    else:
        print(f"\nPlacar final: Você {placar_jogador} X {placar_computador} Computador")
jogo_nim()