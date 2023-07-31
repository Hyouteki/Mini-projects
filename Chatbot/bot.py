import speech_recognition
import pyttsx3
from hugchat import hugchat
from termcolor import colored

recognizer = speech_recognition.Recognizer()
chatbot = hugchat.ChatBot()
speaker = pyttsx3.init()

def doTheJob():
    with speech_recognition.Microphone() as source:
        print("Speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        question = recognizer.recognize_google(audio)
        answer = chatbot.chat(question)
        answer = answer.replace("\n", "")
        print(colored(f"[IN] :: {question}", "green"))
        print(colored(f"[OUT] :: {answer}", "red"))
        speaker.say(answer)
        speaker.runAndWait()

    except speech_recognition.UnknownValueError:
        print("[ERROR] :: Sorry, I didn't understand that")
    except speech_recognition.RequestError as e:
        print("[ERROR] :: Could not request results from Google Speech Recognition service; {0}".format(e))
    except Exception as e:
        print("[ERROR] :: An error occurred: {0}".format(e))

while True:
    doTheJob()