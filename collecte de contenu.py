#coding: utf-8
import csv, requests, time
from bs4 import BeautifulSoup
from random import seed
from random import choice
seed(1) 
sequence = [i for i in range(10)]


fichier = "contenu.csv"
fichierUrl = "url.csv"
fichierUrl= open(fichierUrl)
fichierUrl = csv.reader(fichierUrl)
#### Statuts (certains url n'ont pas d'articles et renvoient un 404. Fforonction en IF à ajouter)
# url = "http://lesmanchettes.com/actualites/justice-et-faits-divers/523"

save = 0
good = 0
bad = 0
num_rows = 0
num_try = 0
for row in open("contenu.csv"):
    num_rows += 1
print(num_rows)
print("*"*16)


for url in fichierUrl:
    if url[1] == "200":
        num_try += 1
        if num_try > num_rows:
            for _ in range(1):            # <--- effet random
                selection = choice(sequence)
                print(selection)
            time.sleep(selection)
            site = requests.get(url[2])
            if site.status_code == 404:
                print(url[2])
                print("Erreur 404")
            else:
                #titre
                #
                page = BeautifulSoup(site.text, "html.parser")
                titre = page.find("h1", class_="entry-title page-header")
                if titre is not None:
                    titre = titre.contents[0]
                    titre = str(titre).strip()
                    # print(titre)
                #
                # # Corps de l'article
                #
                page = BeautifulSoup(site.text, "html.parser")
                article = page.find("article")
                body = article.find_all("p")
                # print("*"*15)
                texte = ""
                for p in body:
                    # print(p.text)
                    texte += p.text + " "
                # print("*"*15)
                # print(texte.strip())
                texte = texte.replace("\n", "")
                texte = texte.replace("\xa0", "")
                texte = texte.strip()
                #categorie
                cat = article.find("span", class_="category-name")
                cat = cat.find("a")
                cat = cat.text
                # print(cat)
                #date
                date = article.find("time")
                # print(date)
                if date is not None:
                    date = date.get("datetime")
                    date = date[0:10]
                    # print(date)
                #nbcar
                nbcar = len(texte)
                #création de la list(rangée du csv)
                infos = list()
                infos.append(url[2])
                infos.append(date)
                infos.append(nbcar)
                infos.append(cat)
                infos.append(titre)
                infos.append(texte)
                print(infos[0])
                print(type(infos))
                #csv
                dead = open(fichier, "a")       #ajouter infos au csv
                obies = csv.writer(dead)
                obies.writerow(infos)