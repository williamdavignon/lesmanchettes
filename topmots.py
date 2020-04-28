#coding : utf-8

import sys, csv, spacy
from collections import Counter

csv.field_size_limit(sys.maxsize)

nlp = spacy.load("fr_core_news_md")

fichier = "contenu.csv"
contenu = open(fichier)
contenu = csv.reader(contenu)
next(contenu)

tousMots = []
bigrams = []
# ls = []

#mots individuels, non-lemmatisés, sans stop ni ponctuation Top 300
for row in contenu:
    texte = row[5].replace("|", "").replace("=","")
    texte = texte.lower()
    doc = nlp(texte)
    tokens = [token.text for token in doc if token.is_stop == False and token.is_punct == False]
    # print(tokens)
    # lemmes = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    for tok in tokens:
        tousMots.append(tok)

list = Counter(tousMots)
top = list.most_common(500)
print(top)

fichierF = "topmots_non_lemm.csv"

for mots in top:
    dead = open(fichierF, "a")       #ajouter infos au csv
    obies = csv.writer(dead)
    obies.writerow(mots)
    print(mots)

