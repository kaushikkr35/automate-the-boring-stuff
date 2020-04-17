# lucky.py - Opens several Google search results to make life easier

import requests, bs4, webbrowser
google = input('Enter your search query: ')

print('Googling....') # text to be displayed while downloading the Google page

res = requests.get('http://google.com/search?q=' + (google))

res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result
linkElems = soup.select(".r a")

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))


