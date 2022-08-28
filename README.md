# ProjetDataCollectionDit
La base de données utilisée dans ce projet est une base de données sqlite. Ce qui veut
dire que le projet peut être testé si vous respectez les consignes qui sont enumerés dans 
la partie 'Demarrage du projet'.

### Demarrage du projet
   - installer les packages contenu dans le fichier requirements.txt
   - Taper à la racine du projet dans un terminal la commande suivante : 
    uvicorn main:app
   - Attender d'avoir le message ' Application startup complete' dans le terminal
   et ouvrer votre navigateur et taper l'adresse qui est indiquée dans 
   le message ' Uvicorn running on http://127.0.0.1:8000'. Généralement l'adresse est : http://127.0.0.1:8000
   - Ceci affichera la liste des employés dans le navigateur au format JSON.

### Description de quelques methodes

#### La méthode getDataFileHtml de HtmlFactory
Cette méthode permet d'ouvrir et de lire le fichier .html et de recuperer les données sous forme d'une liste d'objets

#### La méthode main de HtmlFactory
Elle appelle la méthode getDataFileHtml pour recuperer les données issus du 
fichier html et la méthode naming qui permet de transformé la première lettre
du prénom en majuscule et le nom en majuscule. Et ensuite elle retourne les données.

#### La méthode concatenerPlusieursList de Utils
Cette méthode permet de concatener plusieurs listes quelque soit le nombre d'arguments passé en paramètre

#### La méthode randomElement de Utils
Elle permet d'attribuer aléatoirement les éléments d'une liste

#### La méthode addDevise de DataGlobal
Elle permet d'ajouter le noeud 'devise' à la structure des données et d'attribuer aléatoirement une devise issue
de la liste des devises sur le site de la BECEAO.

#### La méthode addConversionXof de DataGlobal
Elle permet d'ajouter le noeud 'salaryXOF' à la structure de données
et de faire la conversion de chaque salaire de chaque employer en XOF en
fonction de sa devise.

#### La méthode addPays de DataGlobal
Cette méthode permet d'ajouter les noeuds 'pays' et 'flags' à la structure de 
données et d'attribuer aléatoirement un pays à chaque employer et le ou les flag(s) du pays en question.

#### La méthode main de DataGlobal
Elle permet de faire appel à addDevise, addConversionXof et à
addPays pour avoir l'ensemble des traitements qui ont été faites
sur les données.

#### La méthode makeCurrencyList de CurrencyScrapper
Elle permet de recupérer la liste des devises sur le site de 
la BCEAO à l'aide du web scrapping.

#### La méthode apiCountries de Country
Cette méthode permet de recupérer la liste des pays du monde 
à travers l'api https://restcountries.com/v2/all

#### La méthode getConnexion de Connexion
Elle permet de créer une base de données Sqlite appelée 'projetDataCollectionBd.bd'.

#### La méthode createTable de EmployerModel
Elle permet de créer la table Employe dans la base de 
données 'projetDataCollectionBd'.

#### La méthode insererListeEmploye de EmployerModel
Cette méthode permet d'inserer une liste d'objets dans la table 'employe'.

#### La méthode recupererListeEmploye de EmployerModel
Cette méthode permet de recuperer les données de la table 'employe'
sous forme de liste d'objets.

#### la fonction listeEmployerBD de main.py
Elle permet d'avoir les données issues de la table 'employe' de 
la base de données sqlite 'projetDataCollectionBd'

### la fonction root de main.py
Elle permet de delivrer sur une URL(http://127.0.0.1:8000/) la liste des employés issue de la base de données
à l'aide de la fonction 'listeEmployerBD'
   