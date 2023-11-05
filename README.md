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

- [x] Le nom de la série
- [x] Le numéro de l’épisode
- [x] Le numéro de la saison
- [x] La date de diffusion de l’épisode
- [x] Le pays d’origine
- [x] La chaîne qui diffuse la série
- [x] L’url relative de la page de l’épisode sur le site spin-off 

## Fichiers
- [x] Enregistrez ces données dans un fichier episodes.csv
- [x] Écrire une fonction ou une classe qui permet de lire le fichier episodes.csv sans utiliser de librairie

## SQL [1/2]
- [x] Insérer les données de la question Scraping [1/2] dans base de données sqllite appelé database.db 

## Algorithmie [1/2]
- [x] Calculer le nombre d’épisodes diffusés par chaque chaîne de télévision (présente dans les données) en Octobre.
- [x] Indiquer dans le fichier README.md le nom des trois chaînes qui ont diffusé le plus d’épisodes. (voir ci-dessous)
- [x] Indiquer dans le fichier README.md le nom des trois pays qui ont diffusé le plus d’épisodes. (voir ci-dessous)
- [x] Indiquer dans le fichier README.md les mots qui reviennent le plus souvent dans les noms des séries. (voir ci-dessous)

### Les trois chaînes qui ont diffusée le plus d'épisodes
```PY
    {
        'Netflix': 75, 
        'Disney+': 33, 
        'Hulu': 24
    }
```

### Le nombre d'épisode diffusées par pays 
```PY
    {
        'Etats-Unis': 404, 
        'France': 119, 
        'Canada': 82, 
        'Royaume-Uni': 40, 
        'Allemagne': 35, 
        'Espagne': 31, 
        'Suède': 18, 
        'Australie': 11, 
        'Corée du Sud': 6, 
        'Italie': 4, 
        'Belgique': 4, 
        'Danemark': 3, 
        'Europe': 2
    }
```

### Les mots les plus utilisés dans les titres des séries
```PY
    {
        'THE': 21, 
        'OF': 4, 
        'DE': 4,
        # ...
    }
```

## Scraping [2/2] 
- [x] Récupérer la durée de l’épisode pour la chaîne Apple TV

## SQL [2/2]
- [x] Stocker les données de durée d’épisode (en minutes) dans une nouvelles table duration qui contiendra une Foreign Key pointant sur l’épisode en question dans la table episode

## Algorithmie [2/2]
- [x] Indiquer quelle est la chaîne de TV qui diffuse des épisodes pendant le plus grand nombre de jours consécutifs sur le mois de novembre.

### Les chaînes qui diffusent des épisodes pendant le plus grand nombre de jours consécutifs sur le mois de novembre
Neflix est la chaîne TV qui diffuse des épisodes pendant le plus grand nombre de jours consécutifs sur le mois de novembre.

```PY
    {
        'Netflix': 4, 
        'Hulu': 3, 
        'TF1': 3, 
        'Disney+': 3,
        # ...
    }
```
## Orchestration
Créer une commande qui permet d’afficher dans la console les résultats suivants dans le mois de notre choix :

- [x] [NOMBRE] episodes seront diffusés pendant le mois de [MOIS].
- [x] C'est [PAYS] qui diffusera le plus d'épisodes avec [NOMBRE] épisodes.
- [x] C'est [CHAINE] qui diffusera le plus d'episodes avec [NOMBRE] épisodes.
- [x] C'est [CHAINE] qui diffusera des épisodes pendant le plus grand nombre de jours consécutifs avec [NOMBRE] de jours consécutifs.
