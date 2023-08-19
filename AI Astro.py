import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour == 0 and hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Night!")

    speak("I am Astro, How may I help you")

def chooseInputMethod():
    print("Do you want to use voice (v) or text (t) input? (Default is voice)")
    choice = input().strip().lower()
    return choice

def takeVoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        return query.lower()
        
    except Exception as e:
        # print(e)
        print("Repeat please...")
        return None

def takeTextCommand():
    query = input("Enter your command: ").lower()
    return query


if __name__ == "__main__":
    wishme()
    while True:
        choice = chooseInputMethod()

        if choice == 't':
            query = takeTextCommand()
        elif choice == 'v':
            query = takeVoiceCommand()
        else:
            print("Invalid choice. Please choose 'V' for voice or 'T' for text.")
            continue

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif'play music' in query:
            webbrowser.open("spotify.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\91782\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'whatsapp' in query:
            pywhatkit.sendwhatmsg('+91', 'Hello from Astro', 21, 52)
            # add mobile no with country code and further set time.
        elif'amazon' in query:
            webbrowser.open("www.amazon.com")
        elif'flipkart' in query:
            webbrowser.open("www.flipkart.com")
        elif'swiggy' in query:
            webbrowser.open("www.swiggy.com")
        elif'myntra' in query:
            webbrowser.open("www.myntra.com")
        elif'zomato' in query:
            webbrowser.open("www.zomato.com")
        elif'twitter' in query:
            webbrowser.open("www.twitter.com")
        elif'google calendar' in query:
            webbrowser.open("www.calendar.google.com")
        elif'news' in query:
            webbrowser.open("news.google.com")
        elif'github' in query:
            webbrowser.open("www.github.com")
        elif 'quit' in query:
            exit()
