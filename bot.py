# TASK 4: Basic Chatbot

def chatbot_response(user_input):
    # Convert input to lowercase for consistency
    user_input = user_input.lower()

    # Rule-based responses
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def run_chatbot():
    print("Welcome to the Basic Chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        
        if user_input.lower() == "bye":
            break

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
