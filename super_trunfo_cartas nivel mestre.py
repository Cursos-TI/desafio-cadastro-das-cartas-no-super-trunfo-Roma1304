import random

class Carta:
    def __init__(self, nome, atributos):
        self.nome = nome
        self.atributos = atributos

    def __str__(self):
        atributos_str = ', '.join([f"{k}: {v}" for k, v in self.atributos.items()])
        return f"{self.nome} -> {atributos_str}"

class Jogador:
    def __init__(self, nome, cartas):
        self.nome = nome
        self.cartas = cartas

    def tem_cartas(self):
        return len(self.cartas) > 0

    def pega_carta(self):
        return self.cartas.pop(0) if self.tem_cartas() else None

    def adiciona_cartas(self, cartas):
        self.cartas.extend(cartas)

def criar_baralho():
    cartas = [
        Carta("Dragão", {"Força": 90, "Velocidade": 70, "Inteligência": 60}),
        Carta("Unicórnio", {"Força": 70, "Velocidade": 80, "Inteligência": 90}),
        Carta("Troll", {"Força": 85, "Velocidade": 40, "Inteligência": 30}),
        Carta("Fada", {"Força": 40, "Velocidade": 90, "Inteligência": 85}),
        Carta("Gigante", {"Força": 95, "Velocidade": 30, "Inteligência": 20}),
        Carta("Elfo", {"Força": 60, "Velocidade": 85, "Inteligência": 75}),
        Carta("Mago", {"Força": 50, "Velocidade": 65, "Inteligência": 95}),
        Carta("Cavaleiro", {"Força": 80, "Velocidade": 75, "Inteligência": 50}),
    ]
    random.shuffle(cartas)
    return cartas

def jogo():
    baralho = criar_baralho()
    metade = len(baralho) // 2
    jogador1 = Jogador(input("Digite o nome do Jogador 1: ") or "Jogador 1", baralho[:metade])
    jogador2 = Jogador(input("Digite o nome do Jogador 2: ") or "Jogador 2", baralho[metade:])
    jogador_atual = jogador1

    rodada = 1
    while jogador1.tem_cartas() and jogador2.tem_cartas():
        print(f"\n=== Rodada {rodada} ===")
        carta1 = jogador1.pega_carta()
        carta2 = jogador2.pega_carta()

        print(f"{jogador1.nome} tem a carta: {carta1}")
        print(f"{jogador2.nome} tem a carta: {carta2}")

        # Jogador ativo escolhe o atributo
        if jogador_atual == jogador1:
            atributos = list(carta1.atributos.keys())
            print(f"Atributos disponíveis: {', '.join(atributos)}")
            escolha = ""
            while escolha.capitalize() not in atributos:
                escolha = input(f"{jogador_atual.nome}, escolha o atributo para disputa: ")
            escolha = escolha.capitalize()
        else:
            # IA simples: escolhe atributo com maior valor
            escolha = max(carta2.atributos, key=carta2.atributos.get)
            print(f"{jogador_atual.nome} escolheu o atributo: {escolha}")

        valor1 = carta1.atributos[escolha]
        valor2 = carta2.atributos[escolha]

        print(f"{jogador1.nome} tem {valor1} de {escolha}")
        print(f"{jogador2.nome} tem {valor2} de {escolha}")

        if valor1 > valor2:
            print(f"{jogador1.nome} ganha a rodada!")
            jogador1.adiciona_cartas([carta1, carta2])
            jogador_atual = jogador1
        elif valor2 > valor1:
            print(f"{jogador2.nome} ganha a rodada!")
            jogador2.adiciona_cartas([carta1, carta2])
            jogador_atual = jogador2
        else:
            print("Empate! Cada um fica com sua carta.")
            jogador1.adiciona_cartas([carta1])
            jogador2.adiciona_cartas([carta2])

        print(f"Cartas {jogador1.nome}: {len(jogador1.cartas)} | Cartas {jogador2.nome}: {len(jogador2.cartas)}")
        rodada += 1

    if jogador1.tem_cartas():
        print(f"\n{jogador1.nome} venceu o jogo!")
    else:
        print(f"\n{jogador2.nome} venceu o jogo!")

if __name__ == "__main__":
    jogo()