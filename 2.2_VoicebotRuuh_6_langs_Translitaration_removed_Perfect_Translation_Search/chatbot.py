# Rajyalakshmi, Farhan and Nikhil

# Import Libraries
from texttospeech import TTs
import speech_recognition as sr
from fbchat import Client
import time
from fbchat.models import *
from googletrans import Translator
import shutil
from google.cloud import translate
import sys
import os
from gtts import gTTS
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./ruuhvoicebot-5234ddadd06f.json"
import io
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
import os
import maintts
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./ruuhvoicebot-5234ddadd06f.json"

# For emoji types
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)



# Facebook Login credentials
client = Client('farhan_mohammed98@outlook.com', 'Farhan @facebook')
num=1

# RUUH ID : 118809975300669

# Function to convert telugu text to english letters (Indic Transliteration)
#def tel2eng(sentence, detected_lang):
#    return transliterate(sentence, detected_lang, sanscript.ITRANS)


def translate_text(text, target):
    translate_client = translate.Client()
    result = translate_client.translate(text,target_language=target)
    #result = translate_client.translate(text, target_language=target)
    #print(result['translatedText'])
    return result['translatedText']

def detect_language(text):
    # [START translate_detect_language]
    #Detects the text's language
    translate_client = translate.Client()

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.detect_language(text)

    #print('Text: {}'.format(text))
    #print('Confidence: {}'.format(result['confidence']))
    #print('Language: {}'.format(result['language']))
    return result['language']
    # [END translate_detect_language]

def s2t(detected_language=None):
    # Instantiates a client
    client = speech.SpeechClient()
    # The name of the audio file to transcribe
    #file_name = os.path.join(
    #    os.path.dirname('./file.wav'))
    file_name = "./file.wav"
    # Loads the audio into memory
    with open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    if(detected_language!=None):
        if(detected_language=="te"):
            lan="te-IN"
        elif(detected_language=="hi"):
            lan="hi-IN"
        elif(detected_language=="en"):
            lan="en-US"
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=48000,
            language_code=lan)
        # Detects speech in the audio file
        response = client.recognize(config, audio)
        sen=[]
        count=0
        for result in response.results:
            #print('You said: {}'.format(result.alternatives[0].transcript))
            sen.append(result.alternatives[0].transcript)
        #print(sen)
        #print(len(sen))
        sentence=sen[0]
        #print(sentence)
        #print(type(sentence))
        return sentence


# Main Code
def exec():
    S=0
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1, sample_rate = 48000) as source:
        print("Speak")
        try:
            audio = r.record(source, duration = 5)
            #print("Done")
        except:
            exec()
    with open("file.wav", "wb") as f:
        f.write(audio.get_wav_data())

    with sr.WavFile("file.wav") as source:
        aud = r.record(source)
        result = r.recognize_google(audio)
        #detected_lang = detect_language(result)

    temp_result = s2t()
    
    detected_lang=detect_language(result)
    print("Detected language: ", detected_lang)
    actual_result = s2t(detected_lang)
    print("You said : ", actual_result)

    
    if(detected_lang!="en"):
        result = translate_text(actual_result,"en")
    file=open('word.txt','w',encoding='utf-8')
    file.close()
    instr=result
    file=open('word.txt','a',encoding='utf-8')
    file.write(instr)
    file.close()
    file = open("word.txt",'r',encoding='utf-8')
    text=file.read()
    
    #print(text)
    file.close()
    print("Your message according to Ruuh: ",text)
    if "search" in text:
        S=1
        #print(result)
        search_pos = text.find("search") - 1
        srch_term=text[search_pos:]
        print(srch_term)
        search_status = maintts.ruuh_search(srch_term)
        if(search_status=="MainTTSDone"):
            print("re-execution")
            time.sleep(10)
            exec()

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
            print("Ruuh's reply: ",voice_lol.translate(non_bmp_map))
            #print("p1",voice_lol.translate(non_bmp_map))
            voice_lol = translate_text(voice_lol,detected_lang)
            
            #print(voice_lol)
        messages=[]
        message=[]
        

    print("Ruuh replied: ",voice_lol.translate(non_bmp_map))
    tts=gTTS(voice_lol,lang='te',slow=False)
    tts.save('pure.mp3')

    TTs.savemp3(detected_lang)
    TTs.openmp3()   
    time.sleep(10)

while(1):
    exec()
