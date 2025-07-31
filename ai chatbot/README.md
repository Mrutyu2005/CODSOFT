# 🤖 CodBot: A Simple Rule-Based Chatbot with a Streamlit UI

Welcome to **CodBot**, a friendly and simple rule-based chatbot built with Python. This project was created by **Mrutyunjay** as part of the **CodSoft AI Internship**.

The chatbot uses regular expressions to recognize user input and provide predefined responses. The user interface is built with Streamlit to create a clean and interactive web-based chat experience.

## ✨ Features

- **Interactive Chat UI**: A clean and modern user interface powered by Streamlit.
- **Rule-Based Responses**: Uses regex pattern matching to understand and respond to user queries.
- **Variety of Topics**: Can handle greetings, goodbyes, questions about itself, the current time, and more.
- **Friendly Persona**: Designed to be a helpful and engaging conversational partner.
- **Easy to Extend**: New rules and responses can be easily added to expand its knowledge base.

## 🛠️ Installation

To run this chatbot on your local machine, please follow these steps.

### Prerequisites

- Python 3.8 or higher
- `pip` (Python package installer)

### Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Mrutyu2005/codsoft.git
    cd codsoft
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

Once the installation is complete, you can start the chatbot by running the following command in your terminal:

```bash
streamlit run chatbot_app.py
