import pyttsx
import speech_recognition as sr
import pocketsphinx
import pyaudio
import random,os
engine = pyttsx.init()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         a = r.listen(source)

         try:

                    return r.recognize_sphinx(a)

         except sr.UnknownValueError:
                print('could not understand audio')

         except sr.RequestError as e:
                print("Recog Error; {0}".format(e))

         return ""




def media():
    speak('ok sir')
    speak('starting required application')
    speak('what do you want me to play for you')
    k = listen()
    speak('ok sir playing' + k + 'for you')
    os.startfile('C:/Users/it/Music/Playlists/Music/'+k+'.mp3')


def shutdown():
    speak('understood sir')
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown -s')

def gooffline():
    speak('ok sir')
    speak('closing all systems')
    speak('disconnecting to servers')
    speak('going offline')
    quit()



def speak(text):
    engine.say(text)
    engine.runAndWait()
def online():
    speak('ok sir')
    speak('starting all system applications')
    speak('installing all drivers')
    os.system('start E:/Rainmeter.exe')
    speak('every driver is installed')
    speak('all systems have been started')
    speak('now i am online sir')
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
    elif user in ['hi','hey','whatsup','sup','good']:
        d = random.choice(['hey','hi','sup'])
        speak(d)
speak('subscribe to learn anything')

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            mainfunction()
