import speech_recognition as sr
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "input.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    print("Google Speech Recognition results:"+r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

'''
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
try:
    print("Google Cloud Speech recognition results:")
    pprint(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS, show_all=True))  # pretty-print the recognition result
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))


WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"
try:
    print("Wit.ai recognition results:")
    print(r.recognize_wit(audio, key=WIT_AI_KEY, show_all=True))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

BING_KEY = "INSERT BING API KEY HERE"
try:
    print("Bing recognition results:")
    pprint(r.recognize_bing(audio, key=BING_KEY, show_all=True))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))

HOUNDIFY_CLIENT_ID = "INSERT HOUNDIFY CLIENT ID HERE"
HOUNDIFY_CLIENT_KEY = "INSERT HOUNDIFY CLIENT KEY HERE"
try:
    print("Houndify recognition results:")
    pprint(r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY, show_all=True))
except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))

IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE"
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE"
try:
    print("IBM Speech to Text results:")
    pprint(r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD, show_all=True))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))
'''
