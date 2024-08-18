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

    speak("I am John Sir. Please tell me how may I help you")

def greetText():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")   

    else:
        print("Good Evening!")  

    print("I am John Sir. Please tell me how may I help you")

def Commandle():
    

    r = sp.Recognizer()
    with sp.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
           print("Say that again please...")  
           return "None"
    return query
print("Start John as chat(1) or speak(2) ?")
userchoise = int(input())
if userchoise == 2:

    if __name__ == "__main__":
        greet()
        while True:
        
            query = Commandle().lower()

            if 'john' in query or 'java' in query:        
                    if 'who is' in query:
                        speak('Searching.....')
                        query = query.replace("java", "")
                        query = query.replace("john", "")
                        query = query.replace("who is", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to Google")
                        print(results)
                        speak(results)

                    elif 'open youtube' in query or 'start youtube' in query:
                        webbrowser.open("youtube.com")

                    elif 'open google' in query or 'start google' in query:
                        webbrowser.open("google.com")

                    elif 'the time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                        speak(f"Sir, the time is {strTime}")

                    elif 'open vs code' in query or 'start vs code' in query:
                        codePath = "C:\\Users\\tanus_k7afruf\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # add your own path here to open it
                        os.startfile(codePath)
                    
                    elif 'what is' in query:
                        speak('Searching.....')
                        query = query.replace("java", "")
                        query = query.replace("john", "")
                        query = query.replace("what is", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to Google")
                        print(results)
                        speak(results)
                    
                    elif'quit' in query or 'bye' in query or 'buy' in query:
                        print("John: leaving...,thanks for your time sir")
                        speak('leaving...,thanks for your time sir')
                        exit()

                    elif'how are you' in query:
                        print("i am great")
                        speak("i am great")
                    
                    elif 'open chrome' in query or 'start chrome' in query:
                                    chro = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome'
                                    os.startfile(chro)

                    elif 'play' in query and 'youtube' in query:
                        query = query.replace("play","")
                        query = query.replace("youtube","")
                        query = query.replace("on","")
                        query = query.replace("john","")
                        query = query.replace("java","")
                        ytsearch(query)

                    elif 'do' in query and 'homework' in query:
                        print("John: i can not do your homework , but i can convert your text to my handwriting if you want me to do so type below or press control plus c.")
                        speak("i can not do your homework , but i can convert your text to my handwriting if you want me to do so type below or press control plus c.")
                        try:
                            inputdata = input("type here: ")
                            yt.text_to_handwriting(inputdata)
                            speak("it is saved where you saved me")
                            filepath = 'johnhandwriting.png'
                            os.startfile(filepath)
                        except:
                            pass
                    
                    
                    elif 'shutdown this computer' in query:
                        speak("system will shutdown in a minute")
                        yt.shutdown(time=60)


                    elif 'cancel' in query and 'shutdown' in query:
                        yt.cancel_shutdown()
                        speak("shutdown canceled")  


                    elif 'joke' in query or 'jokes' in query:
                        My_joke = joke.get_joke(language="en", category="neutral")
                        print(My_joke,"\n")
                        speak(My_joke)

                    else:
                            query = query.replace("john","")
                            query = query.replace("java","")
                            try:
                                    print("i am still in devlopement by my maker Tanush Chauhan. i would be answering that question soon. untill then i will google it for you\n\n")
                                    yt.search(query)
                            except:
                                pass
            else :
                pass


            #This version of else can also be used but might be annoying.

            # else:
            #      print("i am still in devlopement by my maker Tanush Chauhan. i would be answering that question soon")
            #      speak("i am still in devlopement by my maker Tanush Chauhan. i would be answering that question soon") 

elif userchoise == 1:
    greetText()
    while(True):
            query = input("write here:\n") 
            if 'who is' in query:
                        print('Searching.....\n')
                        query = query.replace("java", "")
                        query = query.replace("john", "")
                        query = query.replace("john", "")
                        query = query.replace("who is", "")
                        results = wikipedia.summary(query, sentences=2)
                        print("According to Google\n")
                        print(results,"\n")

            elif 'open youtube' in query or 'start youtube' in query:
                        webbrowser.open("youtube.com")

            elif 'open google' in query or 'start google' in query:
                        webbrowser.open("google.com")

            elif 'the time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                        print(f"Sir, the time is {strTime}\n")

            elif 'open vs code' in query or 'start vs code' in query:
                        codePath = "C:\\Users\\tanus_k7afruf\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # add own path here
                        os.startfile(codePath)

            elif 'what is' in query:
                        print('Searching.....\n')
                        query = query.replace("java", "")
                        query = query.replace("john", "")
                        query = query.replace("what is", "")
                        results = wikipedia.summary(query, sentences=2)
                        print("According to Google\n")
                        print(results,"\n")
            
            elif'quit' in query or 'bye' in query or 'buy' in query:
                        print("John: leaving...,thanks for your time sir\n")
                        exit()

            elif'how are you' in query:
                        print("i am great")
                        speak("i am great")
            
            elif 'open chrome' in query or 'start chrome' in query:
                                    chro = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome'
                                    os.startfile(chro)

            elif 'play' in query and 'youtube' in query:
                        query = query.replace("play","")
                        query = query.replace("youtube","")
                        query = query.replace("on","")
                        query = query.replace("john","")
                        query = query.replace("java","")
            
            elif 'do' in query and 'homework' in query:
                    print("John: i can not do your homework , but i can convert your text to my handwriting if you want me to do so type below or press control plus c.\n")

                    try:
                        inputdata = input("type here: ")
                        yt.text_to_handwriting(inputdata)
                        print("it is saved where you saved me\n")
                        filepath = 'johnhandwriting.png'
                        os.startfile(filepath)
                    except:
                        pass

            elif 'shutdown this computer' in query:
                        yt.shutdown(time=60)

            elif 'cancel' in query and 'shutdown' in query:
                        yt.cancel_shutdown()
                       
            elif 'joke' in query or 'jokes' in query:
                        My_joke = joke.get_joke(language="en", category="neutral")
                        print(My_joke,"\n")            
                        
            else:
                query = query.replace("john","")
                query = query.replace("java","")
                try:
                        print("i am still in devlopement by my maker Tanush Chauhan. i would be answering that question soon. untill then i will google it for you\n\n")
                        yt.search(query)
                except:
                    pass