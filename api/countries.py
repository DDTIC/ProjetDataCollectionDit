import requests

URL = 'https://restcountries.com/v2/all'

class Country(object):

    @classmethod
    def apiCountries(cls):
        data = requests.get(URL)
        res_json = data.json()
        return res_json

    @classmethod
    def main(cls):
        data = cls.apiCountries()
        return data