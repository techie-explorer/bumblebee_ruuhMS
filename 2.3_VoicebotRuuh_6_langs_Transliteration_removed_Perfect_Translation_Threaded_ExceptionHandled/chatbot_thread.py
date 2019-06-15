# Rajyalakshmi, Farhan and Nikhil

"""--------------------------Import Libraries----------------------------------------------------"""
#import pyttsx3 ################################################for windows
#import objc    ################################################windws
"""use #       speak.say('Hey speak I am Listening ')
    #       speak.runAndWait()"""#win
import subprocess###############################################for mac

import threading

from texttospeech import TTs
import speech_recognition as sr
from fbchat import Client
import time
from fbchat.models import *
from googletrans import Translator
import shutil
import sys
import os
from gtts import gTTS
import io
import maintts # python file

#from indic_transliteration import sanscript
#from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

#google cloud libraries
from google.cloud import translate
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
""" to set environment variable"""
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./voicebot-b4f895f5b726.json"

"""______________________________________________________________________________________________"""

# Thread class for exec

class ex_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            exec()
#For emoji types
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


#Facebook Login credentials
#client = Client('facebook email-id', 'facebook password')
client = Client('farhan_mohammed98@outlook.com', 'Asus@facebook1998')
num=1

"""
# RUUH ID : 118809975300669

# Function to convert telugu text to english letters (Indic Transliteration)
#def tel2eng(sentence, detected_lang):
#    return transliterate(sentence, detected_lang, sanscript.ITRANS)

# Function to translate english to telugu
# Function to convert telugu text to english letters (Indic Transliteration)
#def tel2eng(sentence):
#    return transliterate(sentence, sanscript.TELUGU, sanscript.HK)"""



def translate_text(text, target):
        translate_client = translate.Client()
        result = translate_client.translate(text,target_language=target)
        return result['translatedText']

def detect_language(text):

#   Detects the text's language
    translate_client = translate.Client()
#   Text can also be a sequence of strings, in which case this method
#   will return a sequence of results for each text.
    result = translate_client.detect_language(text)
#    detected_language=result['language']

    return result['language']


def s2t(detected_language=None):
    
#   Instantiates a client
    client = speech.SpeechClient()
#   The name of the audio file to transcribe
#   os.path.dirname('./file.wav'))
    file_name = "./file.wav"
#   Loads the audio into memory
    with open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
        language_list=['en','te','hi']
    if(detected_language!=None):
        if detected_language not in language_list:
#            subprocess.call(["say", 'pardon! cant get u!'])
            print('pardon! cant get u!')
            return 0
        if(detected_language=="te"):
            lan="te-IN"
        elif(detected_language=="hi"):
            lan="hi-IN"
        elif(detected_language=="en"):
            lan="en-US"
#       changed sample_rate_hertz @rajy
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code=lan)
#       Detects speech in the audio file
        response = client.recognize(config, audio)
        sen=[]
        count=0
        for result in response.results:
            sen.append(result.alternatives[0].transcript)
        try:
            sentence=sen[0]
        except Exception as e:
#            subprocess.call(["say", 'pardon! cant get u!'])
            print('pardon! cant get u!')
            return 0
        return sentence

counter=0
# Main Code
def exec():
    S=0
    r = sr.Recognizer()
    """-------for windows---------------------------------------------"""
#   with sr.Microphone(device_index = 1, sample_rate = 44100) as source:
    """-------for mac osx---------------------------------------------"""
#   speak = pyttsx3.init()
    with sr.Microphone() as source:
        print("Speak")
#        subprocess.call(["say", 'Hey speak I am Listening '])
#       speak.say('Hey speak I am Listening ')
#       speak.runAndWait()
#        try:
        audio = r.record(source, duration = 5)
#           print("Done")
#        except Exception:
#            exec()
#            return
    with open("file.wav", "wb") as f:
        f.write(audio.get_wav_data())

    with sr.WavFile("file.wav") as source:
        try:
            aud = r.record(source)
            result = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Oops! didnt catch that!')
#            subprocess.call(["say", 'Oops! didnt catch that!'])
            return
#            if counter==3:
#                subprocess.call(["say", 'bye!'])
#                exit()
#return main

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return
            
#return main()

#    temp_result = s2t()
    detected_lang=detect_language(result)
    print("Detected language: ", detected_lang)

    actual_result = s2t(detected_lang)
    if(not actual_result):
        return
    
    print("You said : ", actual_result)

    
    if(detected_lang!="en"):
        result = translate_text(actual_result,"en")
# rajy
    else:
        result = actual_result
# rajy


    S=0
    file=open('word.txt','w',encoding='utf-8')
    file.close()
    instr=result
    file=open('word.txt','a',encoding='utf-8')
    file.write(instr)
    file.close()
    file = open("word.txt",'r',encoding='utf-8')
    text=file.read()
    file.close()
#    print("Your message according to Ruuh: ",text)
    
###
###
    if "bye" in text:
        #        subprocess.call(["say", 'bye! nice to talk to you'])
#       speak.say('bye! nice to mee you')################################
#       speak.runAndWait()###################################################
        exit(0)
###
    if "search" in text:
        S=1
#       print(result)
        search_pos = text.find("search") - 1
        srch_term=text[search_pos:]
        print(srch_term)
        search_status = maintts.ruuh_search(srch_term)
        if(search_status=="MainTTSDone"):
            print("re-execution")
            time.sleep(10)
#main()

    client.send(Message(text), thread_id="118809975300669", thread_type=ThreadType.USER)
    time.sleep(8)
    messages = client.fetchThreadMessages(thread_id="118809975300669", limit=2)
    messages.reverse()
    ruuh_reply=""
    for message in messages:
#        if(message.text!=text):
        if(message.text!=text):
            ruuh_reply= ruuh_reply+''+message.text
#            print("Ruuh's reply: ",ruuh_reply.translate(non_bmp_map))
    ruuh_reply = translate_text(ruuh_reply,detected_lang)
        #messages=[]
#message=[]


    print("Ruuh replied: ",ruuh_reply.translate(non_bmp_map))
    tts=gTTS(ruuh_reply,lang=detected_lang,slow=False)
    tts.save('pure.mp3')
    TTs.savemp3(detected_lang)
    TTs.openmp3()   
    time.sleep(10)

def start_ruuh():
    ruuh_thread = ex_thread()
    ruuh_thread.start()

def main():
    try:
        start_ruuh()
    except Exception as e:
        print("The following exeption occured\n" + str(e))
        start_ruuh()

#return

main()
