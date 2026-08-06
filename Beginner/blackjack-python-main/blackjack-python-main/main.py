# importações de bibliotecas

import random # para seleção aleatoria
import art #onde está o logo tipo

print(art.logo)

cartas = {
    "2": 2,                #lista de cartas -------------
    "3": 3,                #------------------------------
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10":10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}

mao_jogador = []
mao_bot = []
pontos_jogador = 0
pontos_bot = 0

def regras_games():
    global game, primeira_ronda

    pontos_jogador = calcular_pontos_jogador()
    pontos_bot = calcular_pontos_bot()

    # Blackjack
    if pontos_jogador == 21 and len(mao_jogador) == 2:
        game = False
        print("Blackjack")
        return

    if pontos_bot == 21 and len(mao_bot) == 2:
        game = False
        print("Blackjack do bot")
        return

    # Regras imediatas
    if pontos_jogador > 21:
        game = False
        print("Jogador perdeu")
        return

    if pontos_bot > 21:
        game = False
        print("Jogador Venceu")
        return

    # Regras finais — só depois da primeira ronda
    if primeira_ronda == False:
        if pontos_bot > pontos_jogador:
            game = False
            print("Jogador perdeu")

        elif pontos_bot < pontos_jogador:
            game = False
            print("Jogador Venceu")

        else:
            game = False
            print("Game Over")

# distribuição de cartas para o jogador
def distribuir_jogador():
    carta1 = random.choice(list(cartas.keys()))
    carta2 = random.choice(list(cartas.keys()))
    result = carta1, carta2
    mao_jogador.append(carta1)
    mao_jogador.append(carta2)
    print("Cartas do jogador: ")
    print(" | ".join(mao_jogador))
    pontos_jogador = calcular_pontos_jogador()
    print(f"Pontos do jogador: {pontos_jogador}\n")


def uma_carta_jogador():
    carta = random.choice(list(cartas.keys()))
    result = carta
    mao_jogador.append(carta)
    print("Cartas do jogador: ")
    print(" | ".join(mao_jogador))
    pontos_jogador = calcular_pontos_jogador()
    print(f"Pontos do jogador: {pontos_jogador}\n")


# distibuição de cartas para o bot
def distribuir_bot():
    carta1 = random.choice(list(cartas.keys()))
    carta2 = random.choice(list(cartas.keys()))
    result = carta1, carta2
    mao_bot.append(carta1)
    mao_bot.append(carta2)
    print("Cartas do bot: ")
    print(" | ".join(mao_bot))
    pontos_bot = calcular_pontos_bot()
    print(f"Pontos do bot: {pontos_bot}\n")



def uma_carta_bot():
    carta = random.choice(list(cartas.keys()))
    result = carta
    mao_bot.append(carta)
    print("Cartas do bot: ")
    print(" | ".join(mao_bot))
    pontos_bot = calcular_pontos_bot()
    print(f"Pontos do bot: {pontos_bot}\n")

def primerira_jogada():
    distribuir_jogador()
    distribuir_bot()

def calcular_pontos_jogador():
    pontos = 0

    for carta in mao_jogador:
        pontos += cartas[carta]

    if pontos > 21 and "A" in mao_jogador:
        pontos -= 10

    return pontos

def calcular_pontos_bot():
    pontos = 0

    for carta in mao_bot:
        pontos += cartas[carta]

    if pontos > 21 and "A" in mao_bot:
        pontos -= 10

    return pontos



game = True
primeira_ronda = True

while game:
    if mao_jogador == [] and mao_bot == []:
        primerira_jogada()
        regras_games()

    if not game:
        break

    jogador_ativo = True

    while jogador_ativo and game:
        continuar = input("Deseja continuar Jogador? [S/N] ").upper()

        if continuar == "S":
            uma_carta_jogador()
            regras_games()

        elif continuar == "N":
            jogador_ativo = False

    while calcular_pontos_bot() < 17 and game:
        uma_carta_bot()
        regras_games()

    if game:
        primeira_ronda = False
        regras_games()

    game = False





