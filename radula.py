import requests
from bs4 import BeautifulSoup
import re

def radula(urlNumber, searchForVerbs=False):
    filename = "Rijeci"+str(urlNumber)+".txt"
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
    regex = r'<p class="(?:word|word-old)">(.*?)</p>(.*?)</li>'
    wordsClean = re.findall(regex, str(words))

    for word in wordsClean:
        if (re.findall(r'.*\b\d+\.', word[0])) != []:
            verbs.append("'"+word[1].strip()+"'"+":"+"'"+word[0].strip()+"'")
        else:
            wordList.append(["'"+word[1].strip()+"'"+":"+"'"+word[0].strip()+"'"])

    for word in wordList:
        cleanWord = re.sub(r'\s<i>(.*?)<\/i>', "", word[0])#removes the <i> tags in some words that remained after the regex cleaning
        cleanWord = re.sub(r"\s*\(.*?\)", "", cleanWord) #removes anything in parentheses
        cleanWord = re.sub("[\\,\\.\\-]", "", cleanWord) #removes . , —
        cleanWordList.append(cleanWord)

    for word in verbs:
        cleanVerb = re.sub(r'\s<i>(.*?)<\/i>', "", word) #same thing like the one above just for verbs
        cleanVerb = re.sub(r'"\s*\(.*?\)"', "", cleanVerb)
        cleanVerb = re.sub("[,\\,\\.\\-]", "", cleanVerb)
        cleanVerb = re.sub(r"\s—", "", cleanVerb)
        cleanVerbs.append(cleanVerb)

    if searchForVerbs == False:
        with open("rijeci.txt", "a", encoding="utf-8") as file: #writes the words in first, then the verbs seperately
            file.write("RIJECI VJEZBE BR. "+str(urlNumber)+"\n\n")
            for word in cleanWordList:
                file.write(word + "\n")
            file.write("\n"+"IZDVOJENI GLAGOLI"+"\n\n")
            for verb in cleanVerbs:
                file.write(verb+"\n")
            file.write("\n")
    else:
        with open("GLAGOLI VJEZBE BR."+str(urlNumber), "a", encoding="utf-8") as file: #writes the words in first, then the verbs seperately
            file.write("\n"+"IZDVOJENI GLAGOLI"+"\n\n")
            for verb in cleanVerbs:
                file.write(verb+"\n")

def purgo(finishfile):  # makes a set to remove duplicate words
    words = set()
    with open("rijeciSve.txt", encoding="utf-8") as file:
        for fileLine in file:
            words.add(fileLine)
    with open(finishfile, "w", encoding="utf-8") as file:
        for word in words:
           file.write(word)

def interrogatum():
    with open("glagole.txt", "a", encoding="utf-8") as file:
        for word in wordsClean:
            if (re.findall(r'.*\b\d+\.', word[0])) != []:
                file.write((str(word[0]) + ": " + str(word[1])+"\n"))

