#search anything using google and automation
import bs4, requests , webbrowser, sys
print  ("Googling")
res =requests.get("https://www.google.com/search?q=" + ' '.join(sys.argv[1:]))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text, 'html.parser')

linkElems =soup.select('.r a')
#print len(linkElems)
#numOpen = min(5, len(linkElems))
for i in range (4, len(linkElems)):
    webbrowser.open("https://www.google.com/" + linkElems[i].get('href'))
#webbrowser.open("https://www.youtube.com/watch?v=mniAfFVTdMw")
