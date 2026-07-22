import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import numpy as np
import os

def aura_listen():
    recognizer = sr.Recognizer()
    temp_filename = "temp_voice.wav"
    
    sample_rate = 16000
    duration = 5 # Records in 3-second blocks
    
    while True:
        try:
            # 1. Record a 3-second block from microphone
            recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
            sd.wait()
            
            # 2. Check if there was actual voice energy in the recording
            volume = np.linalg.norm(recording) / len(recording)
            
            # If it's silent, skip processing without printing anything to keep the terminal clean
            if volume < 0.01:  # Silence threshold
                continue
            
            # 3. Sound detected! Show terminal messages and process
            print("\n[Aura]: Listening...")
            
            sf.write(temp_filename, recording, sample_rate)
            
            print("[Aura]: Recognizing...")
            with sr.AudioFile(temp_filename) as source:
                audio_data = recognizer.record(source)
                
            query = recognizer.recognize_google(audio_data, language='en-pak')
            
            if query.strip():
                print(f"You said: {query}")
                return query.lower()
                
        except sr.UnknownValueError:
            # If Google speech couldn't parse the audio, stay in the loop quietly
            pass
        except Exception as e:
            # Silence minor hardware hiccups
            pass
        finally:
            if os.path.exists(temp_filename):
                try:
                    os.remove(temp_filename)
                except Exception:
                    pass