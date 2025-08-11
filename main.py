import time
import sys
from plyer import notification

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format( mins, secs)
        sys.stdout.write("\r" + timer) #Don't add a new line and you can see the timer in the same line.
        sys.stdout.flush()
        time.sleep(1)
        t -= 1

    notification.notify(
        title = "Time is up!",
        message = "Come on get up it's time to work!",
        timeout = 5, #This timeout determine the notification time. You can change the seconds if you want.
    )

t = int(input("Enter time in seconds: "))
countdown(int(t))