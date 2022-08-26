# ProjetDataCollectionDit

### Demarrage du projet
   installer les packages contenu dans le requirements.txt
   installer fastapi avec la commande pip install "fastapi[all]"
   pour lancer le serveur et tester l'api, saisir dans le terminal :
   uvicorn employer:app --reload

### Description de quelques methodes
#### La méthode main de HtmlFactory
Cette méthode permet d'ouvrir et de lire le fichier .html et de recuperer les données sous forme d'une liste d'objets

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
données et d'attribuer aléatoirement un pays à chaque employer et le ou les flag(s) du pays question.

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
Elle permet de réaliser la connexion avec une base de données
Mysql.

#### La méthode createTable de EmployerModel
Elle permet de créer la table Employer dans la base de 
données projetDataCollection si la table n'existe.

#### La méthode inserer de EmployerModel
Cette méthode permet d'inserer une liste d'objets dans la
base de données.

#### La méthode recuperer de EmployerModel
Cette méthode permet de recuperer les données dans la
base de données.
   