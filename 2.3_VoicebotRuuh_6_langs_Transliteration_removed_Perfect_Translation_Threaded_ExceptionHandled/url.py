from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import urllib
class Url:
    """ This class consists of all the necessary functions for reading a url...
processing it and giving the output of required text into a text file"""
    @staticmethod
    def get_info(urllink):
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,} 
        """ Method to get info from the url into text file."""
        try:
            request=urllib.request.Request(urllink,None,headers)
            html = urllib.request.urlopen(request)
            #html=urlopen(req).read()
        except HTTPError as e:
            print(e) 
            return False
        else:
            bsobj = BeautifulSoup(html.read(),features="html5lib")
            text = bsobj.body.find("em")
            if(text!=None and text != ''):
                txt = text.get_text()
                file=open("tex.txt",'w')
                file.close()
                file=open("tex.txt",'a')
                for line in txt:
                    file.write(line)
                file.close()
                return True
            else:
                return False
            
#Url.get_info("https://en.wikipedia.org/wiki/Microsoft")
#print(z)
