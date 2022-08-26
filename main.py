from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.dataAll import DataGlobal
from bd.connexionBd import Connexion
from bd.traitementBd import EmployerModel

if __name__ == '__main__':

    ## recupération des données csv, json et html
    dataCsvFactory = CsvFactory.main()
    dataJsonFactory = JsonFactory.main()
    dataHtmlFactory = HtmlFactory.main()

    print(Utils.divider())
    ## concatenation des données csv, json et html
    dataAll = Utils.concatenerPlusieursList(dataCsvFactory, dataJsonFactory, dataHtmlFactory)
    #print(dataAll)
    print(Utils.divider())

    ## Recuperation des données issu des traitements sous jacents
    dataEmployer = DataGlobal.main(dataAll)
    print(dataEmployer)
    print(Utils.divider())

    ## Connexion à la base de données
    conn = Connexion.getConnexion()

    ## Creation de la table employer
    EmployerModel.createTable(conn)

    ## Inserer les données dans la table employer
    EmployerModel.inserer(dataEmployer, conn)

    ## Recuperer les données de la table employer
    dataBd = EmployerModel.recuperer(conn)
    print(dataBd)
    print(Utils.divider())
    conn.close()

