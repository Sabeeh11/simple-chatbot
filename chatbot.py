# %%
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# %%
# Function to preprocess user input
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    doc = nlp(text)  # Process the text using spaCy
    tokens = [token.text for token in doc]  # Tokenize using spaCy
    return " ".join(tokens)


# %%
# Predefined set of more diverse responses
responses = {
    "hello": "Hey there! 👋 How can I help you today?",
    "hi": "Hello! 🙂 What brings you here?",
    "hey": "Hi! I'm here if you need anything.",
    "how are you": "I'm functioning within normal parameters! 😄 How about you?",
    "what is your name": "You can call me ChatBot 🤖. What's your name?",
    "who are you": "I'm your friendly Python-powered assistant!",
    "bye": "Take care! 👋 See you again soon.",
    "goodbye": "Goodbye! Come back anytime!",
    "thanks": "You're welcome! 😊",
    "thank you": "Always happy to help!",
    "what can you do": "I can chat, answer simple questions, and keep you company. 😊",
    "help": "I'm here to answer your questions or just chat!",
    "default": "Hmm... I'm not sure how to respond to that 🤔"
}

# %%
# Function to get the appropriate response
def get_response(user_input):
    user_input = preprocess_text(user_input)
    for key in responses.keys():
        if key in user_input:
            return responses[key]
    return responses["default"]

# %%
# Interactive chat loop
print("ChatBot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatBot: Goodbye! Have a great day! 👋")
        break
    response = get_response(user_input)
    print(f"ChatBot: {response}")

# %%
