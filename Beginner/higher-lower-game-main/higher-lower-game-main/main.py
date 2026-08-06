import art
import random
import game_data


# Escolhe uma conta aleatória da base de dados
def get_random_account():
    return random.choice(game_data.data)


account_a = get_random_account()
account_b = get_random_account()


# Mostra as contas ao utilizador
def display_accounts():
    print(art.logo)
    print(
        f"Compare A: {account_a['name']}, "
        f"{account_a['description']}, "
        f"from {account_a['country']}"
    )
    print(art.vs)
    print(
        f"Against B: {account_b['name']}, "
        f"{account_b['description']}, "
        f"from {account_b['country']}"
    )


# Determina qual conta tem mais seguidores
def get_correct_answer():
    if account_a["follower_count"] > account_b["follower_count"]:
        return "A"
    else:
        return "B"


# Obtém a escolha do utilizador
def get_user_guess():
    return input(
        "Who has more followers? Type 'A' or 'B': "
    ).upper()


# Função principal do jogo
def play_game():
    global account_a, account_b

    game_should_continue = True
    score = 0

    while game_should_continue:
        display_accounts()

        user_guess = get_user_guess()
        correct_answer = get_correct_answer()

        if user_guess == correct_answer:
            score += 1

            if correct_answer == "A":
                account_a = account_b

            account_b = get_random_account()

            print(f"You're right! Current score: {score}")

        else:
            game_should_continue = False
            print(f"Game Over. Your final score was: {score}")


play_game()





