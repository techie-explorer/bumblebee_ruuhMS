
# Perfect Start

# Imports the Google Cloud client library
import io
import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import time
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./ruuhvoicebot-5234ddadd06f.json"
import speech_recognition as sr
r = sr.Recognizer()


#starts recording...
with sr.Microphone(device_index = 1, sample_rate = 48000) as source:
    r.adjust_for_ambient_noise(source)
    now=time.time()
    print("Speak")
    now=time.time()
    audio_listen=r.listen(source)
    until = time.time()
    print(int(until-now))
    
    audio = r.record(audio_listen, duration = int(until-now))
    print("Done")

#writes the recorded data into a file    
with open("file.wav", "wb") as f:
    f.write(audio.get_wav_data())
# Instantiates a client
client = speech.SpeechClient()
# The name of the audio file to transcribe
#file_name = os.path.join(
#    os.path.dirname('./file.wav'))
file_name = "C:/Users/farha/Desktop/VoicebotRuuh_6_langs_Modified - Copy/file.wav"


# Loads the audio into memory
with open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)
config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code='hi-IN')
# Detects speech in the audio file
response = client.recognize(config, audio)
sen=[]
count=0
for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    sen.append(result.alternatives[0].transcript)
print(sen)
print(len(sen))
sentence=sen[0]
print(sentence)
print(type(sentence))


# Perfect End
##################################################################################################################################################################################






"""
from google.cloud import speech_v1p1beta1 as speech
import argparse
import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./ruuhvoicebot-5234ddadd06f.json"



client = speech.SpeechClient()

speech_file = './file.wav'

first_lang = 'en-US'
second_lang = 'es'

with open(speech_file, 'rb') as audio_file:
    content = audio_file.read()

audio = speech.types.RecognitionAudio(content=content)

config = speech.types.RecognitionConfig(
    encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    audio_channel_count=2,
    language_code=first_lang,
    alternative_language_codes=[second_lang])

print('Waiting for operation to complete...')
response = client.recognize(config, audio)

for i, result in enumerate(response.results):
    alternative = result.alternatives[0]
    print('-' * 20)
    print('First alternative of result {}: {}'.format(i, alternative))
    print(u'Transcript: {}'.format(alternative.transcript))

"""
"""
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./ruuhvoicebot-5234ddadd06f.json"

client = speech_v1.SpeechClient()

encoding = enums.RecognitionConfig.AudioEncoding.FLAC
sample_rate_hertz = 44100
language_code = 'en-US'
config = {'encoding': encoding, 'sample_rate_hertz': sample_rate_hertz, 'language_code': language_code}
uri = 'gs://bucket_name/file_name.flac'
audio = {'uri': uri}

response = client.recognize(config, audio)
"""
"""
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone(device_index = 1, sample_rate = 48000) as source:
    print("Speak")
    audio = r.record(source, duration = 5)
    print("Done")
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())
"""
