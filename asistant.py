from tkinter.tix import ListNoteBook
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
engine.setProperty('rate', 145)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    if engine._inLoop:
        engine.endLoop()

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        talk('Te escucho...')
        listener.pause_treshold = 0.1
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)

    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()
    except sr.UnknownValueError:
        print("NO te entendí, intenta de nuevo")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return rec
