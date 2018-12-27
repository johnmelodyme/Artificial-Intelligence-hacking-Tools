from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gTTS(text = audio, lang='en')
    tts.save("audio.mp3")
    os.system("apg123 audio.mp3")
# Command Listening ~ $0
def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please execute a command: ")
        r.pause_thresold =1 
        r.adjust_for_ambient_noise(source, duration =1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said:" + command + "/n")
# Loop back to  ~ $0
    except sr.UnknownValueError:
        assistant(myCommand())
    return command
# `If` statement for executing command
def assistant (command):
    if "search engine" in command:
        chromium_path =  '/usr/bin/chromium-browser'
        url = 'https://www.google.com/search'
        webbrowser.get(chromium_path).open(url)
# Commands ~ $1 
    if "sabrina" in command:
        talkToMe("Yes?")
    if "hello" in command:
        talkToMe("hello")
    