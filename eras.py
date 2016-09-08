## baroque 

brq = "https://en.wikipedia.org/wiki/List_of_Baroque_composers"

from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

soup = BeautifulSoup(urlopen(brq), 'html.parser')

#for li in soup.find_all("li"):
#    print li.text ## names and birth/death dataes were saved in brq.txt


#with open("brq.txt") as csvfile:
#    reader = csv.reader(csvfile, delimiter = '(')
#    for row in reader:
#        name = row[0]
#        name = name[:-1]
#        print name


##Repeat the procedure with other eras

# classical
cls = "https://en.wikipedia.org/wiki/List_of_Classical-era_composers"

soup2 = BeautifulSoup(urlopen(cls), 'html.parser')

#for li in soup2.find_all("li"):
#    print li.text


#with open("cls.txt") as csvfile:
#    reader = csv.reader(csvfile, delimiter = '(')
#    for row in reader:
#        name = row[0]
#        name = name[:-1]
#        print name


#the rest contains table mixed with lists or table only

## 21century

#latest = "https://en.wikipedia.org/wiki/List_of_21st-century_classical_composers"
#soup3 = BeautifulSoup(urlopen(latest), 'html.parser')

#for content in soup3.find_all('a'):
#    print content.get("title")

## 20th century

#twenty = "https://en.wikipedia.org/wiki/List_of_20th-century_classical_composers"
#soup4 = BeautifulSoup(urlopen(twenty), 'html.parser')

#for content in soup4.find_all('a'):
#    print content.get("title")

## romantic era
#romantic = "https://en.wikipedia.org/wiki/List_of_Romantic-era_composers"
#soup5 = BeautifulSoup(urlopen(romantic), 'html.parser')

#for content in soup5.find_all('a'):
#    print content.get("title")

## medieval era

#medieval = "https://en.wikipedia.org/wiki/List_of_medieval_composers"
#soup6 = BeautifulSoup(urlopen(medieval), 'html.parser')

#for content in soup6.find_all('a'):
#    print content.get("title")

## renaissance era

renaissance = "https://en.wikipedia.org/wiki/List_of_Renaissance_composers"
soup7 = BeautifulSoup(urlopen(renaissance), 'html.parser')

for content in soup7.find_all('a'):
    print content.get("title")

