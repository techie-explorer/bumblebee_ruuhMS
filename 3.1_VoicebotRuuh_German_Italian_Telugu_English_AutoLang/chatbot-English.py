"""--------------------------Import Libraries----------------------------------------------------"""
# Python files
#from texttospeech import TTs
#import maintts
# # Facebook
from fbchat import Client
from fbchat.models import *
# Basic Google
from tempfile import TemporaryFile
from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
# Built-ins
import win32com.client as wincl
import threading
from pygame import mixer
import sys
import os
import time
from io import BytesIO
# Google cloud libraries
from google.cloud import translate
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

speak = wincl.Dispatch("SAPI.SpVoice")

""" To set environment variable in Windows """
# 'RuuhVoiceBotProject' project from google cloud console - Servive Account = 'RuuhVoiceBotService'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./RuuhVoiceBotProject-643071727a51.json" # The path should be the .json Google cloud credential file path
"""_________________________________________________________________________________________________________________________________________"""

# Thread class for 'ruuh()' function
class ruuh_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            ruuh()

"""_________________________________________________________________________________________________________________________________________"""         
#For emoji types
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

"""_________________________________________________________________________________________________________________________________________"""

#Facebook Login credentials
#client = Client('facebook email-id', 'facebook password')
# The facebook account for Ruuh Voice Bot - Microsoft
client = Client('Ruuh Voicebot', 'ruuhvoicebot')

# RUUH ID : 118809975300669


"""_________________________________________________________________________________________________________________________________________"""


# Function to translate text to another language
def translate_text(text, target):
        translate_client = translate.Client()
        result = translate_client.translate(text,target_language=target)
        return result['translatedText']
"""_________________________________________________________________________________________________________________________________________"""



# Main Code

def ruuh():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #speak.Speak(" I am listening !")
        print(" Speak !")
        audio = r.listen(source)
    try:
        result = r.recognize_google(audio)
        #print(" You said: ", result)
    except sr.UnknownValueError:
        speak.Speak('Oops! didnt catch that!')
        return
    except sr.RequestError as e:
        speak.Speak("Could not request results from Google Speech Recognition service; {0}".format(e))
        return

    print("You said: ", result)
    #result=translate_text(result_temp,"en")
    print("You said (according to Ruuh) : ",result)

    #file=open('word.txt','a',encoding='utf-8')
    #file.write(result)
    #file.close()
    #file = open("word.txt",'r',encoding='utf-8')
    #text=file.read()
    #file.close()
    if "bye" in result:
        speak.Speak(" Bye ! Nice to talk to you !")
        exit(0)

# This is the code for searSch feature and is still under development !

#    # Review search program later
#    if "search" in text:
#       print(result)
#        search_pos = text.find("search") - 1
#        srch_term=text[search_pos:]
#        print(srch_term)
#        search_status = maintts.ruuh_search(srch_term)
#        if(search_status=="MainTTSDone"):
#            print("re-execution")
#            time.sleep(10)

    client.send(Message(result), thread_id="118809975300669", thread_type=ThreadType.USER)
    time.sleep(8)
    messages = client.fetchThreadMessages(thread_id="118809975300669", limit=2)
    messages.reverse()
    ruuh_reply=""
    for message in messages:
        if(message.text!=result):
            ruuh_reply= ruuh_reply+''+message.text
            print("Ruuh's reply: ",ruuh_reply.translate(non_bmp_map))
        messages=[]
        message=[]
    #ruuh_reply = translate_text(ruuh_reply,"en")
    print("Ruuh replied: ",ruuh_reply.translate(non_bmp_map))
    tts=gTTS(ruuh_reply,lang="en",slow=False)
    mixer.init()
    sf=TemporaryFile()
    tts.write_to_fp(sf)
    sf.seek(0)
    
    #tts.save('ruuh_reply.mp3')
    
    mixer.music.load(sf)
    mixer.music.play()
    #TTs.savemp3("te")
    #TTs.openmp3()-
    time.sleep(6)
    #os.remove('ruuh_reply.mp3')

"""_________________________________________________________________________________________________________________________________________"""

# Function to launch RuuhVoiceBot using threads
def start_ruuh():
    start_thread = ruuh_thread()
    start_thread.start()

"""_________________________________________________________________________________________________________________________________________"""

# Function to initialize the start_ruuh function
def main():
    try:
        start_ruuh()
        #speak("I'am listening")
    except Exception as e:
        print("The following exeption occured\n" + str(e))
        start_ruuh()
speak.Speak(" I am listening !")
main()
