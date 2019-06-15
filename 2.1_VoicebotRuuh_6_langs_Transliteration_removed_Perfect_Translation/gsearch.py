

from googlesearch import search
query = "Microsoft"
 
for j in search(query, tld="co.in", num=10, stop=1, pause=2):
    print(j)
