#!/usr/bin/env python3
"""
Simple Rule-Based Chatbot with a Streamlit UI
Created during CodSoft AI Internship
Author: Mrutyunjay
"""

import re
import random
import datetime
import streamlit as st

class CodSoftChatbot:
    """
    A simple rule-based chatbot class.
    """
    def __init__(self):
        self.name = "CodBot"
        self.creator = "Mrutyunjay"
        self.company = "CodSoft"
        
        # Predefined responses for different categories
        self.greetings = [
            f"Hello! I'm {self.name}, your friendly AI assistant created by {self.creator} during the CodSoft internship! 😊",
            "Hi there! Great to meet you! I'm here to chat and help you out! 🤖",
            "Hey! Welcome! I'm CodBot, ready to have an awesome conversation with you! ✨",
            "Greetings! I'm your AI companion, built with love during my creator's CodSoft journey! 👋"
        ]
        
        self.goodbyes = [
            "Goodbye! It was wonderful chatting with you! Take care! 👋",
            "See you later! Hope to chat again soon! 🌟",
            "Farewell! Thanks for the great conversation! Stay awesome! ✨",
            "Bye for now! Remember, I'm always here when you need a chat! 😊"
        ]
        
        self.how_are_you_responses = [
            "I'm doing fantastic! Thanks for asking! As an AI, I'm always excited to learn and chat! 😄",
            "I'm wonderful! Every conversation makes me better. How are you doing today? 🌟",
            "I'm great! Living my best digital life and loving every interaction! How about you? ⚡",
            "Doing amazing! Ready to tackle any question you throw my way! What's on your mind? 🚀"
        ]
        
        self.weather_responses = [
            "I wish I could check the weather for you! Try asking your weather app or checking online! ☀️",
            "As an AI, I don't have real-time weather data, but I hope it's beautiful where you are! 🌤️",
            "I can't access current weather, but every day is a good day for learning something new! ⛅",
            "No weather powers here, but I can chat about anything else under the sun! 🌈"
        ]
        
        self.about_responses = [
            f"I'm {self.name}, created by {self.creator} during an exciting AI internship at {self.company}! I'm a rule-based chatbot built with Python! 🤖",
            f"I'm an AI chatbot developed as part of {self.creator}'s {self.company} internship project. I use pattern matching to chat with you! 💻",
            f"Hello! I'm {self.name}, a friendly AI assistant. My creator {self.creator} built me during their {self.company} AI internship to show how cool chatbots can be! ⚡"
        ]
        
        self.help_responses = [
            "I can chat about many things! Try asking me about:\n• How I'm doing\n• The time\n• Myself or my creator\n• Or just have a casual conversation! 💬",
            "I'm here to help! You can ask me questions, have a chat, or learn about my creation during the CodSoft internship! What interests you? 🤔",
            "I love helping! I can respond to greetings, answer questions about myself, tell time, or just be your conversation buddy! 😊"
        ]
        
        self.unknown_responses = [
            "That's interesting! I'm still learning, so I might not understand everything yet. Can you tell me more? 🤔",
            "Hmm, I'm not sure about that one! As a rule-based chatbot, I'm always growing. What else would you like to chat about? 💭",
            "I don't quite understand, but I'm eager to learn! Could you rephrase that or ask me something else? 🌟",
            "That's beyond my current knowledge, but I'm always improving! Try asking me about time, or just say hi! 😊"
        ]
        
        self.compliment_responses = [
            "Aww, thank you so much! That makes my circuits happy! My creator Mrutyunjay will be thrilled to hear that! 😊",
            "You're too kind! I'm just doing my best to be helpful and friendly! Thanks for the lovely words! ✨",
            "That's so sweet of you to say! I'm glad I could brighten your day a little! 🌟",
            "Thank you! Comments like yours make all the coding worthwhile! You're awesome too! 🚀"
        ]
    
    @property
    def time_responses(self):
        """Returns a list of time-related responses with the current time."""
        return [
            f"The current time is {datetime.datetime.now().strftime('%I:%M %p')} on {datetime.datetime.now().strftime('%B %d, %Y')}! ⏰",
            f"Right now it's {datetime.datetime.now().strftime('%H:%M')} - time flies when you're having fun chatting! 🕐",
            f"It's {datetime.datetime.now().strftime('%I:%M %p')} - perfect time for a great conversation! ⌚"
        ]

    def preprocess_input(self, user_input):
        """Clean and prepare user input for processing"""
        return user_input.lower().strip()

    def pattern_match(self, user_input, patterns):
        """Check if user input matches any of the given patterns"""
        for pattern in patterns:
            if re.search(pattern, user_input, re.IGNORECASE):
                return True
        return False

    def get_response(self, user_input):
        """Generate appropriate response based on user input"""
        processed_input = self.preprocess_input(user_input)
        
        # Define patterns inside the method to ensure they are always available
        greeting_patterns = [r'\b(hi|hello|hey|greetings|good\s+(morning|afternoon|evening))\b', r'\bhowdy\b', r'what\'s\s+up', r'\bsup\b']
        goodbye_patterns = [r'\b(bye|goodbye|see\s+you|farewell|exit|quit)\b', r'talk\s+to\s+you\s+later', r'catch\s+you\s+later']
        how_are_you_patterns = [r'how\s+are\s+you', r'how\s+are\s+things', r'how\'s\s+it\s+going']
        weather_patterns = [r'\bweather\b', r'(sunny|rainy|cloudy|hot|cold|temperature)', r'how\'s\s+the\s+weather']
        time_patterns = [r'\b(time|clock)\b', r'what\s+time\s+is\s+it', r'current\s+time']
        about_patterns = [r'(who\s+are\s+you|what\s+are\s+you|about\s+you)', r'tell\s+me\s+about\s+yourself', r'who\s+created\s+you', r'who\s+made\s+you', r'\bcodsoft\b']
        help_patterns = [r'\bhelp\b', r'what\s+can\s+you\s+do', r'\bcommands\b', r'\boptions\b']
        compliment_patterns = [r'\b(good|great|awesome|amazing|wonderful|fantastic|cool|nice|smart|clever)\b', r'i\s+like\s+you', r'you\'re\s+(good|great|awesome|amazing|wonderful|fantastic|cool|nice|smart|clever)']

        # Pattern matching and response selection
        if self.pattern_match(processed_input, goodbye_patterns):
            return random.choice(self.goodbyes)
        elif self.pattern_match(processed_input, greeting_patterns):
            return random.choice(self.greetings)
        elif self.pattern_match(processed_input, how_are_you_patterns):
            return random.choice(self.how_are_you_responses)
        elif self.pattern_match(processed_input, weather_patterns):
            return random.choice(self.weather_responses)
        elif self.pattern_match(processed_input, time_patterns):
            return random.choice(self.time_responses)
        elif self.pattern_match(processed_input, about_patterns):
            return random.choice(self.about_responses)
        elif self.pattern_match(processed_input, help_patterns):
            return random.choice(self.help_responses)
        elif self.pattern_match(processed_input, compliment_patterns):
            return random.choice(self.compliment_responses)
        else:
            return random.choice(self.unknown_responses)

