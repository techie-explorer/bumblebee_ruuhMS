from gtts import gTTS
import os
class TTs:
    """ This class provides the method to convert Text obtained to speech"""
    @staticmethod
    def savemp3():
        """ This method saves the voice output as an mp3 file"""
        if(os.path.exists('telugu.txt')):
            f=open('telugu.txt')
            tts=gTTS(text=f.read(),lang='te',slow=False)
            f.close()
            if(os.path.exists('sample.mp3')):
                os.remove('sample.mp3')
            tts.save('sample.mp3')
            os.remove('telugu.txt')
        else:
            tts=gTTS(text="sorry couldn't get any results for what you are looking for",lang='te',slow=False)
            if(os.path.exists('sample.mp3')):
                os.remove('sample.mp3')
            tts.save('sample.mp3')
    @staticmethod
    def openmp3():
        """This method opens the Mp3 file and outputs the voice"""
        os.popen('sample.mp3')

            
