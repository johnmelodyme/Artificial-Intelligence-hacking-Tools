#Arificial_Intelligent: Sabrina[AI]
import pyttsx
import speech_recognition as sr
import pocketsphinx
import pyaudio
import random,os
engine = pyttsx.init()
def listen():
    r - sr.Microphone() as source:
    a = r.listen(source)

    try:

            return r.recognize_sphinx(a)

    except sr.UnknownValueError as e:
           print('could not understand audio')

    except sr.ResquestError:
           print("Recog Error;{0}" .format(e))

    return ""



def media():
    speak('Ok, Mr President')
    speak('starting required application')
    speak('What would you like to hear, Mr president?')
    k = listen()
    speak('playing' + k )
    os.startfile('/home/johnmelodyme/music/'+k+'.mp3')

def shutdown():
   speak('Ok, Mr President')
   speak('Command received')
   speak('I am shutting down')
   os.system('shutdown -s')

def gooffline():
   speak('Ok, Mr President')
   speak('Closing all data')
   speak('disconnecting servers')
   speak('going offline')
   quit()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def online():
    speak('okay, Mr president')
    speak('All system initiated')
    speak('installing all drivers')
    os.system('start E:/Rainmeter.exe')
    speak('every drivers are installed')
    speak('Loading')
    speak('At your service, Mr President')
def mainfunction():
    a = r.listen(source)
    user = r.recognize_sphinx(a)
    print(user)

    if user == "dennis":
        online()

    elif user == "song":
        media()


    elif user == "down":
            gooffline()
    elif user == "shutdown":
            shutdown()
    elif user in ['hi','hey','whatsup','sup','good','hello']:
        d = random.choice(['hey','hi','sup','At your service, Sir'])
        speak(d)
speak('Mr President')

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction()
