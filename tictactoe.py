# Simple Tic Tac Toe in Python

# Español:
# Imprime el tablero en consola mostrando las casillas separadas por líneas.
#
# Português:
# Imprime o tabuleiro no console mostrando as casas separadas por linhas.
def print_board(board):
    for row in board:
        print(" | ".join(row))
        #print("-" * 5)


# Español:
# Verifica si el jugador actual ha ganado revisando filas, columnas y diagonales.
#
# Português:
# Verifica se o jogador atual venceu verificando linhas, colunas e diagonais.
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False


# Español:
# Verifica si el tablero está lleno (empate).
#
# Português:
# Verifica se o tabuleiro está cheio (empate).
def is_board_full(board):
    pass


# Español:
# Controla el flujo del juego:
# - Inicializa el tablero
# - Alterna turnos entre los jugadores X y O
# - Pide coordenadas al usuario
# - Comprueba victorias o empate
#
# Português:
# Controla o fluxo do jogo:
# - Inicializa o tabuleiro
# - Alterna turnos entre os jogadores X e O
# - Solicita coordenadas ao usuário
# - Verifica vitórias ou empate
def game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Choose row (0-2): "))
            col = int(input("Choose column (0-2): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if row not in range(3) or col not in range(3):
            print("Move out of range. Try again.")
            continue

        if board[row][col] != " ":
            print("Cell already occupied. Try again.")
            continue

        board[row][col] = current_player

        # Switch player
        ##current_player = "O" if current_player == "X" else "X"


# Start game
game()
