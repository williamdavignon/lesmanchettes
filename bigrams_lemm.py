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
# ls = []


#bi-grams lemmatisés
for row in contenu:
    texte = row[5].replace("|", "").replace("=","")
    texte = texte.lower()
    doc = nlp(texte)
    tokens = [token.text for token in doc]
    # print(tokens)
    lemmes = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
    for lemme in lemmes:
        tousMots.append(lemme)
    
    for x, y in enumerate (lemmes[:-1]):
        bigrams.append("{} {}".format(lemmes[x], lemmes[x+1]))

list = Counter(bigrams)
top = (list.most_common(200))
print(top)

fichierF = "topBigrams_lemm.csv"


for mots in top:
    dead = open(fichierF, "a")       #ajouter infos au csv
    obies = csv.writer(dead)
    obies.writerow(mots)
    print(mots)

print("done")
os.system("say 'Done'")




