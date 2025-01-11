import tkinter as tk
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
from tkinter import messagebox

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  
engine.setProperty('volume', 1) 

# Initialize the speech recognizer
recognizer = sr.Recognizer()

#  to speak out loud
def speak(text):
    engine.say(text)
    engine.runAndWait()

# to listen to user's voice input
def listen():
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        root.update()  
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        status_label.config(text=f"Recognized: {query}")
        root.update()  
        return query.lower()
    except sr.UnknownValueError:
        status_label.config(text="Sorry, I did not understand that.")
        root.update()
        return None
    except sr.RequestError:
        status_label.config(text="Could not request results.")
        root.update()
        return None

#  to tell the time
def tell_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M:%S")
    speak(f"The time is {time_str}")

#  to search Wikipedia
def search_wikipedia(query):
    try:
        speak("Searching Wikipedia...")
        result = wikipedia.summary(query, sentences=2)
        status_label.config(text=f"Wikipedia result: {result}")
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("There were multiple results, please be more specific.")
    except wikipedia.exceptions.HTTPTimeoutError:
        speak("Wikipedia service is currently unavailable.")

# to open a website
def open_website(query):
    if 'youtube' in query:
        webbrowser.open("https://www.youtube.com")
    elif 'google' in query:
        webbrowser.open("https://www.google.com")
    elif 'facebook' in query:
        webbrowser.open("https://www.facebook.com")
    elif 'twitter' in query:
        webbrowser.open("https://www.twitter.com")
    elif 'wikipedia' in query:
        webbrowser.open("https://www.wikipedia.org")
    else:
        if 'open' in query:
            query = query.replace("open", "").strip()
            website = f"https://{query}.com"
            webbrowser.open(website)
            speak(f"Opening {website}")
            status_label.config(text=f"Opening {website}")
            root.update()
        else:
            speak("Sorry, I don't know how to open that website.")
            status_label.config(text="Sorry, I don't know how to open that website.")
            root.update()

# Main function for processing commands
def process_command():
    query = listen() 
    if query is None:
        return

    if 'time' in query:
        tell_time()
    elif 'wikipedia' in query:
        query = query.replace("wikipedia", "").strip()
        search_wikipedia(query)
    elif 'open' in query:
        open_website(query)
    elif 'exit' in query or 'quit' in query:
        speak("Goodbye!")
        status_label.config(text="Goodbye!")
        root.quit()
    else:
        speak("Sorry, I don't understand that command.")
        status_label.config(text="Sorry, I don't understand that command.")

#  the main window
root = tk.Tk()
root.title("Voice Assistant -by Sudalai Muthu")
root.geometry("500x350")
root.config(bg="#F4F4F9")  # Background color

# Welcome speech
def welcome_speech():
    speak("Hello, welcome to your voice assistant. How can I Help you today?")
    status_label.config(text="Hello, welcome to your voice assistant.")
    root.update()

#  a label for status updates
status_label = tk.Label(root, text="Initializing...", font=("Arial", 16, "bold"), wraplength=400, bg="#F4F4F9")
status_label.pack(pady=20)

# a button to start voice assistant
start_button = tk.Button(root, text="Need Help!", command=process_command, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", width=15)
start_button.pack(pady=10)

# heading label
heading_label = tk.Label(root, text="Voice Assistant", font=("Arial", 24, "bold"), fg="#2C3E50", bg="#F4F4F9")
heading_label.pack(pady=10)

# Run the welcome speech
welcome_speech()

# Run the application
root.mainloop()
