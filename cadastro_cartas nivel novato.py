cartas = []

try:
    n = int(input("Quantas cartas deseja cadastrar? "))
except ValueError:
    print("Entrada inválida. Usando 3 cartas por padrão.")
    n = 3

for i in range(n):
    print(f"\nCadastro da carta #{i + 1}")
    nome = input("Nome da carta: ").strip()
    while nome == "":
        nome = input("Nome não pode ser vazio. Digite novamente: ").strip()

    # Entrada segura para inteiros entre 0 e 100
    while True:
        try:
            ataque = int(input("Ataque (0-100): "))
            if 0 <= ataque <= 100:
                break
            print("Valor fora do intervalo.")
        except ValueError:
            print("Digite um número inteiro.")

    while True:
        try:
            defesa = int(input("Defesa (0-100): "))
            if 0 <= defesa <= 100:
                break
            print("Valor fora do intervalo.")
        except ValueError:
            print("Digite um número inteiro.")

    while True:
        try:
            velocidade = int(input("Velocidade (0-100): "))
            if 0 <= velocidade <= 100:
                break
            print("Valor fora do intervalo.")
        except ValueError:
            print("Digite um número inteiro.")

    especial = input("Poder especial (opcional): ")

    carta = {
        "Nome": nome,
        "Ataque": ataque,
        "Defesa": defesa,
        "Velocidade": velocidade,
        "Especial": especial
    }

    cartas.append(carta)

print("\nCartas cadastradas:")
for idx, c in enumerate(cartas, 1):
    print("------------------------")
    print(f"Carta #{idx}")
    for chave, valor in c.items():
        print(f"{chave}: {valor if valor != '' else '-'}")