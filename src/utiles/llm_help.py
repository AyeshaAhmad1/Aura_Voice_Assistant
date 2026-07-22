from groq import Groq
from dotenv import load_dotenv
import os

def ask_aura_ai(user_prompt):
    """
    Sends conversational text to Groq 
    and returns a short, voice-friendly text response.
    """
    
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    
    try:
        # 1. Initialize the Groq core client connection
        client = Groq(api_key=api_key)
        
        # 2. Structure the data packet using system instructions 
        # This tells the model how to behave as a voice assistant
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are Aura, a helpful and witty desktop voice assistant. Keep your responses highly concise, natural, and under 3 sentences long."
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=150
        )
        
        # 3. Pull the text answer safely out of the nested layout dictionary
        response_text = chat_completion.choices[0].message.content
        if response_text:
            return response_text.strip()
        return "I processed that, but received an empty response."
        
    except Exception as e:
        # This prints inside your console log for internal debugging if something fails
        print(f"[AI Error]: {e}")
        return "I am having trouble connecting to my neural network right now."