import psutil
import subprocess

def system_control(command):
    if "lock" in command:
        subprocess.Popen(r"rundll32.exe user32.dll,LockWorkStation", shell=True)
        return "Locking your PC now"
    if "battery" in command:
        battery = psutil.sensors_battery()
        if battery is None:
            return "I couldn't detect a battery. Are you running on a desktop PC?"
        percent = battery.percent
        is_plugged = battery.power_plugged
        if is_plugged:
            if percent == 100:
                return("Your battery is 100% and fully charged")
            else:
                return(f"Your battery has {percent}% charging and plugged")
        else:
            return(f"Your battery is {percent}% and running on battery power")






     

      