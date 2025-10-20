def chatbot_response(user_input):
    user_input = user_input.lower() 
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thanks for asking! And you?"
    elif "your name" in user_input:
        return "I'm a simple chatbot created with Python."
    elif "what can you do" in user_input:
        return "I can chat with you, answer simple questions, and keep you company!"
    elif "bye" in user_input:
        return "Goodbye! It was nice talking to you."
    else:
        return "Sorry, I don't understand that. Can you try again?"

print("Chatbot 🤖: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot 🤖:", response)
    
    if "bye" in user_input.lower():
        break

