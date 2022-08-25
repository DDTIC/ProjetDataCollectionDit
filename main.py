from libraries.utils import Utils
from libraries.csv import CsvFactory
from libraries.json import JsonFactory
from libraries.html import HtmlFactory


if __name__ == '__main__':

    csvFactory = CsvFactory
    jsonFactory = JsonFactory
    htmlFactory = HtmlFactory

    dataCsvFactory = csvFactory.main()
    dataJsonFactory = jsonFactory.main()
    dataHtmlFactory = htmlFactory.main()

    print(Utils.divider())
    print(dataHtmlFactory)
    print(Utils.divider())
    print(dataJsonFactory)
    print(Utils.divider())
    print(dataCsvFactory)