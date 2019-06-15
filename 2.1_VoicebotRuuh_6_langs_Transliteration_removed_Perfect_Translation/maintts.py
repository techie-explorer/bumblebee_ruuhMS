from url import Url
from texttospeech_search import TTs
import url_generate as ug
import speech_recognition as sr
def ruuh_search(instr):
    print("reached to maintts")
    file=open('word.txt','w')
    file.close()
    #instr=r.recognize_google(audio)
    print(type(instr))
    file=open('word.txt','a')
    file.write(instr)
    file.close()
    file = open("word.txt",'r')
    stat=file.read()
    file.close()
    #print(stat)
    #get_results(stat)
    file1=open("urlfile.txt",'w')
    file1.close()
    urllist=ug.get_results(stat)
    print("came back")
    print(urllist)
    file1=open("urlfile.txt",'a')
    for url in urllist:
        file1.write(url+"\n")
        print(url)
    file1.close()
    file=open('urlfile.txt')
    while(True):
        #print("fail1")
        Urlink=file.readline()
        #print("fail2")
        if(Urlink != "" and not Url.get_info(Urlink)):
            #print("fail3")
            continue
        else:
            break
    file.close()
    TTs.savemp3()
    TTs.openmp3()
    return "MainTTSDone"
#ruuh_search("search for laptop")
