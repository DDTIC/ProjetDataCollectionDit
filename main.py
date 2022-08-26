from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory
from libraries.dataAll import DataGlobal
from api.countries import Country

if __name__ == '__main__':

    ## instanciation des classes de notre librairies
    csvFactory = CsvFactory
    jsonFactory = JsonFactory
    htmlFactory = HtmlFactory
    dataGlobal = DataGlobal

    ## recupération des données csv, json et html
    dataCsvFactory = csvFactory.main()
    dataJsonFactory = jsonFactory.main()
    dataHtmlFactory = htmlFactory.main()

    ## concatenation des données csv, json et html
    dataAll = Utils.concatenerPlusieursList(dataCsvFactory, dataJsonFactory, dataHtmlFactory)
    print(Utils.divider())
    #print(dataAll)

    ## Ajout d'une entrée concernant la devise attribuée et d'une entrée contenant la conversion en XOF via les données de la BCEAO
    dataSalaryXOF = dataGlobal.main(dataAll)
    print(dataSalaryXOF)
