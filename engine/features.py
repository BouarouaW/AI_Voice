from playsound import playsound

import eel

# Playing Assistante sound fonction 

@eel.expose
def playAssistantSound():
    
    music_dic= "www\\assets\\audio\\start_sound.mp3" 
    playsound(music_dic)