# coding:utf-8
import re
import urllib
import urllib2
from urlparse import urlparse
from urlparse import urljoin
import codecs
import sys
import os
from bs4 import BeautifulSoup

# pip install --upgrade beautifulsoup4

def getPdf(dirPath):
    number = 0
    sourceFilePath = os.path.join(dirPath, 'source.txt')

    if not os.path.isfile(sourceFilePath):
        sys.stderr.write('Source file' + sourceFilePath + "does not exist.")
        exit(EXIT_FAILURE)

    for url in open(sourceFilePath, 'r'):
        html = urllib2.urlopen(url).read().decode('utf-8', 'ignore')
        soup = BeautifulSoup(html, "html.parser")
        links = [a.get("href") for a in soup.find_all("a", href=re.compile(r'.*\.pdf'))]

        saveDirPath = os.path.join(dirPath, 'list' + str(number)) 
        try: os.mkdir(saveDirPath)
        except OSError: pass

        for link in links:
            saveFilePath = os.path.join(saveDirPath, os.path.basename(link))
            absPdfUrl = urljoin(url, link)
            urllib.urlretrieve(absPdfUrl, saveFilePath)    

        number = number + 1

if __name__ == '__main__':
    getPdf('ipa')
