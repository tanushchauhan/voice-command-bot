#Make sure you have all these modules installed to run it...
import pyttsx3 
import speech_recognition as sp 
import datetime
import wikipedia 
import webbrowser
import os
import pywhatkit as yt
import pyjokes as joke

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def ytsearch(searchitem):
    yt.playonyt(searchitem)

def google(googleitem):
    yt.search(googleitem)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")

def greetText():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")   

    else:
        print("Good Evening!")  

    print("I am Jarvis Sir. Please tell me how may I help you")