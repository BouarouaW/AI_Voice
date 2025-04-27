import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')   
    print(voices)
    engine.setProperty('voice', voices[0].id) 
    engine.setProperty('rate', 150)     # setting up new voice rate
    engine.say(text)

    engine.runAndWait()

@eel.expose
def takecommand():

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        eel.DisplayMessage("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print("test")
        print('recognizing')
        eel.DisplayMessage("listening...")
        query = r.recognize_google(audio, language="en-in")
        print(f"wiam galt : {query}")
        eel.DisplayMessage(query)
        speak(query)

        if "open" in query:
            print(" i run")
    
        else:
            print("not run")
    

    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands():
    print("test")

    query= takecommand()
    print(query)
    
    if "open" in query:
        print(" i run")
    
    else:
        print("not run")

