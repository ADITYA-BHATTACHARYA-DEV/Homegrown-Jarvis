import pyttsx3
import wikipedia
import pyaudio
import datetime
import webbrowser
import speech_recognition as sr
engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour <18:
        speak("Good Afternoon")
    else :
        speak("Good Evening")
    speak("I am Angela sir . Please tell me how may i help you ")
def takeCommand():
    #it takes microphone input from  user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching Wikipedia....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening Youtube")
        elif 'open jiosaavn' in query:
            speak("opening jiosaavn")
            webbrowser.open("https://www.jiosaavn.com")






    


