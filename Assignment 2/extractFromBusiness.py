import os
from bs4 import BeautifulSoup

file = "business/1040901_business_story_3700171.utf8"

with open(file, encoding="utf8") as fileData:
    soup = BeautifulSoup(fileData, features="html.parser")

    docNo = soup.find('docno').text
    text = soup.find('text').text

print(repr(docNo))
print("--------------------------------")
print(repr(text))