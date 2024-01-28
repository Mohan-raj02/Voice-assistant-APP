import pyttsx3 #pip install pyttsx3 (It allows you to convert text into spoken words.)
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia 
import webbrowser
import os
import subprocess
import comtypes.client

#pip install pywin ,#pip install pyaudio

engine=pyttsx3.init('sapi5')  # SAPI5 : (Speech Application Programming Interface 5) driver for text-to-speech synthesis. 
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Alex , please tell me how may I help you")

def open_spotify():
    # Define the command to open Spotify
    spotify_command = "spotify"

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1    # time interval
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except sr.UnknownValueError:
        print("Sorry, I did not get that. Please say that again.")
        return "None"

    except sr.RequestError:
        print("Sorry, my speech service is down. Please try again later.")
        return "None"

    try:
        # Open Spotify using subprocess
        subprocess.Popen(spotify_command, shell=True)
        print("Spotify opened successfully!")

    except Exception as e:
        print("Error opening Spotify:", e)

        return query
    
def take_voice_command():
    if __name__ == "__main__":
        print("Listening...")
    while True:
        query = take_voice_command().lower()

        if 'open spotify' in query:
            open_spotify()
            break  # Stop listening after opening Spotify

if __name__=="__main__":
    wishMe()
    while True:
    #if 1:
        query=takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open spotify' in query:
            spotify_command = "spotify"

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir = 'D:\\songs\\Favorite'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

