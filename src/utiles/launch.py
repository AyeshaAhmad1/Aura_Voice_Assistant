import webbrowser
import subprocess

def app_or_website_launch(command):
    if "youtube" in command or "utube" in command or "yt" in command:
        if "play" in command:
            query = command.split("play")[-1].strip()
            query = query.replace("on youtube", "").replace("on utube", "").strip()
            search_url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(search_url)
            return f"Searching for and playing {query} on YouTube"
        else:
            webbrowser.open("https://youtube.com")
            return "Opning youtube"
    elif "lms" in command:
        webbrowser.open("https://lms3.numl.edu.pk/my/")
        return "opning your lms"
    elif "google" in command:
        webbrowser.open("https://google.com")
        return "opning google"
    elif "cheom" in command:
        subprocess.Popen("start chrome")
        return "Opening Google Chrome"
    elif "notepad" in command:
        subprocess.Popen("start notepad")
        return "Opening Notepad"
    elif "vscode" in command:
        subprocess.Popen("start code")
        return "Opening Visual Studio Code"
    elif "d drive" in command or "projects folder" in command:
        subprocess.Popen(r"explorer D:\TIC_TAC_TOE")
        return "Opening your folder on the D drive"
    
    return None
    



   





