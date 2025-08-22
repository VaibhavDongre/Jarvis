import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d31293237487424189e06673053e510e"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")  
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")  
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com") 
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com") 
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com") 

    #For music librabry
    elif c.lowe().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link) 

    #For news
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=d31293237487424189e06673053e510e")   
        if r.status_code == 200:
            data = r.json #parse the JSON response
            articles = data.get('articles', []) #Extract the articles
            for article in articles:
                speak(article['title'])  

    else:
        speak("Please try again...")                           

if __name__ == "__main__":
    speak("Initializing Jarvis.....")   
    while True:
        #Listen for the wake word "Jarvis"
        # Obtaian audio from the mic
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1) #for faster execution
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes Sir")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except sr.RequestError as e:
            print("Error; {0}".format(e))              