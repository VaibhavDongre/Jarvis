import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

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