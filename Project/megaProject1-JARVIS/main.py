import speech_recognition as sr
import webbrowser
import pyttsx3
from fuzzywuzzy import process
import requests
import google.generativeai as genai
from datetime import datetime
from random import choice
import os
import subprocess as sp
import wikipedia
import pywhatkit as kit
import smtplib
from email.message import EmailMessage
import musicLibrary
from utils import opening_text
from utils import paths

EMAIL = ""
PASSWORD = ""
GENAI_API = "AIzaSyAqDF85ykRBOiLr1ezHRh86TZqMuhc-pIQ"
NEWS_API = "78ba354f04c14c04b1114492d4d76f3f"
OPENWEATHER_APP_ID = "4fd2a7e62172679f6140ffad01d1b44e"


recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 190)

# text to speech (pyttsx3)
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# greet user
def greet_user():
    # Greets the user according to the time
    
    hour = datetime.now().hour
    if (hour >= 1) and (hour < 12):
        speak(f"Good Morning sir.")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon sir")
    elif (hour >= 16) and (hour < 24):
        speak(f"Good Evening sir")
    speak(f"How may I assist you today?")

# take user input
def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 3
        audio = r.listen(source, timeout=8, phrase_time_limit=10)
    try:
        print('Recognizing...')
        command = r.recognize_google(audio, language='en-in')
        if not 'exit' in command or 'stop' in command:
            speak(choice(opening_text))
            processCommand(command)
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!, see you soon')
            exit()
    except Exception:
        speak('Sorry sir, I could not understand. Could you please say that again?')

# process command
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("opening google, sir")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("opening facebook, sir")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
        speak("opening instagram, sir")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("opening youtube, sir")
    elif "open twitter" in c.lower():
        webbrowser.open("https://x.com")
        speak("Opening twitter, sir")
        
    elif c.lower().startswith("play"):
        song_name = c.replace("play", "").strip()
        best_match = process.extractOne(song_name, musicLibrary.music.keys(), score_cutoff=75)
        if best_match:
            song = best_match[0]
            link = musicLibrary.music[song]
            speak("As you wish, sir")
            webbrowser.open(link)
        else:
            speak("I couldn't find the song, sir")
            
    elif c.lower() == "open camera":
        speak("Opening camera")
        openCamera()
        
    elif c.lower() == "open notepad":
        speak("Opening notepad")
        openNotepad()
        
    elif c.lower() == "open calculator":
        speak("Opening calculator")
        openCalc()
        
    elif c.lower() == "open cmd":
        speak("Opening command prompt")
        openCmd()
        
    elif c.lower() == "open vs code":
        speak("Opening vs code")
        openVSCode()
        
    elif c.lower() == "open chrome":
        speak("Opening chrome")
        openChrome()
        
    elif "ip" in c.lower():
        speak("Searching IP address, sir")
        ipAdr = ip()
        speak(f'Your IP address is {ipAdr}.\n For your convenience, I am printing it on the screen sir.')
        print(f'Your IP Address is {ipAdr}')
    
    elif "search on wikipedia" in c.lower():
        speak('What do you want to search on Wikipedia, sir?')
        query = take_user_input().lower()
        results = searchWikipedia(query)
        speak(f"According to Wikipedia, {results}")
        speak("For your convenience, I am printing it on the screen sir.")
        print(results)
    
    elif 'play on youtube' in c.lower():
        speak('What do you want to play on Youtube, sir?')
        video = take_user_input().lower()
        playYoutube(video)
    
    elif 'search on google' in query:
        speak('What do you want to search on Google, sir?')
        query = take_user_input().lower()
        searchGoogle(query)
    
    elif "send whatsapp message" in query:
        speak('On what number should I send the message sir? Please enter in the console: ')
        number = input("Enter the number, sir: ")
        speak("What is the message sir?")
        message = take_user_input()
        sendWhatsappMessage(number, message).lower()
        speak("I've sent the message sir.")
    
    elif "send email" in query:
        speak("On what email address do I send sir? Please enter in the console: ")
        receiver_address = input("Enter email address, sir: ")
        speak("What should be the subject sir?")
        subject = take_user_input().capitalize()
        speak("What is the message sir?")
        message = take_user_input().capitalize()
        if sendEmail(receiver_address, subject, message):
            speak("I've sent the email sir.")
        else:
            speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

    elif 'news' in query:
        speak(f"I'm reading out the latest news headlines, sir")
        speak(getNews())
        speak("For your convenience, I am printing it on the screen sir.")
        print(*getNews(), sep='\n')
    
    elif 'weather' in query:
        ip_address = ip()
        city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
        speak(f"Getting weather report for your city {city}")
        weather, temperature, feels_like = getWeatherReport(city)
        speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
        speak(f"Also, the weather report talks about {weather}")
        speak("For your convenience, I am printing it on the screen sir.")
        print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
        
    elif 'joke' in query:
        speak(f"Hope you like this one sir")
        joke = getJoke()
        speak(joke)
        speak("For your convenience, I am printing it on the screen sir.")
        print(joke)
        
    elif "advice" in query:
        speak(f"Here's an advice for you, sir")
        advice = getAdvice()
        speak(advice)
        speak("For your convenience, I am printing it on the screen sir.")
        print(advice)
    
    else:
        # Let genai handle the requests 
        output = aiProcess(c)
        speak(output)   

# genai
def aiProcess(command):
    genai.configure(api_key=GENAI_API)

    model = genai.GenerativeModel('gemini-1.5-pro')

    messages = [
        {"role": "system", "content": "You are a virtual assistant named Jarvis. Always respond like J.A.R.V.I.S. from Iron Man franchise."},
        {"role": "user", "content": command}
    ]

    combined_prompt = "\n".join([f"{message['role']}: {message['content']}" for message in messages])


    response = model.generate_content(combined_prompt)
    return response.text

# camera
def openCamera():
    sp.run(paths["camera"], shell=True)

# notepad
def openNotepad():
    os.startfile(paths["notepad"])
    
# calculator
def openCalc():
    os.popen(paths["calculator"])
    
# cmd
def openCmd():
    os.system(paths["cmd"])
    
# vscode
def openVSCode():
    os.startfile(paths["vs code"])
    
# chrome
def openChrome():
    os.startfile(paths["chrome"])

# ip
def ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
    
# search on wikipedia
def searchWikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

# video on youtube
def playYoutube(video):
    kit.playonyt(video)
    
# search on google
def searchGoogle(query):
    kit.search(query)
    
# send whatsapp message
def sendWhatsappMessage(number, message):
    kit.sendwhatmsg_instantly(f"+977{number}", message)

# send email
def sendEmail(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

# news
def getNews():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

# weather
def getWeatherReport(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

# jokes
def getJoke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

# advice
def getAdvice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    greet_user()
    while True:

        # # Listen for the wake word 'JARVIS'
        # # obtain audio from the microphone
        r = sr.Recognizer()
        print("Listening...")
        try:
            with sr.Microphone() as source:
                print("Recognizing...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("at your service, sir.")

                take_user_input()
        except:
            print('Waiting for activation...')