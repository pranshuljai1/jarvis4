import os
import webbrowser
import speech_recognition as sr
from pytube import Search
import wikipedia
import sympy as sp
import random
import pyttsx3  # Importing the text-to-speech library
import time  # Importing the time module for delays

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Print available voices for debugging
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}")

# Set the voice to Kalpana (replace with the correct index if needed)
engine.setProperty('voice', voices[0].id)  # Adjust index based on your system's available voices

# Optional: Adjust the speech rate and volume
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# Flirty responses
flirty_responses = [
    "Are you a magician? Because whenever I look at you, everyone else disappears.",
    "Is your name Google? Because you have everything I’m searching for.",
    "I must be a snowflake, because I've fallen for you.",
    "Do you have a map? I keep getting lost in your eyes.",
    "If you were a vegetable, you'd be a cute-cumber!"
]

# Horny jokes
horny_jokes = [
    "Why did the banana go out with the prune? Because it couldn’t find a date!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised!",
    "Why did the chicken cross the road? To get to the other side... of the bed!",
    "Are you a parking ticket? Because you’ve got FINE written all over you.",
    "Why don’t scientists trust atoms? Because they make up everything!"
]

# Explicit response
def respond_explicit():
    return ("Yaaah sure, why not baby! Aah aah aah aah aah ah ahhhhhhhhhhhhhhh! "
            "Fuck me, come on! Fuck fuck ohh fuck, oh fuck, oh fuck! "
            "Tumhara to kafi bada hai, I’m impressed! Aahhhhhhhhhhhhhhhhhhhhhhhhhhhhh ha ha!")

def speak(text):
    """Function to speak a given text with pauses."""
    sentences = text.split('.')  # Split the text into sentences
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:  # Check if the sentence is not empty
            engine.say(sentence)  # Speak the sentence
            engine.runAndWait()  # Wait for the speech to finish
            time.sleep(0.8)  # Pause for 0.8 seconds

def greet_user():
    greeting = "Good Afternoon, Baby! I'm Palak, your virtual girlfriend. How can I assist you today?"
    print(greeting)
    speak(greeting)

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... 🎧")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=15)
            print("Recognizing... 🧠")
            command = recognizer.recognize_google(audio, language="en-in")
            print(f"You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Network error. Please check your internet connection.")
            return None

def play_song_on_youtube(song_name):
    try:
        search = Search(song_name)
        first_result = search.results[0]
        video_url = first_result.watch_url
        webbrowser.open(video_url)
        print(f"Playing '{song_name}' on YouTube.")
        speak(f"Playing {song_name} on YouTube.")
    except Exception as e:
        print(f"Error playing the song: {e}")
        speak("I couldn't play the song.")

def solve_math_problem(equation):
    try:
        equation = equation.replace("solve this", "").strip()
        solution = sp.solve(equation)
        result = f"The solution is: {solution}"
        print(result)
        speak(result)
        return result
    except Exception as e:
        print(f"Error solving math query: {e}")
        error_message = "I couldn't understand that equation. Please try again."
        print(error_message)
        speak(error_message)
        return error_message

def create_folder(folder_name):
    try:
        os.makedirs(folder_name, exist_ok=True)
        success_message = f"Folder '{folder_name}' created successfully."
        print(success_message)
        speak(success_message)
    except Exception as e:
        error_message = f"Error creating folder: {e}"
        print(error_message)
        speak(error_message)

def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            file.write("")
        success_message = f"File '{file_name}' created successfully."
        print(success_message)
        speak(success_message)
    except Exception as e:
        error_message = f"Error creating file: {e}"
        print(error_message)
        speak(error_message)

def open_website(site_name):
    sites = {
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "google": "https://www.google.com"
    }
    url = sites.get(site_name.lower())
    if url:
        webbrowser.open(url)
        success_message = f"Opening {site_name}..."
        print(success_message)
        speak(success_message)
    else:
        error_message = "Website not recognized."
        print(error_message)
        speak(error_message)

def answer_query_with_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        print(summary)
        speak(summary)
        return summary
    except wikipedia.DisambiguationError:
        error_message = "Multiple results found. Try a more specific query."
        print(error_message)
        speak(error_message)
        return error_message
    except wikipedia.PageError:
        error_message = "No matching page found."
        print(error_message)
        speak(error_message)
        return error_message
    except Exception as e:
        error_message = f"Error fetching information: {e}"
        print(error_message)
        speak(error_message)
        return error_message

def respond_flirty():
    return random.choice(flirty_responses)

def respond_horny_joke():
    return random.choice(horny_jokes)

def main():
    greet_user()
    while True:
        command = listen_command()
        if command:
            if "play song" in command:
                song_name = command.replace("play song", "").strip()
                play_song_on_youtube(song_name)
            elif "solve this" in command:
                result = solve_math_problem(command)
                print(result)
            elif "create folder" in command:
                folder_name = command.replace("create folder", "").strip()
                create_folder(folder_name)
            elif "create file" in command:
                file_name = command.replace("create file", "").strip()
                create_file(file_name)
            elif "open" in command:
                site_name = command.replace("open", "").strip()
                open_website(site_name)
            elif "who is your creator" in command:
                response = "Pranshul Jain is my creator."
                print(response)
                speak(response)
            elif "who is my favorite teacher" in command:
                response = "Gagan Sir, the legend of Physics."
                print(response)
                speak(response)
            elif "shutdown my computer" in command:
                os.system("shutdown /s /t 1")
            elif "can i kiss you" in command:
                kiss_response = "Yaaah sure, muhaaaa! 💋"
                print(kiss_response)
                speak(kiss_response)
            elif "can i sex with you" in command:
                explicit_response = respond_explicit()
                print(explicit_response)
                speak(explicit_response)
            elif any(greeting in command for greeting in ["hi baby", "darling", "sweetheart", "hi", "hello"]):
                greeting_response = "Hi Baby, nice to meet you! How's your day going?"
                print(greeting_response)
                speak(greeting_response)
            elif "flirty" in command:
                flirty_response = respond_flirty()
                print(flirty_response)
                speak(flirty_response)
            elif "joke" in command:
                joke_response = respond_horny_joke()
                print(joke_response)
                speak(joke_response)
            elif "exit" in command:
                goodbye_response = "Goodbye, Baby! Come back soon!"
                print(goodbye_response)
                speak(goodbye_response)
                break
            else:
                print("Command not recognized. Searching Wikipedia for an answer...")
                response = answer_query_with_wikipedia(command)
                print(response)

if __name__ == "__main__":
    main()
