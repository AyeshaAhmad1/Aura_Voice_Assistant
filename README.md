# Aura Voice Assistant

Aura is a lightweight, modular desktop voice assistant built in Python. Designed for hands-free system automation and real-time query responses, Aura combines high-speed AI responses using Groq's LPU inference engine with system-level command capabilities.

---

## Features

**Fast Conversational AI:** Powered by Groq LLM integration (`llama-3.3-70b-versatile`) for instant, contextual answers.
**Voice Recognition:** Robust audio processing using `sounddevice` and Google Speech Recognition without PyAudio dependencies.
**Live Weather Updates:** Real-time regional forecasts fetched via WeatherAPI integration.
**System Automation:** Hands-free OS automation routines (hardware diagnostics, system commands).
**Secure Configuration:** Environment variables kept isolated using `python-dotenv` to ensure secret key protection.

---

## Built With

-- Language:** Python 3
-- AI Engine:** Groq API (`llama-3.3-70b-versatile`)
-- Audio / Speech:** `speech_recognition`, `sounddevice`, `soundfile`
-- Integrations:** WeatherAPI, OS Subprocesses
-- Environment & Security:** `python-dotenv`


