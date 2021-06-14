#---------------------Start Importing Packages---------------------------#
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys
#---------------------End Of Importing Packages---------------------------#

#---------------------Setting Up Voices---------------------------#
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#---------------------End Of Setting up Voices---------------------------#

#---------------------Defining Functions --------------------------#
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello Sir, Good Morning!")
    elif hour>=12 and hour<18:
        speak("Hello Sir, Good Afternoon!")
    else:
        speak("Hello Sir, Good Evening!")

    speak("I am Bella, Please tell me how may I help you sir?")


def takeCommand():
    #takes microphone input from user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said :{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please......")
        return "None"
    return query

#---------------------End Of defining functions---------------------------#

#---------------------Starting the main function---------------------------#

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()


#---------------------Playing with Wikipedia Module---------------------------#
        if "wikipedia" in query:
            speak("Searching Wikipedia......")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)


#---------------------Playing with Webbrowser Module---------------------------#

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open whats app' in query:
            webbrowser.open("whatsapp.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        
        elif 'open wikipedia' in query:
            webbrowser.open("wikipedia.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")
        
        elif 'open gaana' in query:
            webbrowser.open("gaana.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


#---------------------Playing with OS module---------------------------#
 
        elif 'open command prompt' in query:
            os.system('start cmd')

        elif 'open wordpad' in query:
            os.system('start wordpad')

        elif 'open notepad' in query:
            codeN = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(codeN)

        elif 'open paint' in query:
            codeP = "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(codeP)
            
        elif 'play music' in query:
            music_dir = "D:\\My_Music\\My_Playlist"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play video' in query:
            video_dir = "E:\Entertain"
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir, videos[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir The time is {strTime}")

        elif 'open v s code' in query:
            codeV = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codeV)

        elif 'open pycharm' in query:
            CodeP = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.2\\bin\\pycharm64.exe"
            os.startfile(CodeP)

        elif 'open android studio' in query:
            codeA = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(codeA)

        elif 'open Virtual Machine' in query:
            codeM = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
            os.startfile(codeM)

        elif 'open java' in query:
            codeJ = "C:\\Users\\hp\\Downloads"
            os.startfile(codeJ)

        elif 'open anaconda' in query:
            conda = "C:\\Users\hp\\anaconda3\\pythonw.exe C:\\Users\\hp\\anaconda3\\cwp.py C:\\Users\\hp\\anaconda3 C:\\Users\\hp\\anaconda3\\pythonw.exe C:\\Users\\hp\\anaconda3\\Scripts\\anaconda-navigator-script.py"
            os.startfile(conda)

        elif 'open zoom' in query:
            codeZ = "C:\\Users\\hp\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(codeZ)


#---------------------Stoping The Execution of the program---------------------------#

        elif 'you can sleep now' in query:
            speak("Thank you sir! Have a nice day! Bye!!!!")
            sys.exit()

#-----------------------------End Of Main Method-------------------------------------#









