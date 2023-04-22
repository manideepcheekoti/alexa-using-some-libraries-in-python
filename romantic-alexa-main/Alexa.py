import speech_recognition as sr
import pyttsx3
import pywhatkit as pw
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')       # THis two lines is for
engine.setProperty('voice',voices[1].id)                        # getting a female voice.

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source) # microphone should not hear background voice(noice)
            print("Listening.....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
                print(command)
            # else:
            #     talk(f"Alexa is not there,{command}")
            #     print(f"Alexa is not there,{command}")
    except:
        print("Can't hear :(")

    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing')
        pw.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M') # For 12 hours format use datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current time is:" + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache.')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
