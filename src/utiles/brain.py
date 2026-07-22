import time

from src.utiles.Date_Time_helper import get_current_time, get_current_date
from src.utiles.launch import app_or_website_launch
from src.utiles.sys_op import system_control
from src.utiles.voice_helper import aura_speak
from src.utiles.listen import aura_listen
from src.utiles.weather import get_weather
from src.utiles.llm_help import ask_aura_ai

class AssistentBrain:
    def __init__(self , name = "Aura"):
        '''This is the constructor which initialize the assistent'''
        self.name = name
        self.is_running = True
    def start(self):
        '''Method to start the assistent'''
        aura_speak(f"it's {self.name} here.")
        self._run_loop()
    def _run_loop(self):
        """
        A private method (indicated by the underscore) that runs continuously,
        listening for user commands until the assistant is shut down.
        """
        while self.is_running:
            command = aura_listen()
           
            print(f"[User Said]: {command}")
            self.processed_command(command)
            
    def processed_command(self , command):
        
           
        if "stop" in command or "exit" in command or "bye" in command or "thanks" in command:
            aura_speak("Ok, thanks, Good bye!, See you soon")
            self.is_running = False

        elif "how" in command:
            aura_speak("I am doing good!")

        elif "hello" in command or "hi" in command or "hey" in command:
            aura_speak("hello!")
            aura_speak("Nice to meet you!")
            aura_speak("How can i help you?")
            
        elif "current time" in command :
            aura_speak(f"The currect time  {get_current_time()}")

        elif "date" in command:
            aura_speak(f"The currect date is   {get_current_date()}")

        elif "open" in command or "launch" in command or "play" in command:
            response = app_or_website_launch(command)
            if response:
                aura_speak(response)
            else:
                aura_speak("Sorry, i donot have access to it")
                
        elif "lock" in command or "battery" in command:
            response = system_control(command)
            if(response):
                aura_speak(response)
        elif "weather" in command:
            
            target_city = ""
            
            #
            if " in " in command:
                target_city = command.split(" in ")[-1]
            
            elif " of " in command:
                target_city = command.split(" of ")[-1]
            else:
                
                target_city = command.replace("weather", "").strip()
                
            
            if target_city:
                weather_report = get_weather(target_city)
                aura_speak(weather_report)
            else:
                aura_speak("Which city's weather would you like to check?")
        else:
            ai_response = ask_aura_ai(command)
            print(f"[Aura Response]: {ai_response}")
            aura_speak(ai_response)


        
        
            
        
        



