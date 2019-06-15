import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('Say something : ')
    audio = r.listen(source)    
    #print('Google thinks you said : '+r.recognize_google(audio))
    file=open('input.txt','w')
    file.close()
    instr=r.recognize_google(audio)
    print(type(instr))
    file=open('input.txt','a')
    file.write(instr)
    file.close()
