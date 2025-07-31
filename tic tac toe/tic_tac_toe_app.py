# tic_tac_toe_app.py
# Created by Mrutyunjay during CodSoft AI Internship
# Final corrected version with real-time updates using on_click

import streamlit as st
import time

# --- Game Logic (Unchanged) ---

def check_winner(board):
    """Checks for a winner (X, O), a Draw, or None if the game continues."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    if all(cell != "" for row in board for cell in row):
        return "Draw"
    return None

def minimax(board, is_ai):
    """Minimax algorithm to determine the best score."""
    winner = check_winner(board)
    if winner == "O": return 1
    if winner == "X": return -1
    if winner == "Draw": return 0

    if is_ai:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = ""
                    best_score = min(score, best_score)
        return best_score

def ai_move(board):
    """Determines the best move for the AI."""
    best_score = -float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# --- Streamlit UI and State Logic ---

st.set_page_config(page_title="Tic-Tac-Toe AI", page_icon="⚔️")

def handle_click(i, j):
    """This function is called when a human player clicks a button."""
    # Prevent moves if game is over or cell is taken
    if st.session_state.game_over or st.session_state.board[i][j] != "":
        return

    # Human's move
    st.session_state.board[i][j] = "X"
    
    # Check for winner after human move
    winner = check_winner(st.session_state.board)
    if winner:
        st.session_state.game_over = True
        st.session_state.winner = winner
        return

    # AI's move
    st.session_state.message = "AI is thinking..."
    # A short delay to make the AI's move feel more natural
    time.sleep(0.5) 
    
    ai_r, ai_c = ai_move(st.session_state.board)
    if ai_r is not None:
        st.session_state.board[ai_r][ai_c] = "O"
    
    # Check for winner after AI move
    winner = check_winner(st.session_state.board)
    if winner:
        st.session_state.game_over = True
        st.session_state.winner = winner
    else:
        st.session_state.message = "Your turn."

# --- Main App Layout ---

st.title("⚔️ Tic-Tac-Toe with Minimax AI")
st.write("Created by **Mrutyunjay** during the **CodSoft AI Internship**.")

# Initialize or reset the game state using a button in the sidebar
if st.sidebar.button("New Game", key="new_game"):
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.game_over = False
    st.session_state.winner = None
    st.session_state.message = "You are 'X'. Make your move."

# Initialize state for the first run
if "board" not in st.session_state:
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.game_over = False
    st.session_state.winner = None
    st.session_state.message = "You are 'X'. Make your move."

# Sidebar with game info
st.sidebar.title("Game Info")
st.sidebar.info(
    "This Tic-Tac-Toe game uses the **Minimax algorithm** for its AI opponent. "
    "The AI will always play an optimal move, making it impossible to beat. "
    "The best you can achieve is a draw!"
)

# Display the game status message
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.info("Game Over! It's a Draw.")
    elif st.session_state.winner == "X":
        st.success("Game Over! Congratulations, you win!")
    else:
        st.error("Game Over! The AI wins. Better luck next time.")
else:
    st.write(st.session_state.message)

# Create the Tic-Tac-Toe grid
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            # Each button is a cell in the grid
            st.button(
                label=st.session_state.board[i][j] or " ",
                key=f"btn_{i}_{j}",
                use_container_width=True,
                disabled=st.session_state.game_over,
                on_click=handle_click,
                args=(i, j)
            )

# Apply some custom CSS for bigger buttons and text
st.markdown("""
<style>
    div[data-testid*="stButton"] > button {
        height: 100px;
        font-size: 2.5em;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)