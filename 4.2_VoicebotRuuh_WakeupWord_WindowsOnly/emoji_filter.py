import re

#text = "hi :) boo....s   :-)  sdf349023323sfjl"
#print(text) # with emoji
def emicon_filter(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    
    txt1 = emoji_pattern.sub(r'', text)# no emoji
    #txt2 = re.sub(r"[^a-zA-Z0-9',.' ']"," ",txt1)
    #print('from filetering:',txt2)# no special chars
    
    return txt1
#r = emicon_filter(text)#
    #return txt2
#r = emicon_filter(text)
#print(r)