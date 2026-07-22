import pyttsx3

try:
    print("Initializing engine...")
    engine = pyttsx3.init()
    print("Engine initialized successfully.")
    
    print("Attempting speech...")
    engine.say("Testing the voice engine connection.")
    engine.runAndWait()
    print("Speech loop executed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")