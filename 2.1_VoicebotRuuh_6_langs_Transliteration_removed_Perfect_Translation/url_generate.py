# Project Ananya - Team 2nd CSE B and C
# Generate URLs for a given text
from googlesearch import search
def get_results(query):
    links=[]
    print(query)
    for j in search(query, tld="co.in", num=10, stop=1, pause=2):
        links.append(j)
        print(j)
        #print(j)
        #print(links)
    return links
    
#z=get_results("Microsoft")
#print(z)
