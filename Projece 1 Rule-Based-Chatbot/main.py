# Import the response function
from logic import normalize_input, get_response
from responses import chatbot_response_database

# Define exit commands
EXIT_COMMANDS = ["bye", "exit", "quit", "goodbye", "see you", "later", "bye bye", "stop", "end"]


def start_chatbot():

    print("=" * 40)
    print("       WELCOME TO AI CHATBOT")
    print("=" * 40)

    print("DecodeBot: Hello! How can i help you. Type 'bye' to exit.")

    # Start continuous conversation
    while True:

        # Get input from the user
        user_input = input("\nYou: ")

        # Normalize user input
        cleaned_input = normalize_input(user_input)
        
        # Check whether the user input is empty
        if not cleaned_input:
            print("DecodeBot: Please type something.")
            continue

        # Check whether the user wants to exit
        if cleaned_input in EXIT_COMMANDS:

            print(f"DecodeBot: {chatbot_response_database[cleaned_input]}")
            break

        # Generate chatbot response
        response = get_response(user_input)

        # Display response
        print(f"DecodeBot: {response}")


# Run the chatbot
if __name__ == "__main__":
    start_chatbot()