import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')   
    print(voices)
    engine.setProperty('voice', voices[0].id) 
    engine.setProperty('rate', 150)     # setting up new voice rate
    eel.DisplayMessage(text)
    
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
        print('recognizing')
        eel.DisplayMessage("listening...")
        query = r.recognize_google(audio, language="en-in")
        print(f"wiam galt : {query}")
        eel.DisplayMessage(query)
        time.sleep(2)


    except Exception as e:
        return ""
    
    return query.lower()


@eel.expose
def allCommands():
    print("test")

    query = takecommand()
    print(query)
    query = query.lower()



    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "hello how are you" in query:
        speak("I'm fine thank you")
    elif "on youtube" in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)
    elif "on google" in query or "i want to search about" in query:
        from engine.features import SearchGoogle
        SearchGoogle(query)
    else:
        speak("I don't know")

    

    

