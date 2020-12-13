import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lex' in command:
                command = command.replace('lex','')
                print(command)

    except:
        pass
    return command

def run_lex():
    command = take_command()
    print(command)
    if 'play' in command:
        track = command.replace('play','')
        speak('playing ' + track)
        pywhatkit.playonyt(track)

run_lex()