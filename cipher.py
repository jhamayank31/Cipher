
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import cv2  # camera library
import smtplib
import random
import pywhatkit as kit
import sys
import time
import pyjokes
from requests import get


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Sir, I am Cipher. Please tell me how may I help you")

# to convert voice into text


def takeCommand():

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

# to send email


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'youtube' in query:
            webbrowser.open("instagram.com")

        elif 'browser' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stack overflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\cipher\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "ip adress" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP adress is {ip}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            codePath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2210.5.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(codePath)
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(100)
                if k == 27:
                    break ;
                cap.release()
                cv2.destroyAllWindows()

        elif 'email to abhishek' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Abhishek. I am not able to send this email")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        
# to close applications

        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill/f /im notepad.exe")

# to set an alarm
        elif "setb alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir, songs[0])

# to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shutdown the system" in query:
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (yes/no)")
            if shutdown == "yes":
                os.system("shutdown /s /t 1")
            elif shutdown == "no":
             break

        elif "restart the system" in query:
            os.system("shutdown /r /t S")

        elif "sleep the system" in query:
            os.system("rund1132.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "whatsapp" in query:
            from whatsapp import sendMessage
            sendMessage()