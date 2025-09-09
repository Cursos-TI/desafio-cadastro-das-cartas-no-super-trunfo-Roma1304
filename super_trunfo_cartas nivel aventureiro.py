import random

# Lista de cartas
cartas = [
    {"nome": "Dragão Flamejante", "força": 90, "magia": 70, "velocidade": 60},
    {"nome": "Guerreiro das Sombras", "força": 75, "magia": 60, "velocidade": 80},
    {"nome": "Feiticeiro Ancião", "força": 50, "magia": 95, "velocidade": 40},
    {"nome": "Elfa Veloz", "força": 60, "magia": 55, "velocidade": 95},
    {"nome": "Gigante da Montanha", "força": 95, "magia": 30, "velocidade": 25},
]

def escolher_carta(baralho):
    # Remove carta sorteada do baralho e retorna
    return baralho.pop(random.randint(0, len(baralho) - 1))

def exibir_carta(carta):
    print(f"\nCarta: {carta['nome']}")
    for atributo in ["força", "magia", "velocidade"]:
        print(f"{atributo.capitalize()}: {carta[atributo]}")

def jogar_rodada(baralho_jogador, baralho_computador):
    jogador = escolher_carta(baralho_jogador)
    computador = escolher_carta(baralho_computador)

    print("\n--- Sua Carta ---")
    exibir_carta(jogador)

    atributos_validos = ["força", "magia", "velocidade"]
    escolha = input("Escolha um atributo para competir (força, magia, velocidade): ").lower()
    while escolha not in atributos_validos:
        escolha = input("Atributo inválido. Digite força, magia ou velocidade: ").lower()

    print("\n--- Carta do Computador ---")
    exibir_carta(computador)

    print(f"\nVocê ({jogador[escolha]}) x ({computador[escolha]}) Computador em {escolha.capitalize()}")

    if jogador[escolha] > computador[escolha]:
        print("\n✅ Você venceu esta rodada!")
        return 1
    elif jogador[escolha] < computador[escolha]:
        print("\n❌ Você perdeu esta rodada!")
        return -1
    else:
        print("\n⚔️ Empate!")
        return 0

def jogar():
    pontos = 0
    rodadas = 3
    for i in range(rodadas):
        print(f"\n======== Rodada {i+1} ========")
        # Faz cópias para que cada rodada não tenha repetição de cartas.
        baralho_jogador = cartas[:]
        baralho_computador = cartas[:]
        resultado = jogar_rodada(baralho_jogador, baralho_computador)
        pontos += resultado
    print("\n===== Fim do Jogo =====")
    if pontos > 0:
        print("🎉 Parabéns, você venceu o jogo!")
    elif pontos < 0:
        print("💀 Você perdeu o jogo. Tente novamente!")
    else:
        print("⚖️ O jogo terminou empatado.")

# Início do jogo
jogar()