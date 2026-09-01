import nltk
from nltk.chat.util import Chat, reflections


# Download required NLTK data
nltk.download("punkt", quiet=True)
nltk.download("averaged_perceptron_tagger", quiet=True)


# Predefined patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        [
            "Hello! How can I help you today?",
            "Hi there! How may I assist you?"
        ]
    ],

    [
        r"my name is (.*)",
        [
            "Hello %1! How can I assist you today?"
        ]
    ],

    [
        r"(.*) your name\?",
        [
            "I am your friendly rule-based chatbot!"
        ]
    ],

    [
        r"how are you\?",
        [
            "I'm just a bot, but I'm doing well! How about you?"
        ]
    ],

    [
        r"tell me a joke",
        [
            "Why don't skeletons fight each other? They don't have the guts!"
        ]
    ],

    [
        r"(.*) (help|assist) (.*)",
        [
            "Sure! How can I assist you with %3?"
        ]
    ],

    [
        r"what can you do\?",
        [
            "I can respond to greetings, remember your name during a conversation, "
            "tell jokes, and answer some predefined questions."
        ]
    ],

    [
        r"thank you|thanks",
        [
            "You're welcome!",
            "Happy to help!"
        ]
    ],

    [
        r"bye|exit|quit",
        [
            "Goodbye! Have a great day!",
            "See you later!"
        ]
    ],

    [
        r"(.*)",
        [
            "I'm sorry, I didn't understand that. Could you rephrase?",
            "Could you please elaborate?"
        ]
    ]
]


class RuleBasedChatbot:
    """A simple rule-based chatbot using NLTK."""

    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)

    def respond(self, user_input):
        """Generate a response based on the user's input."""
        return self.chat.respond(user_input)


def chat_with_bot():
    """Start an interactive conversation with the chatbot."""

    print("=" * 50)
    print("       RULE-BASED CHATBOT")
    print("=" * 50)
    print("Hello! I am your chatbot.")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")
    print("-" * 50)

    chatbot = RuleBasedChatbot(pairs)

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Chatbot: Please enter something.")
            continue

        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot.respond(user_input)

        if response:
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I'm sorry, I didn't understand that.")


if __name__ == "__main__":
    chat_with_bot()
