""" Once you run, you have to call 'genius' plus something"""
""" Example: genius,whats the time?
      genius, who the heck is 'a celebritys name,idk'
      genius, i am sad, or genius tell me a joke, he will tell you a joke, is it funny? of course not.
      genius, play ' a famous singer', ex: genius play justin bieber 
      please speak loud, he's kinda deaf :(
     He has weird accent , i think he's german or chinese, something in between '-'
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            listener.dynamic_energy_threshold = 3000
            print('listening...')
            print('What are your wishes?')
            voice = listener.listen(source, timeout=5.0)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'genius' in command:
                command = command.replace('genius', '')
                print(command)
    except:
        pass
    return command

def run_genius():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is ' + time)
        print(time)

    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'i am sad' in command:
        talk('sorry,here s a joke you might enjoy')
        talk(pyjokes.get_joke())

    elif 'are you single' in command:
        talk('You know i cant get out of this lamp')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again.')
        command = ""

while True:
    try:
        run_genius()
    except UnboundLocalError:
        print("No command detected! Genius has stopped working ")
        command = ""
        print(command)
