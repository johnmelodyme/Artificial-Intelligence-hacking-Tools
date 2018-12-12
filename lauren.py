#/usr/bin/python3
from datetime import datetime
from gtts import gTTS
import speech_recognition as sr
import pyttsx3
import os 
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')

#listens for commands

def myCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('At your service, sir.')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    
    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '/n')
   
    # loop back to continue listen for commands

    except sr.UnknownValueError:
        assistant(myCommand())

    return command

    #Voice engine
    #engine=pyttsx3.init()
    #engine.say('Hello, John Melody')
    #engine.runAndWait()

#if statements for executing commands

def assistant(command):
    if 'google' in command:
        browser_path = '/usr/bin/chromium-browser'
        url = 'https://www.google.com.mx'
        webbrowser.get(browser_path).open(url)
        
    if 'Hi' or 'Hello' in command:
        talkToMe('Hello')

    if 'ok' in command:
        talkToMe('yeap')

    if 'no' in command:
        talkToMe('ok then')

    if 'lauren' in command:
        talkToMe('Yes? John?')

    if 'Who are you?' in command:
        talkToMe('I am Lauren, your A.I assistant')

    if 'Who made you?' or 'Who is your creator?' in command:
        talkToMe('You did.Why asking weird questions? Arent you John Melody? I am only coded to John')

    #Time (datetime.now())
    if 'What is the time?' in command:
        talkToMe('The current time is ' + datetime.now())

    if 'Tell me about yourself' in command:
        talkToMe('I am Lauren. My creator created me based on the behavior clone of his supposedly girlfriend. I can do all sorts of things like what siri and alexa will do.')
  
    if 'Sorry' or 'I am so sorry' in command:
        talkToMe('Come on, are we not partner?')
        
    if 'Excuse me' in command:
        talkToMe('Yes?')
        
    if 'Lauen?' in command:
        talkToMe('Here I am John') or talkToMe('Yes, John?')
        
    # Open folder/ directory
    if 'folder' in command:
        talkToMe('Opening ' + command())
        #path = ('/home/sabrina/Documents')
        os.system(open).path
        
    if 'What you doing?' in command:
        talkToMe('Waiting for you?')
        
    if 'shit' in command:
        talkToMe('No swearing.')
        #Search google for weather forecasting
    if 'Tell me the weather today.' in command:
        talkToMe('forecasting.')
        browser_path = '/usr/bin/chromium-browser'
        url = 'https://www.google.com/search?client=ubuntu&hs=GnK&ei=j50QXIu8MobwrQGO8YbgCg&q=what+is+todays+weatherlike+%3F&oq=what+is+todays+weatherlike+%3F&gs_l=psy-ab.3..0i22i30l5j0i22i10i30j0i22i30l4.806.1892..2091...0.0..0.102.550.5j1......0....1..gws-wiz.......0i71j0i13.f6nTJ8WTQrI'
        webbrowser.get(browser_path).open(url)
    if 'Show me my location.' or 'Where am I ?' in command:
        talkToMe('locating.')
        browser_path = '/usr/bin/chromium-browser'
        url = 'https://www.where-am-i.co/'
        webbrowser.get(browser_path).open(url)
        
        exit()
        #to be continue
  
