## Projet créé par Lucky MARTY & Jonathan MARTIN
Créé le 05/11/2023 
Organiser via GitHub 

## Nécessitées
- Voir les imports fait dans le fichier `requirements.txt` 
- Voir la version de Python dans le fichier `runtime.txt` 

### Questions 
“Pensez à bien utiliser cette commande dans le même terminal que celui que vous utilisez pour exécuter vos fichiers .py.“
Commande à utiliser : `pip show [package-name]`
Réponse : Car cela permet d'avoir la bonne version de la librairie qui tourne dans un environnement Python sur un projet donné.

# Questions traitées 
## Scraping  [1/2]

[X] Le nom de la série
[X] Le numéro de l’épisode
[X] Le numéro de la saison
[X] La date de diffusion de l’épisode
[X] Le pays d’origine
[X] La chaîne qui diffuse la série
[X] L’url relative de la page de l’épisode sur le site spin-off 

## Fichiers
[X] Enregistrez ces données dans un fichier episodes.csv
[X] Écrire une fonction ou une classe qui permet de lire le fichier episodes.csv sans utiliser de librairie

## SQL [1/2]
[X] Insérer les données de la question Scraping [1/2] dans base de données sqllite appelé database.db 

## Algorithmie [1/2]
[X] Calculer le nombre d’épisodes diffusés par chaque chaîne de télévision (présente dans les données) en Octobre.
[X] Indiquer dans le fichier README.md le nom des trois chaînes qui ont diffusé le plus d’épisodes. (voir ci-dessous)
[X] Indiquer dans le fichier README.md le nom des trois pays qui ont diffusé le plus d’épisodes. (voir ci-dessous)
[X] Indiquer dans le fichier README.md les mots qui reviennent le plus souvent dans les noms des séries. (voir ci-dessous)

### Les trois chaînes qui ont diffusée le plus d'épisodes
```PY
    {
        'Netflix': 126,
        'TF1': 43,
        'Disney+': 34
    }
```

### Le nombre d'épisode diffusées par pays 
```PY
    {
        'Allemagne': 35,
        'Australie': 11,
        'Belgique': 4,
        'Canada': 81,
        'Corée du Sud': 6,
        'Danemark': 3,
        'Espagne': 31,
        'Etats-Unis': 404,
        'Europe': 2,
        'France': 119,
        'Italie': 4,
        'Royaume-Uni': 40,
        'Suède': 18
    }
```

### Les mots les plus utilisés dans les titres des séries
```PY
    {
        'THE': 23,
        'OF': 7,
        'DE': 3,
        '(2023)': 3,
        'LES': 3, 
        'AMERICAN': 3, 
        'EVERYTHING': 2,
        # ...
    }
```

## Scraping [2/2] 
[X] Récupérer la durée de l’épisode pour la chaîne Apple TV

## SQL [2/2]
[X] Stocker les données de durée d’épisode (en minutes) dans une nouvelles table duration qui contiendra une Foreign Key pointant sur l’épisode en question dans la table episode

## Algorithmie [2/2]
[X] Indiquer quelle est la/les chaîne(s) de TV qui diffuse(nt) des épisodes pendant le plus grand nombre de jours consécutifs sur le mois d’Octobre.

### Les chaînes qui diffusent des épisodes pendant le plus grand nombre de jours consécutifs sur le mois d'octobre
TF1 et France 2 (ex aequo) sont les chaînes TV qui diffusent des épisodes pendant le plus grand nombre de jours consécutifs sur le mois d'octobre.

```PY
    {
        'TF1': 5, 
        'France 2': 5, 
        'TVE': 4, 
        'ZDF': 4, 
        'Netflix': 3,
        # ...
    }
```
## Orchestration
Créer une commande qui permet d’afficher dans la console les résultats suivants dans le mois de notre choix :
[X] [NOMBRE] episodes seront diffusés pendant le mois de [MOIS].
[X] C'est [PAYS] qui diffusera le plus d'épisodes avec [NOMBRE] épisodes.
[X] C'est [CHAINE] qui diffusera le plus d'episodes avec [NOMBRE] épisodes.
[X] C'est [CHAINE] qui diffusera des épisodes pendant le plus grand nombre de jours consécutifs avec [NOMBRE] de jours consécutifs.