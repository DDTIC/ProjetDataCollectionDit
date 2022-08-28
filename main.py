from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.dataAll import DataGlobal
from bd.connexionBd import Connexion
from bd.traitementBd import EmployerModel

from fastapi import FastAPI

## Renvoie la liste des employés qui se trouve dans la base de données
def listeEmployerBD():

    ## recupération des données csv, json et html
    dataCsvFactory = CsvFactory.main()
    dataJsonFactory = JsonFactory.main()
    dataHtmlFactory = HtmlFactory.main()

    ## concatenation des données csv, json et html
    dataAll = Utils.concatenerPlusieursList(dataCsvFactory, dataJsonFactory, dataHtmlFactory)

    ## Recuperation des données issu des traitements sous jacents
    dataEmployer = DataGlobal.main(dataAll)

    ## Création de la base de données
    engine = Connexion.getConnexion()

    ## Creation de la table employe
    table_employe = EmployerModel.createTable(engine)

    ## Inserer les données dans la table employe
    EmployerModel.insererListeEmployer(engine, table_employe, dataEmployer)

    ## Recuperer les données de la table employe
    dataBd = EmployerModel.recupererListeEmploye(engine, table_employe)
    return dataBd


app = FastAPI()
@app.get("/")
async def root():
    return listeEmployerBD()


'''
if __name__ == '__main__':


    ## recupération des données csv, json et html
    dataCsvFactory = CsvFactory.main()
    dataJsonFactory = JsonFactory.main()
    dataHtmlFactory = HtmlFactory.main()

    ## concatenation des données csv, json et html
    dataAll = Utils.concatenerPlusieursList(dataCsvFactory, dataJsonFactory, dataHtmlFactory)
    #print(dataAll)

    ## Recuperation des données issu des traitements sous jacents
    dataEmployer = DataGlobal.main(dataAll)
    #print(dataEmployer)

    ## Création de la base de données
    engine = Connexion.getConnexion()

    ## Creation de la table employe
    table_employe = EmployerModel.createTable(engine)

    ## Inserer les données dans la table employe
    EmployerModel.insererListeEmployer(engine, table_employe, dataEmployer)

    ## Recuperer les données de la table employe
    dataBd = EmployerModel.recupererListeEmploye(engine, table_employe)
    print(Utils.divider())
    #print(dataBd)
    print(Utils.divider())
'''





