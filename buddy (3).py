import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import time
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Buddy. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    while True :
        wishMe()
        i=0
        while i<2:
            i=i+1
        # if 1:
            query = takeCommand().lower()
            chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s'

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.get(chrome_path).open("youtube.com")
            
            elif 'open classes' in query:
                webbrowser.get(chrome_path).open("https://classroom.google.com/u/1/h")

            elif 'open google' in query:
                webbrowser.get(chrome_path).open("google.com")

            elif 'open facebook' in query:
                webbrowser.get(chrome_path).open("www.facebook.com")   


            elif 'play music' in query:
                music_dir = 'C:\\Users\\Pavan.K\\Music\\fav4'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'reminder' in query:
                #Path = 'C:\\Users\\Pavan.K\\vscode\\Reminder'
                os.system('explorer "C:\\Users\\Pavan.K\\vscode\\reminder"')

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            