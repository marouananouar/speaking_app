import pyttsx3
import speech_recognition as sr
import webbrowser
import time

wel = pyttsx3.init()
voices = wel.getProperty('voices')
wel.setProperty('voices', voices[0].id)
print(wel)

def speak(audio):
    wel.say(audio)
    wel.runAndWait()
def TakeCommands():
    command = sr.Recognizer()
    with sr.Microphone() as mic:
        print('Say your Commands sir ...')
        command.phrase_threshold=1
        audio = command.listen(mic)

        try:
            print('Recording...')
            query = command.recognize_google(audio , language='en')
            print(f" you said : {query}")
        except Exception as Error:

            return None
        return query.lower()

speak('hello sir marouan anouar , say your commands please')

while True:
    query = TakeCommands()

    if 'hello' in query:
        speak('hello sir marouan')
    if 'how are you' in query:
        speak('im fine, and you?')
    if 'thanks' in query:
        speak('ok by boss')
    if 'open google' in query:
        speak('ok sir')
        time.sleep(3)
        webbrowser.open_new_tab('https://www.google.com')
        



