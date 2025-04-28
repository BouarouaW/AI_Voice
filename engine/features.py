import re
from playsound import playsound

import eel

from engine.config import ASSISTANT_NAME
import eel
import pyttsx3
import speech_recognition as sr
import eel
import os
from engine.command import speak

# Playing Assistante sound fonction 
import pywhatkit as kit
import webbrowser


@eel.expose
def playAssistantSound():
    
    music_dic= "www\\assets\\audio\\start_sound.mp3" 
    playsound(music_dic)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower()
    
    if query!="":
        speak("opening "+query)
        os.system("start "+query)
    else:
        speak("not found")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak(f"Playing {search_term} on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Sorry, I didn't understand what to play.")

def extract_yt_term(command):
    pattern = r'(?:play\s+)?(.+?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    
    if match and match.lastindex:
        return match.group(1).strip()
    else:
        cleaned_command = command.lower().replace("on youtube", "").strip()
        return cleaned_command if cleaned_command else None


def SearchGoogle(query):
    search_term = extract_google_term(query)
    if search_term:
        speak(f"Searching for {search_term} on Google")
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(url)
    else:
        speak("Sorry, I didn't understand what to search for.")

def extract_google_term(command):
    pattern = r'(?:search\s+)?(.+?)\s+on\s+google'
    match = re.search(pattern, command, re.IGNORECASE)

    if match and match.lastindex:
        return match.group(1).strip()
    else:
        cleaned_command = command.lower().replace("on google", "").replace("search", "").strip()
        cleaned_command = command.lower().replace("i want to search about", "").strip()

        return cleaned_command if cleaned_command else None
