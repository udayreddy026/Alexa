import speech_recognition as sr
import pyttsx3


listener1 = sr.Recognizer()
voice_engine = pyttsx3.init()
voices = voice_engine.getProperty('voices')
voice_engine.setProperty('voice', voices[1].id, )
voice_engine.setProperty('volume', 0.7)
voice_engine.say('I am u r assistant what can i do for u')
voice_engine.say("Welcome")
voice_engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("start giving commands...")
        voice_in = listener1.listen(source)
        command = listener1.recognize_google(voice_in)
        command1 = command.lower()
        if 'alexa' in command1:
            print(command1)
except:
    pass

print("bye")
