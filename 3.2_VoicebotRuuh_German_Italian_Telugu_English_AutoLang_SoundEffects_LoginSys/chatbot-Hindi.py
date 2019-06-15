"""--------------------------Import Libraries----------------------------------------------------"""
# Python files
#from texttospeech import TTs
#import maintts
# # Facebook
import fbloginpage as fb
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
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./Ruuh3Nov2018-489a2a8626b6.json" # The path should be the .json Google cloud credential file path
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
fb.start()
fb_id = fb.username
fb_pwd = fb.password
client = Client(fb_id, fb_pwd)

# RUUH ID : 118809975300669


"""_________________________________________________________________________________________________________________________________________"""


# Function to translate text to another language
def translate_text(text, target):
        translate_client = translate.Client()
        result = translate_client.translate(text,target_language=target)
        return result['translatedText']
"""_________________________________________________________________________________________________________________________________________"""



# Main Code
mixer.init()
def ruuh():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #speak.Speak(" I am listening !")
        print(" Speak !")
        mixer.music.load('siri_start.mp3')
        mixer.music.play()
        audio = r.listen(source)
    try:
        mixer.music.load('siri_heard.mp3')
        mixer.music.play()

        result_temp = r.recognize_google(audio,language="hi-IN")
        #print(" You said: ", result)
    except sr.UnknownValueError:
        speak.Speak('Oops! didnt catch that!')
        return
    except sr.RequestError as e:
        speak.Speak("Could not request results from Google Speech Recognition service; {0}".format(e))
        return

    print("You said: ", result_temp)
    result=translate_text(result_temp,"en")
    print("You said (according to Ruuh) : ",result)
    mixer.music.load('cortana_thinking.mp3')
    mixer.music.play()

    #mixer.music.load('cortana_thinking.mp3')
    #mixer.music.play()


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

    mixer.music.load('cortana_thinking.mp3')
    mixer.music.play()

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
    ruuh_reply = translate_text(ruuh_reply,"hi")
    print("Ruuh replied: ",ruuh_reply.translate(non_bmp_map))
    tts=gTTS(ruuh_reply,lang="hi",slow=False)
    mixer.music.load('cortana_thinking.mp3')
    mixer.music.play()

#    mixer.init()
    sf=TemporaryFile()
    tts.write_to_fp(sf)
    sf.seek(0)
    
    #tts.save('ruuh_reply.mp3')
    
    mixer.music.load(sf)
    mixer.music.play()
    #TTs.savemp3("te")
    #TTs.openmp3()-
    time.sleep(10)
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

main()
