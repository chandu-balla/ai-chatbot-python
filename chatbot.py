import datetime
import webbrowser

def respond(user):
    greetings = ["hello", "hi", "hey"]

    if user in greetings:
        return "Hi!"
    
    elif "how are you" in user:
        return "I am fine"
    
    elif "your name" in user:
        return "I am your AI assistant"
    
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%H:%M")
        return f"Current time is {current_time}"
    
    elif "open youtube" in user:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube..."
    
    elif "open google" in user:
        webbrowser.open("https://www.google.com")
        return "Opening Google..."
    
    elif user == "bye":
        return "Goodbye!"
    
    else:
        return "Sorry, I didn't understand"

def run_chatbot():
    while True:
        user = input("You: ").lower()
        reply = respond(user)
        print("AI:", reply)

        if user == "bye":
            break

run_chatbot()
