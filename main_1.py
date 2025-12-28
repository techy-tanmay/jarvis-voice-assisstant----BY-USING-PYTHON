import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def proceedcommand(c):
    if c.lower() == "open youtube":
        webbrowser.open("https://www.youtube.com")

    elif c.lower() == "open gmail":
        webbrowser.open("https://www.gmail.com")

    elif c.lower() == "open linkedin":
        webbrowser.open("https://www.linkedin.com")

    elif c.lower() == "open instagram":
        webbrowser.open("https://www.instagram.com")

    elif c.lower() == "open github":
        webbrowser.open("https://www.github.com")
        
    else:
        speak("Command not recognized")

if __name__ == "__main__":
    speak("Initializing jarvis...")
    print("recognizing..")

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)

            order = recognizer.recognize_google(audio)
            print("you said:", order)

            if "jarvis" in order.lower():
                print("jarvis activated")
                speak("Yes")

                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=4, phrase_time_limit=4)

                command = recognizer.recognize_google(audio)
                print("command:", command)
                proceedcommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out")

        except sr.UnknownValueError:
            print("Could not understand audio")
            speak("I did not understand")

        except sr.RequestError:
            print("Speech recognition service error")
            speak("Network error")

        except Exception as e:
            print("Error:", e)
