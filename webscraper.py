import requests
from bs4 import BeautifulSoup
import re


def radula(urlNumber):
    url = "https://www.elementalatina.com/2014/06/vjezba-"+str(urlNumber)+".html"
    html = requests.get(url)
    search = BeautifulSoup(html.content, "html.parser")
    vocabulary = search.find(id="rj")
    words = vocabulary.find_all("li")
    wordList = []
    filename = "rijeci-"+str(urlNumber)+".txt"

    def cleanWords():
        regex = r'<p class="(?:word|word-old)">(.*?)</p>(.*?)</li>'
        wordsClean = re.findall(regex, str(words))
        for word in wordsClean:
            wordList.append([word[0]+": "+word[1]])

    def createFile():
        with open(filename, "x", encoding="utf-8") as file:
            file.write("RIJECI VJEZBE BR. "+str(urlNumber)+"\n")

    def wordsToTxt():
        with open(filename, "a", encoding="utf-8") as file:
            for word in wordList:
                file.write(word[0]+"\n")

    cleanWords()
    createFile()
    wordsToTxt()


