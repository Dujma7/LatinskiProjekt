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

    def cleanWords():
        regex = r'<p class="(?:word|word-old)">(.*?)</p>(.*?)</li>' #regex for cleaning up the words, if the word is a verb, it is stored seperately, else it's stored in the wordList
        wordsClean = re.findall(regex, str(words))
        for word in wordsClean:
            if (re.findall(r'.*\b\d+\.', word[0])) != []:
                verbs.append(word[0] + ": " + word[1])
            else:
                wordList.append([word[0] + ": " + word[1]])

    def removeItalics():
        for word in wordList:
            cleanWord = re.sub(r'<i>(.*?)<\/i>', r"\1", word[0]) #removes the <i> tags in some words that remained after the regex cleaning
            cleanWordList.append(cleanWord)

    def removeItalicsVerbs():
        for word in verbs:
            cleanVerb = re.sub(r'<i>(.*?)<\/i>', r"\1", word) #same thing like the one above just for verbs
            cleanVerbs.append(cleanVerb)

    def createFile():
        with open("rijeci.txt", "x", encoding="utf-8") as file: #self-explanatory really
            file.write("RIJECI\n\n")

    def wordsToText():
        with open("rijeci.txt", "a", encoding="utf-8") as file: #writes the words in first, then the verbs seperately
            for word in cleanWordList:
                file.write(word + "\n")
            file.write("\n"+"IZDVOJENI GLAGOLI"+"\n\n")
            for verb in cleanVerbs:
                file.write(verb+"\n")

    def verbsToText():
        with open("rijeci.txt", "a", encoding="utf-8") as file: #same thing like above (used for verb searching exclusively
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
        #createFile()
        wordsToText()

def purgo(): #makes a set to remove duplicate words, then rewrites it in a seperate text file
    words = set()
    with open("rijeci.txt", encoding="utf-8") as file:
        for fileLine in file:
            words.add(fileLine)
    with open("rijeciCiste.txt", "w", encoding="utf-8") as file:
        for word in words:
            file.write(word)
