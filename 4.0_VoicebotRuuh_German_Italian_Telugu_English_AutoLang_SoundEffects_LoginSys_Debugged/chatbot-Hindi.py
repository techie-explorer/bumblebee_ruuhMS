lang_short = "hi"
lang_long = "hi-IN"
google_api_json_filename = "./ProjectRuuhVoicBot-fb63647dd4d7.json"
""" IMPORTING LIBRARIES """
from fbchat import Client
import fbloginpage as fb
from fbchat.models import *
from gtts import gTTS
import speech_recognition as sr
import threading
from playsound import playsound
import sys
import os
import time
from google.cloud import translate
from google.cloud import speech
""" SET ENVIRONMENT VARIABLES IN SYSTEM PATH """
# The path should be the .json Google cloud credential file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_api_json_filename
# Thread class for 'ruuh()' function
class ruuh_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            ruuh()
# To handle emojis from Ruuh's replies
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
# Facebook Login credentials
client = Client('Ruuh VoiceBot', 'Microsoft@Ruuh')
# The facebook account for Ruuh Voice Bot - Microsoft
# fb_id = input("Please enter your facebook ID: ")
# fb_pwd = input("Please enter your facebook password: ")
# fb.start()
# fb_id = fb.username
# fb_pwd = fb.password
# client = Client(fb_id, fb_pwd)
# RUUH ID : 118809975300669
# Function to translate text to another language
def translate_text(text, target):
        translate_client = translate.Client()
        result = translate_client.translate(text, target_language=target)
        return result['translatedText']
# ----------------------------------------- MAIN CODE ---------------------------------
# Counter
c = 0
# Initializing pygame audio systems
def ruuh():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print(" Speak !")
        # Apple Siri's initialization sounds
        playsound('siri_start.mp3', True)
        # Listening to microphone
        audio = r.listen(source)
    try:
        global c
        c = c
        playsound('siri_heard.mp3', True)
        result_temp = r.recognize_google(audio, language=lang_long)
    except sr.UnknownValueError:
        if(c <= 1):
            playsound("oops_didn't_catch_that.mp3", True)
            c = c+1
        else:
            # Will be executed when you don't talk to Ruuh for 2 iterations
            playsound("oops_didn't_catch_that.mp3", True)
            exit(0)
        return
    except sr.RequestError as e:
        #speak.Speak("Could not request results from Google Speech Recognition service; {0}".format(e))
        return
    print("You said: ", result_temp)
    result = translate_text(result_temp, "en")
    print("You said (according to Ruuh) : ", result)
    if "bye" in result:
        playsound('bye.mp3', True)
        exit(0)
    client.send(Message(result), thread_id="118809975300669",thread_type=ThreadType.USER)
    playsound('cortana_thinking.mp3', True)
    time.sleep(1)
    playsound('cortana_thinking.mp3', True)
    messages = client.fetchThreadMessages(thread_id="118809975300669", limit=2)
    messages.reverse()
    ruuh_reply = ""
    for message in messages:
        if(message.text != result):
            ruuh_reply = ruuh_reply+''+message.text
            print("Ruuh's reply: ", ruuh_reply.translate(non_bmp_map))
        messages = []
        message = []
    ruuh_reply = translate_text(ruuh_reply, lang_short)
    print("Ruuh replied: ", ruuh_reply.translate(non_bmp_map))
    c = 0
    tts = gTTS(ruuh_reply, lang=lang_short, slow=False)
    tts.save('reply.mp3')
    playsound('reply.mp3', True)
    os.remove('reply.mp3')
# Function to launch RuuhVoiceBot using threads
def start_ruuh():
    start_thread = ruuh_thread()
    #start_thread.setDaemon = True
    start_thread.start()
# Function to initialize the start_ruuh function
def main():
    try:
        start_ruuh()
        #speak("I'am listening")
    except Exception as e:
        print("The following exeption occured\n" + str(e))
        start_ruuh()
main()
