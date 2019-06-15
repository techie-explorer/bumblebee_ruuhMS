# Imported Libraries
from porcupine import Porcupine
from emoji_filter import emicon_filter
from fbl import *
from tkinter import messagebox as tm
from fbchat import Client
from fbchat.models import *
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import sys
import os
import time
from google.cloud import translate
from google.cloud import speech
import argparse
import struct
from datetime import datetime
import numpy as np
import pyaudio
from capture import capture
from drowsiness import drowsinessfeature

from custompython import classify


#import soundfile
sys.path.append("./")
""" SET ENVIRONMENT VARIABLES IN SYSTEM PATH """
# The path should be the .json Google cloud credential file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./ProjectRuuhVoicBot-fb63647dd4d7.json"
# To handle emojis from Ruuh's replies
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
# Facebook Login credentials
client = Client(username, password)
user = client.fetchUserInfo(client.uid)[client.uid]
tts = gTTS('hello' + user.name, lang="en-US", slow=False)
tts.save("hello.mp3")
playsound("hello.mp3")
# Speech-to-Text Translation Function
def translate_text(text, target):
        translate_client = translate.Client()
        result = translate_client.translate(text, target_language=target)
        return result['translatedText']
c = 0
""" **************************** """
# The Main Ruuh Project Function
def ruuh():
    flag = 0
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #import lol
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
        result = r.recognize_google(audio, language="en-US")
    except sr.UnknownValueError:
        if(c <= 1):
            playsound("oops_didn't_catch_that.mp3", True)
            c = c+1
        else:
            # Will be executed when you don't talk to Ruuh for 2 iterations
            playsound("catch_you_later.mp3", True)
            start_porcupine()
        return
    except sr.RequestError as e:
        #speak.Speak("Could not request results from Google Speech Recognition service; {0}".format(e))
        return
    print("You said: ", result)
    print("You said (according to Ruuh) : ", result)
    if "bye" in result:
        playsound('bye.mp3', True)
        print("byeeeeeee")
        start_porcupine()
    if "secure my drive" in result:
        flag = 1
        try:
            drowsinessfeature()
        except Exception as e:
            print("Error Occured",e)
            start_porcupine()
    if "describe a photo" in result:
        capture()
        client.sendLocalFiles("opencv5.png", thread_id="118809975300669", thread_type=ThreadType.USER)
        flag = 1
    if "what is around me" in result:
        capture()
        classify()
        flag = 3
        ruuh()


    if (flag==0):
        client.send(Message(result), thread_id="118809975300669",thread_type=ThreadType.USER)
    playsound('cortana_thinking.mp3', True)
    time.sleep(1)
    playsound('cortana_thinking.mp3', True)
    if(flag==1):
        messages = client.fetchThreadMessages(thread_id="118809975300669", limit=1)
    elif(flag==0):
        messages = client.fetchThreadMessages(thread_id="118809975300669", limit=2)    
    messages.reverse()
    ruuh_reply = ""
    for message in messages:
        if(message.text != result):
            ruuh_reply = ruuh_reply+''+message.text
            print("Ruuh's reply: ", ruuh_reply.translate(non_bmp_map))
        messages = []
        message = []
    print("Ruuh replied: ", ruuh_reply.translate(non_bmp_map))
    c = 0
    ruuh_reply = emicon_filter(ruuh_reply)
    tts = gTTS(ruuh_reply, lang="en-US", slow=False)
    tts.save('reply.mp3')
    playsound('reply.mp3', True)
    os.remove('reply.mp3')
# Wake word Function....Do Not Alter
def start_porcupine():
    library_path = "libpv_porcupine.dll"
    model_file_path = "porcupine_params.pv"
    keyword_file_paths = ["bumblebee_windows.ppn"]
    sensitivities = [0.3]
    input_device_index = None
    output_path = None
    if output_path is not None:
        recorded_frames = []
    num_keywords = len(keyword_file_paths)
    keyword_names =\
        [os.path.basename(x).replace('.ppn', '').replace(
            '_tiny', '').split('_')[0] for x in keyword_file_paths]
    print('listening for:')
    for keyword_name, sensitivity in zip(keyword_names, sensitivities):
        print('- %s (sensitivity: %f)' % (keyword_name, sensitivity))
        #print("sensivities: ", sensitivities)
        #print("paths: ", keyword_file_paths)
        porcupine = None
        pa = None
        audio_stream = None
        try:
            porcupine = Porcupine(
                library_path=library_path,
                model_file_path=model_file_path,
                keyword_file_paths=keyword_file_paths,
                sensitivities=sensitivities)
            pa = pyaudio.PyAudio()
            audio_stream = pa.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length,
                input_device_index=input_device_index)
            while True:
                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
                if output_path is not None:
                    recorded_frames.append(pcm)
                result = porcupine.process(pcm)
                if num_keywords == 1 and result:
                    print('[%s] detected keyword' % str(datetime.now()))
                    #porcupine.delete()
                    #audio_stream.close()
                    #pa.terminate()
                    while(True):
                            try:
                                while True:
                                    ruuh()
                            except Exception as e:
                                print("The following exeption occured\n" + str(e))
                                ruuh()
                elif num_keywords > 1 and result >= 0:
                    print('[%s] detected %s' %
                          (str(datetime.now()), keyword_names[result]))
        except KeyboardInterrupt:
            print('stopping ...')
        finally:
            if porcupine is not None:
                porcupine.delete()
            if audio_stream is not None:
                audio_stream.close()
            if pa is not None:
                pa.terminate()
            if output_path is not None and len(recorded_frames) > 0:
                recorded_audio = np.concatenate(
                    recorded_frames, axis=0).astype(np.int16)
                soundfile.write(output_path, recorded_audio,
                                samplerate=porcupine.sample_rate, subtype='PCM_16')
start_porcupine()
