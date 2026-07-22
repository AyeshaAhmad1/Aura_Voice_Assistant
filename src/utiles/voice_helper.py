import pyttsx3

def aura_speak(text):
    print(f"Aura : {text}")
    try:
        # Initialize a fresh engine instance for this phrase
        engine = pyttsx3.init('sapi5')
        engine.setProperty('rate', 170)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        
        engine.say(text)
        engine.runAndWait()
        
        # Clean up the engine after speaking to free the audio channel
        engine.stop()
    except Exception as e:
        pass