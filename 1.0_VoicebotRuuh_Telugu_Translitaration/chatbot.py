# Rajyalakshmi, Farhan and Nikhil

# Import Libraries
from texttospeech import TTs
import speech_recognition as sr
from fbchat import Client
import time
from fbchat.models import *
from googletrans import Translator
import shutil
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
from google.cloud import translate
import sys
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./ruuhvoicebot-5234ddadd06f.json"


# For emoji types
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)


# Facebook Login credentials
client = Client('farhan_mohammed98@outlook.com', 'Farhan @facebook')
num=1

# RUUH ID : 118809975300669

# Function to convert telugu text to english letters (Indic Transliteration)
def tel2eng(sentence):
    return transliterate(sentence, sanscript.TELUGU, sanscript.HK)

# Function to translate english to telugu
def translate_text(text, target):
    translate_client = translate.Client()
    result = translate_client.translate(text,target_language=target)
    result = translate_client.translate(text, target_language=target)
    return result['translatedText']

# Function to translate telugu language to english
def translation(given_txt):
   translator = Translator()
   translations = translator.translate(given_txt, dest='en',src='te')
   #for transltion in translations:
   print(translations.origin, ' -> ', translations.text)
   return translations.text


# Main Code
def exec():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Say something : ')
        time.sleep(1)
        audio = r.listen(source)    
        result = r.recognize_google(audio)
        result = translation(result)
        file=open('word.txt','w')
        file.close()
        instr=result
        file=open('word.txt','a')
        file.write(instr)
        file.close()
    file = open("word.txt",'r')
    text=file.read()
    #print(text)
    file.close()
    client.send(Message(text), thread_id="118809975300669", thread_type=ThreadType.USER)
    time.sleep(8)
    messages = client.fetchThreadMessages(thread_id="118809975300669", limit=2)
    messages.reverse()
    print("\n")
    file1=open('tex.txt','w')
    file1.close()
    for message in messages:
        if(message.text!=text):
            voice=message.text
            #print(voice)
            voice_lol=voice
            voice_lol = translate_text(voice_lol,"te")
            #print(voice_lol)
        messages=[]
        message=[]
    final = tel2eng(voice_lol)
    print("final: ",final.translate(non_bmp_map))
    telugu = open('telugu.txt','w')
    telugu.close()

    #telugu=open('telugu.txt','a')
    #telugu.write(final)
    #telugu.close()

    with open('telugu.txt','a',encoding='utf-8') as telugu:
        telugu.write(final)
    TTs.savemp3()
    TTs.openmp3()   
    time.sleep(10)
while(1):
    exec()
        
    

