#coding : utf-8

import sys, csv, spacy, os
from collections import Counter

csv.field_size_limit(sys.maxsize)

nlp = spacy.load("fr_core_news_md")

fichier = "contenu.csv"
contenu = open(fichier)
contenu = csv.reader(contenu)
next(contenu)

tousMots = []
bigrams = []

for row in contenu:
    texte = row[5].replace("|", "").replace("=","")
    texte = texte.lower()
    doc = nlp(texte)
    tokens = [token.text for token in doc if token.is_stop == False and token.is_punct == False]
    for tok in tokens:
        tousMots.append(tok)
    
    for x, y in enumerate (tokens[:-1]):
        bigrams.append("{} {}".format(tokens[x], tokens[x+1]))

list = Counter(bigrams)
top = (list.most_common(300))
print(top)

fichierF = "topBigrams non-lemmatisés.csv"


for mots in top:
    dead = open(fichierF, "a")       #ajouter infos au csv
    obies = csv.writer(dead)
    obies.writerow(mots)
    print(mots)




