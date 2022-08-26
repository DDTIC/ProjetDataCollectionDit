import requests
import json
#BASE_URL = 'http://api.countrylayer.com/v2/'
#URL = BASE_URL+'all?access_key=ac45601f59458421222964db9544159e'
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