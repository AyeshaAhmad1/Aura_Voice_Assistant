class AssistentBrain:
    def __init__(self , name = "Aura"):
        '''This is the constructor which initialize the assistent'''
        self.name = name
        self.is_running = True
    def start(self):
        '''Method to start the assistent'''
        print(f"Hello!. I am {self.name}. How can i help you today?")
        self._run_loop()
    def _run_loop(self):
        """
        A private method (indicated by the underscore) that runs continuously,
        listening for user commands until the assistant is shut down.
        """
        while self.is_running:
            command = input("You").strip().lower()
            if not command:
                continue

            self.processed_command(command)
    def processed_command(self , command):
        if "stop" in command or "exit" in command:
            print("Ok, Good buy!, See you soon")
            self.is_running = False
        elif "hello" in command or "hi" in command or "hey" in command:
            print("hello!, How are you")
            print("How can i help you today")
        



