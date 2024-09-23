import requests
from bs4 import BeautifulSoup
import re

url = "https://www.elementalatina.com/2014/06/vjezba-32.html"
html = requests.get(url)
search = BeautifulSoup(html.content, "html.parser")
vocabulary = search.find(id="rj")
words = vocabulary.find_all("li")
regex = r'<p class="(?:word|word-old)">(.*?)</p>(.*?)</li>'
wordsClean = re.findall(regex, str(words))
wordList = []
for word in wordsClean:
    wordList.append([word[0]+": "+word[1]])

filename = "rijeci.txt"
with open("rijeci.txt", "w", encoding="utf-8") as file:
    for words in wordList:
        file.write(words[0]+"\n")



