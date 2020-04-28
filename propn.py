#coding : utf-8

import csv, json, spacy, sys
from collections import Counter
nlp = spacy.load("fr_core_news_md")

csv.field_size_limit(sys.maxsize)

fichier = "contenu.csv"
contenu = open(fichier)
contenu = csv.reader(contenu)
next(contenu)

noms = []

liste = []
for row in contenu:
    doc = nlp(row[5])
    for ent in doc.ents:
        liste.append(str(ent))


count = Counter(liste)
print(count)
top = count.most_common(350)

fichierF = "PROPN.csv"
for mots in top:
    dead = open(fichierF, "a")       #ajouter infos au csv
    obies = csv.writer(dead)
    obies.writerow(mots)
    print(mots)

