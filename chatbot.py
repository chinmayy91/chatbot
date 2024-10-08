import random

# Define some sample responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm doing well, thanks for asking!", "I'm great! How about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "chinmay": ["you are smart", "you can get more info from him"],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase that?", "I don't understand. Can you try asking something else?"]
}

def get_response(user_input):
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()
    
    # Check if the input matches any of our known responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    # If no match is found, return a default response
    return random.choice(responses["default"])

def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)