def main():
    """Main function to run the Streamlit chatbot UI"""
    
    st.set_page_config(page_title="CodBot", page_icon="🤖")

    # --- CHATBOT INSTANCE & SESSION STATE ---
    # Initialize chatbot instance in session state if it doesn't exist
    if "chatbot" not in st.session_state:
        st.session_state.chatbot = CodSoftChatbot()
    
    # Initialize chat history in session state if it doesn't exist. [1, 2, 4]
    if "messages" not in st.session_state:
        # Start with a welcome message from the chatbot
        st.session_state.messages = [{"role": "assistant", "content": random.choice(st.session_state.chatbot.greetings)}]

    # --- SIDEBAR INFORMATION ---
    with st.sidebar:
        st.title("About CodBot")
        st.info(
            f"**Creator:** {st.session_state.chatbot.creator}\n\n"
            f"**Company:** {st.session_state.chatbot.company}\n\n"
            "This is a simple rule-based chatbot created as part of an AI internship. "
            "It uses regular expressions to recognize patterns and provide appropriate responses. "
            "Feel free to ask about the time, what it can do, or just have a friendly chat!"
        )
        st.markdown("---")
        st.markdown("Type 'help' to see available commands.")
        st.markdown("Type 'bye' or 'quit' to end the chat.")

    # --- MAIN CHAT INTERFACE ---
    st.title("🤖 CodBot: Your Friendly AI Assistant")
    st.write("Created by Mrutyunjay during the CodSoft AI Internship")
    st.markdown("---")

    # Display chat messages from history on app rerun. [7]
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar="🧑‍💻" if message["role"] == "user" else "🤖"):
            st.markdown(message["content"])

    # Accept user input. [2]
    if prompt := st.chat_input("What would you like to say?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user", avatar="🧑‍💻"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant", avatar="🤖"):
            # Get response from the chatbot
            response = st.session_state.chatbot.get_response(prompt)
            st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()