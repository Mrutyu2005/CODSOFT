# ⚔️ Tic-Tac-Toe with an Unbeatable AI

This project is a classic Tic-Tac-Toe game with a graphical user interface where you can play against an AI that is impossible to beat. The AI's logic is powered by the Minimax algorithm, ensuring it always makes the optimal move.

This application was created by Mrutyunjay as part of the CodSoft AI Internship and features a clean, web-based UI built with Streamlit.


---

## ✨ Features

-   Interactive Web UI: A modern and responsive user interface built with Streamlit, which you can run in your browser.
-   Unbeatable AI Opponent: Play against an AI that uses the Minimax algorithm to predict moves and play optimally. You can never win—the best you can do is a draw!
-   Real-time Updates: The game board updates instantly after each move.
-   Clear Game State: Get notifications for whose turn it is, and see a clear message when the game ends (win, loss, or draw).
-   Reset and Replay: Start a "New Game" at any time with a simple button click.

---

## 🛠 How It Works

The project consists of two main parts:

1.  Game Logic (Backend): This is the core of the game, written in pure Python. The minimax function is a recursive algorithm that explores all possible future moves in the game. It assigns a score to each move, allowing the AI to choose the path that leads to the best possible outcome (a win, or a draw if a win isn't possible).

2.  User Interface (Frontend): The UI is built using the Streamlit library. It creates the game board, buttons, and status messages. Streamlit's state management (st.session_state) is used to keep track of the board, whose turn it is, and whether the game is over. The on_click callback for each button ensures that both the human and AI moves are processed instantly for a smooth user experience.

---

## 🚀 Getting Started

Follow these instructions to get the game running on your local machine.

### Prerequisites

-   Python 3.8 or newer
-   pip (Python's package installer)

### Installation & Setup

1.  Clone the repository (or simply download the files into a new folder):
        git clone https://github.com/your-username/tic-tac-toe-ai.git
    cd tic-tac-toe-ai
    

2.  Create and activate a virtual environment (recommended):
        # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    

3.  Install the required packages from the requirements.txt file:
        pip install -r requirements.txt
    

### Running the Game

With your virtual environment active and packages installed, run the following command in your terminal:

```bash
streamlit run tic_tac_toe_app.py