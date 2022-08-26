from .utils import Utils
from scrapping.deviseBeceao import CurrencyScrapper
from api.countries import Country

class DataGlobal(object):

    @classmethod
    def listDeviseBeceao(cls):
        return CurrencyScrapper.makeCurrencyList()

    @classmethod
    def addDevise(cls, data):
        def devise(x):
            x['devise'] = Utils \
                    .randomElement(['Euro', 'Dollar us', 'Yen japonais'])
            return x

        data = map(devise, data)
        return list(data)

    @classmethod
    def addConversionXof(cls, listeDevise, data):
        def convEnXOF(x):
            for devise in listeDevise:
                if x['devise'] == devise['Devise']:
                        salaryXOF = x['salary'] * devise['Achat']
                        x['salaryXOF'] = salaryXOF
                        return x

        data = map(convEnXOF, data)
        #data = filter(None, list(data))
        return list(data)

    @classmethod
    def addPays(cls, data, liste):
        def pays(x):

            country = Utils \
                .randomElement(liste)
            x['pays'] = country['name']
            x['flags'] = country['flags']

            return x

        data = map(pays, data)
        return list(data)

    @classmethod
    def main(cls, data):
        data = cls.addDevise(data)
        listDevise = cls.listDeviseBeceao()
        data = cls.addConversionXof(listDevise, data)
        listeCountries = Country.main()

        data = cls.addPays(data, listeCountries)
        return data


