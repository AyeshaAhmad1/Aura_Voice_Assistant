from datetime import datetime 


def get_current_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")

def get_current_date():
   now = datetime.now()
   return now.strftime("%B %d, %Y")

