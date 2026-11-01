# Rule-Based AI Chatbot 🤖

A simple rule-based chatbot built with Python as part of the Code Decode Lab AI Internship Project.

## What It Can Do

* **Greetings:** Responds to hello, hi, and hey.
* **Identity:** Answers basic questions about its name and purpose.
* **Well-being:** Responds to conversational questions.
* **Gratitude:** Handles thank-you messages.
* **Help:** Shows supported topics and commands.
* **Exit:** Handles commands to end the conversation.

## How It Works

1. **Input Normalization:** Cleans user input by converting it to lowercase and removing extra spaces and selected punctuation.
2. **Response Selection:** Checks the cleaned input against predefined responses using conditional logic.
3. **Fallback Handling:** Returns a default message if no matching response is found.
4. **Conversation Loop:** Continues interacting with the user until an exit command is entered.

## Key Concepts

* Predefined response database using Python dictionaries.
* If-else logic for response selection.
* Input normalization and string processing.
* Continuous interaction using a while loop.
* Modular code organization.

## 📂 Project Structure

```text
Rule-Based-Chatbot/
│
├── responses.py
├── logic.py
├── main.py
├── README.md
└── .gitignore
```

Each Python file has a separate responsibility:

| File           | Description                                  |
| -------------- | -------------------------------------------- |
| `responses.py` | Stores predefined chatbot responses.         |
| `logic.py`     | Normalizes user input and selects responses. |
| `main.py`      | Controls the chatbot conversation.           |
| `README.md`    | Documents the project.                       |

## How to Run

Run the chatbot using Python:

```bash
python main.py
```

## Technologies

Python 3 | Dictionaries | Conditional Logic | Functions | Loops

## Example Interaction

```text
You: hey
DecodeBot: Hey! What's on your mind?

You: how are you
DecodeBot: I'm doing well, thank you! How are you doing today?

You: I'm fine
DecodeBot: Nice to hear it.

You: who created you?
DecodeBot: I was created by Mosairul Alam Tyhan as part of the training program at Decode Labs.
```

## Author

**Mosairul Alam Tyhan**
Computer Science & Technology Student | Aspiring AI/ML Engineer
