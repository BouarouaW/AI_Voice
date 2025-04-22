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
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        query = r.recognize_google(audio, language="en-in")
        print(f"wiam galt hhhhhh : {query}")
        speak(query)
    except Exception as e:
        return ""
    
    return query.lower()

