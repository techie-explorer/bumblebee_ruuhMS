"""--------------------------Import Libraries----------------------------------------------------"""
# Python files
#from texttospeech import TTs
#import maintts
# # Facebook
from fbchat import Client
from fbchat.models import *
# Basic Google
from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
# Built-ins
from tempfile import TemporaryFile
import win32com.client as wincl
import threading
import sys
import os
import time
from pygame import mixer
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

# Function to speak a statement
#def speak(say):
#    tts = gTTS(text=say, lang='en', slow=False)
#    tts.save("statement.mp3")
#    os.popen("statement.mp3")

"""_________________________________________________________________________________________________________________________________________"""


# Function to translate text to another language
def translate_text(text, target):
        translate_client = translate.Client()
        result = translate_client.translate(text,target_language=target)
        return result['translatedText']
"""_________________________________________________________________________________________________________________________________________"""

# Detects the text's language
def detect_language(text):
    translate_client = translate.Client()
#   Text can also be a sequence of strings, in which case this method
#   will return a sequence of results for each text.
    result = translate_client.detect_language(text)
#    detected_language=result['language']
    return result['language']

"""_________________________________________________________________________________________________________________________________________"""

# Function for speech to text
def speech_2_text(detected_language=None):
#   Instantiates a client
    client = speech.SpeechClient()
#   The name of the audio file to transcribe
#   os.path.dirname('./speech_2_text.wav'))
    file_name = "./speech_2_text.wav"
#   Loads the audio into memory
    with open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
        language_list=['en','te','it','de']
    if(detected_language!=None):
        if detected_language not in language_list:
            speak.Speak("Pardon, can't get you !")
            return 0
        if(detected_language=="de"):
            lan="de-DE" # German language
        elif(detected_language=="it"):
            lan="it-IT" # Italian language
        elif(detected_language=="en"):
            lan="en-US" # English language
        elif(detected_language=="te"):
            lan="te-IN" # Telugu language
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code=lan)

#       Detects speech in the audio file
        response = client.recognize(config, audio)
        sen=[]
        sentence=""
        count=0
        for result in response.results:
            sen.append(result.alternatives[0].transcript)
        for i in sen:
            sentence = sentence + str(i)
        return sentence

"""_________________________________________________________________________________________________________________________________________"""

# Main Code

def ruuh():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #speak.Speak(" I am listening !")
        print(" Speak !")
        audio = r.record(source, duration = 5) # Review for dynamic recording

    with open("speech_2_text.wav", "wb") as f:
        f.write(audio.get_wav_data())

    #with sr.WavFile("speech_2_text.wav") as source:
    try:
        #audio = r.record(source)
        result = r.recognize_google(audio)
    except sr.UnknownValueError:
        speak.Speak('Oops! didnt catch that!')
        return
    except sr.RequestError as e:
        speak.Speak("Could not request results from Google Speech Recognition service; {0}".format(e))
        return

    detected_lang=detect_language(result)
    print("Detected language: ", detected_lang)
    actual_result = speech_2_text(detected_lang)

    # Exception in s2t caught
    if not actual_result:
        return

    print("You said : ", actual_result)
    if(detected_lang!="en"):
        result = translate_text(actual_result,"en")
    else:
        result = actual_result
#    file=open('word.txt','w',encoding='utf-8')
#    file.close()
#    instr=result


    if "bye" in result:
        speak.Speak(" Bye ! Nice to talk to you !")
        exit(0)

# This is the code for search feature and is still under development !

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
    ruuh_reply = translate_text(ruuh_reply,detected_lang)
    print("Ruuh replied: ",ruuh_reply.translate(non_bmp_map))
    tts=gTTS(ruuh_reply,lang=detected_lang,slow=False)
    mixer.init()
    sf=TemporaryFile()
    tts.write_to_fp(sf)
    sf.seek(0)

    mixer.music.load(sf)
    mixer.music.play()

    time.sleep(10)

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
