from responses import chatbot_response_database
import re

# Default response when user input is not recognized
FALLBACK_MESSAGE = "Sorry, I don't understand that yet. Type 'help' to see more options."


def normalize_input(user_input: str) -> str:
    """
    Cleans and standardizes the raw user input by:
    1. Converting text to lowercase.
    2. Stripping extra leading/trailing whitespaces and internal double spaces.
    3. Removing common edge punctuation marks (!, ., ,, ?).
    """
    if not isinstance(user_input, str):
        return ""
    
    # Convert to lowercase and strip outer whitespace
    cleaned_text = user_input.lower().strip()
    
    # Collapse multiple internal spaces into a single space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    
    # Remove common edge punctuation marks
    cleaned_text = cleaned_text.strip(" !,.?")
    
    return cleaned_text


def get_response(user_input):
    
    """
    Processes the user input, matches it against the 
    chatbot database, and returns the appropriate response.
    """
    
    # Clean user input data
    cleaned_text = normalize_input(user_input)
    
    # Executing a rule-based system
    if cleaned_text in chatbot_response_database:
        return chatbot_response_database[cleaned_text]
    
    else:
        return FALLBACK_MESSAGE