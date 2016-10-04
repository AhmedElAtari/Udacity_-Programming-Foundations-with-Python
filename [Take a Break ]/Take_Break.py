__author__ = 'Ahmed_EL_ATARI'

import webbrowser
import time


Count=1 #Init Counter
while Count<=3: # Take a Break for 3 Times
    time.sleep(2*60*60) # Every 2 Hours
    webbrowser.open("https://www.youtube.com/watch?v=Eox2qAjrf0U") #Play the music
    Count=Count+1 # Move to the second break time
