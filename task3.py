import nltk
import random
import string

from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize

# Sample responses (you can expand this)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"how are you ?",
        ["I'm just a bot, but I'm doing great! How can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["You can call me ChatBot!", "I'm your friendly assistant."]
    ],
    [
        r"(.*) your name ?",
        ["My name is ChatBot."]
    ],
    [
        r"(.*) help (.*)",
        ["Sure! I'm here to help you. Ask me anything."]
    ],
    [
        r"quit|exit",
        ["Goodbye! Have a great day!", "See you soon!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase?", 
         "Interesting... tell me more!", 
         "Let's talk about something else."]
    ]
]

# Create and start the chatbot
def start_chat():
    print("Hi! I'm your chatbot. Type 'quit' or 'exit' to end the conversation.\n")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Run the chatbot
if __name__ == "__main__":
    start_chat()
