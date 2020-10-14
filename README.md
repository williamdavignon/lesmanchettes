# lesmanchettes
Scripts et contenu recueillis


Ce projet est une collecte de données réalisée à partir du site de fausses nouvelles Lesmanchettes.com. J'avais pour but de constater si certains sujets étaient plus traités que d'autres sur ce site qui tend vers la droite et les théories du complot à la George Soros, New World Order, etc.

Le site a une architecture très simple: les articles sont numérotés dans l'URL, peu importe leur catégorisation. Par exemple, le lien: 

«http://lesmanchettes.com/actualites/international/1481»

menera au même article que le lien:

«http://lesmanchettes.com/actualites/sports/1481».

Le script url.py vise à créer une liste de tout les URLs menant à un article, compilés dans le fichier url.csv.

Le script collecte_de_contenu.py se sert d'une liste d'url et compile le texte contenu dans les titres et le contenu des articles, ainsi que la catégorie, la date de publication et le nombre de caractères, dans un fichier nommé contenu.csv.

Les autres script .py créent des listes de mots individuels et de bigrams, lemmatisés et non-lemmatisés. Ils produisent également une liste de trigrams et des noms propres, chacun triés par fréquence, qu'on peut retrouver dans le dossier "csv".

