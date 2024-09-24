import requests
from bs4 import BeautifulSoup
import re

def radula(urlNumber, searchForVerbs=False):
    num = 6
    if urlNumber > 61:
        num = 7
    url = "https://www.elementalatina.com/2014/0"+str(num)+"/vjezba-"+str(urlNumber)+".html"
    html = requests.get(url)
    search = BeautifulSoup(html.content, "html.parser")
    vocabulary = search.find("ul", id="rj")
    words = vocabulary.find_all("li")
    wordList = []
    cleanWordList = []
    verbs = []
    cleanVerbs = []
    filename = "rijeci-"+str(urlNumber)+".txt"
    filenameVerbs = "glagoli-" + str(urlNumber) + ".txt"

    def cleanWords():
        regex = r'<p class="(?:word|word-old)">(.*?)</p>(.*?)</li>'
        wordsClean = re.findall(regex, str(words))
        for word in wordsClean:
            if (re.findall(r'.*\b\d+\.', word[0])) != []:
                verbs.append(word[0] + ": " + word[1])
            else:
                wordList.append([word[0] + ": " + word[1]])

    def removeItalics():
        for word in wordList:
            cleanWord = re.sub(r'<i>(.*?)<\/i>', r"\1", word[0])
            cleanWordList.append(cleanWord)

    def removeItalicsVerbs():
        for word in verbs:
            cleanVerb = re.sub(r'<i>(.*?)<\/i>', r"\1", word)
            cleanVerbs.append(cleanVerb)

    def createFile():
        with open(filename, "x", encoding="utf-8") as file:
            file.write("RIJECI VJEZBE BR. " + str(urlNumber) + "\n\n")

    def wordsToText():
        with open(filename, "a", encoding="utf-8") as file:
            for word in cleanWordList:
                file.write(word + "\n")
            file.write("\n"+"IZDVOJENI GLAGOLI"+"\n\n")
            for verb in cleanVerbs:
                file.write(verb+"\n")

    def verbsToText():
        with open(filenameVerbs, "a", encoding="utf-8") as file:
            for word in cleanVerbs:
                file.write(word + "\n")

    if searchForVerbs == True:
        cleanWords()
        removeItalicsVerbs()
        verbsToText()

    else:
        cleanWords()
        removeItalics()
        removeItalicsVerbs()
        createFile()
        wordsToText()

for number in range(1, 80):
    radula(number)



