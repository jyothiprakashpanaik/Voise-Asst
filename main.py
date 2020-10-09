import pyttsx3 
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import pywhatkit
import random 
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice: ',voices[0].id)
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

contacts = {'vijaya':'+918008044443'}

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=11:
        speak('Good Morning ')
    elif hour >= 12 and hour < 16:
        speak('Good Afternoon')
    else :
        speak('Good Evening')
    speak('Hello World I am Janvit, Speed 1 terahertz, memory 1 zeta byte.')
    speak('What would i do for you?')

def takeComand():
    # take input from user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listining...')
        r.pause_threshold = 1
        r.non_speaking_duration = 1
        r.energy_threshold = 500
        audio = r.listen(source)
        try :
            print('Recognizing...')
            query = r.recognize_google(audio,language='en-in') #hi-IN
            speak(audio)
            print('User said: ',query)
        except Exception as e :
            print(e)
            # speak('Could you pleas repeat it')
            print('Could you pleas repeat it')
            return "None"
    return query
def send_mess(ph_no,body):
    now = datetime.datetime.now()
    pywhatkit.sendwhatmsg(ph_no,body,now.hour,(now.minute + 2))

if __name__ == "__main__":
    wishMe()
    while True :
        query = takeComand().lower()

        if 'wikipedia' in query :
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences=1)
            speak('According to wikipedia')
            print()
            print(result)
            speak(result)

        elif 'open youtube' in query :
            speak("ok opening youtube")
            webbrowser.get('chrome').open('youtube.com')
        elif 'open google' in query :
            speak("ok opening google")
            webbrowser.get('chrome').open('google.com')
        elif 'open linkedin' in query :
            speak("ok opening linkedin")
            webbrowser.get('chrome').open('linkedin.com')
        elif 'play music' in query:
            speak("ok play music")
            mic_path = 'D:\\USER_D\\Doucments_D\\Fav_sng'
            songs = os.listdir(mic_path)
            print(songs)
            try :
                n = random.randint(0,len(songs))
            except :
                n=0
            os.startfile(os.path.join(mic_path,songs[n]))
        elif 'play music' in query :
            speak('ok')
            mic_path = 'D:\\USER_D\\Doucments_D\\Fav_sng'
            os.startfile("D:\\USER_D\\Doucments_D\\Fav_sng\\gabber sing.mp3")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S') 
            speak(strTime)
        elif 'open code' in query :
            cod_path = "C:\\Users\\Jyothi Prakash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(cod_path)
        elif 'open whatsapp and send message' in query :
            speak(f'ok..Sending Whattsapp message')
            lis_mes = query.split()
            if lis_mes[-1] in list(contacts.keys()):
                speak('what should i send')
                content = takeComand()
                speak(f"ok sending message to {lis_mes[-1]} in 2 secounds")
                send_mess(contacts[lis_mes[-1]],content)        
        elif 'open whatsapp' in query :
            webbrowser.get('chrome').open('https://web.whatsapp.com/')
        elif 'who are you' in query :
            speak('Main dikhta ek insaan hoon par hoon ek machine')
        elif 'quit' in query:
            break 
