#Schreiben Sie ein Python-Programm, um zu überprüfen, ob eine Zeichenfolge nur einen bestimmten Satz von Zeichen enthält (in diesem Fall a-z, A-Z und 0-9).




import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))


#Schreiben Sie ein Python-Programm, das eine Zeichenfolge mit einem a gefolgt von null oder mehr bs abgleicht.
import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))

#Der Unterschied zwischen ^a(b*)$ und ^ab*$ liegt in der Anzahl der "b"-Zeichen, die in der Zeichenkette vorkommen können.

#^a(b*)$ erlaubt beliebig viele "b"-Zeichen (einschließlich keinmal), solange sie direkt nach dem Buchstaben "a" stehen.
#    erlaubt beliebig viele "b"-Zeichen (einschließlich keinmal), die direkt nach dem Buchstaben "a" stehen, aber es erlaubt auch, dass die Zeichenkette nur aus dem Buchstaben "a" besteht.



#Schreiben Sie ein Python-Programm, das eine Zeichenfolge mit einem a gefolgt von drei „b“ abgleicht.

import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))

#Schreiben Sie ein Python-Programm, das ein Wort findet, das „z“ enthält, nicht den Anfang oder das Ende des Wortes.


import re
def text_match(text):
        patterns = '\Bz\B'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))

#Quelle und weitere Übungen unter: https://www.w3resource.com/python-exercises/re/

def fakultaet(n):
    if n == 0:
        return 1
    else:
        return n * fakultaet(n-1)

def fakultaet_iterative(n):
    fakultaet = 1
    for i in range(1, n+1):
        fakultaet *= i
    return fakultaet
    
zahl = 6
ergebnis = fakultaet_iterative(zahl)
print(f"Fakultaet von {zahl} ist: {ergebnis}")

eingebettete_liste = [[1,2,3],[4,5,6],[7,8,9]]

flache_liste = []
for innere_liste in eingebettete_liste:
    for item in innere_liste:
        flache_liste.append(item)
print(flache_liste)

# Klasse Person, Name, Alter
# Begrüßungsfunktion mit Name und Alter
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    def begruessung(self):
        print(f"Hallo, mein Name ist {self.name} und mein Alter ist {self.age}.")
        
        
person1 = Person("Vorname", 21)
person1.begruessung()
# Dictionary Personen: Alter, Beruf, Wohnort
# 2 Presonen anlegen

personen = {
    "Max": [25, "Ingenieur", "Berlin"],
    "Peter": [27, "Lehrer", "München"]
}

# Person hinzufügen
personen["Stefan"] = [27, "Lehrer", "München"]

#Alter ändern:
personen["Max"][0] = 30
print(personen)
#FUnktion nah_und_fern : 3 inputs (a,b,c)
#+ True, wenn b oder c nahe ist (nicht größer als 1)
#False, Abstand größer als 2

def nah_und_fern(a,b,c,):
    bedingung1 = abs(a-b) <= 1 and abs(b-c) >=2 and abs(a-c) >= 2
    bedingung2 = abs(a-c) <= 1 and abs(a-b) >=2 and abs(c-b) >= 2
    return bedingung1 or bedingung2
    
print(nah_und_fern(2,4,6))
# False

#Alterszahlenreihe

def summe_ohne_zwanziger(a, b, c):
# keine zahl im intervall 20 bis 29
# Summe aus 3 Zahlen (int)
    gesamtsumme = a + b + c
    if 20 <= a <= 29:
        gesamtsumme -= a
    if 20 <= b <= 29:
        gesamtsumme -= b
    if 20 <= c <= 29:
        gesamtsumme -= c
    
    return gesamtsumme
    
ergebnis = summe_ohne_zwanziger(10,20,30)
print(ergebnis) # 40


class Book:
    def __init__(self, title, author, content):
        self.title=title
        self.author=author
        self.content=content
        
        
    def read(self, page):
        pages = self.content.split("\n")
        for i in range(0, page-1):
            print(pages[i])
            
    def __str__(self):
        return self.title + " geschrieben von " + self.autor
        
# funktion primzahl
# true anhand zahl 


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
# 2, 3, 6, 18, 108, 1944, ? , ??, ???
# rekursive funktion für nte zahl der sequenz
def next_num(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return next_num(n-1) * next_num(n-2)
        
        

# FOM -> MOF rekursiv
def reverse(text):
    if len(text) == 0:
        return ""
    else:
        return text[-1] + reverse(text[0:-1])
        
def get_biggest(meine_liste): #rekursiv größter wert der liste ausgeben
    if len(meine_liste) == 1:
        return meine_liste[0]
    else:
        return max(meine_liste[0], get_biggest(meine_liste[1:]))


#Anonyme Funktion, die 15 zu zahl addiert
r = lambda a: a + 15
print(r(19))

# produkt von 2 zahlen
r = lambda x, y: x*y
print(r(4,7))

# test_range n in 3 bis 8
def test_range(n):
    if n in range(3,9):
        print("ist in range")
    else:
        ...
test_range(5)

# funktion mit 2 argumenten, max aus 2 zahlen
def max_zahl(x,y):
    if x > y:
        return x
    return y

# max aus 3 zahlen
def max_aus_drei(x,y,z):
    max_zahl(x, max_zahl(y,z))
    
print(max_aus_drei(3,2,-6))

# liste : alle geraden nummern mit lambda

nums = [1,2,34,4,5,7]

gerade_num = list(filter(lambda x: x % 2 == 0, nums))

#ungeraden

ungerade_num = list(filter(lambda x: x % 2 != 0, nums))

# dictionary: handy hersteller, modell, farbe
# sortierten nach farbe

models = [
    {'hersteller': 'Nokia', 'modell': 6210, 'farbe': 'Schwarz'},
    {'hersteller': 'Samsung', 'modell': 515, 'farbe': 'Gruen'}
]

sorted_models = sorted(models, key=lambda x: x['farbe'])
print(sorted_models)

#
import datetime

now = datetime.datetime.now()
print(now)
# 
year = lambda x: x.year
...

#2 listen mit zahlen, die sich überlappen

num1 = [1,2,3,4,5,6]
num2 = [4,5,6,7,8,9]

result = list(filter(lambda x: x in num1, num2))
print(result)

# tupel

mein_tuple = (2,5,7,8,9,10)
# immutable!
mein_tuple = mein_tuple + (11,)
print(mein_tuple)

#15,20,25 hinzufügen, zwischen den ersten fünf elementen, die original 5 element duplizieren

mein_tuple=mein_tuple[:5] + (15,20,25) + mein_tuple[:5]

## array von 5 integern, anzeigen einzelner array-elemente, über indizes
# import array !!
zahlen_array = array('i', [1,2,5,7])
for i in zahlen_array:
    print(i)
    
print(zahlen_array[0])

# funktion innerhalb von funktionen aufrufen
b = ...
def test(a):
    def add(b):
        nonlocal a
        a += 1  
        return a + b
    return add
func = test(4)


# funktion quadratzahlen 1-20 innerhalb liste
def zahlenausgeben():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(l)
    
zahlenausgeben()

# string-reverse
def string_reverse(str1):
    rstr1 = ''
    
    index = len(str1)
    
    while index > 0:
        rstr1 += str1[index -1]
        
        index = index - 1
        
    return rstr1
    
# w3resource.com