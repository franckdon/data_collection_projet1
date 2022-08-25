import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import random

PATH_URL = 'cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts'
URL = f'https://www.bceao.int/fr/{PATH_URL}'

lien = 'https://restcountries.com/v2/all'

class dataCountries(object):

    @classmethod
    def apiGet(cls, lien):
        res = requests.get(lien)
        data = res.text
        parse_json = json.loads(data)
        return parse_json

    @classmethod
    def makeList(cls, data):
        if data:
            countries_name = []
            countries_flags = []
            list_countries = []
            for items in data:
                countries_name.append(items['name'])
                countries_flags.append(items['flag'])
            list_countries = [{'name': countries_name, 'flag': countries_flags} for countries_name, countries_flags in zip(countries_name, countries_flags) ]
            return list_countries
        return None

class DataSouper(object):
    
    @classmethod
    def httpFetcher(cls, URL):
        with requests.Session() as session:
            result = session.get(URL)
            result = result.text
            return result


class CurrencyScrapper(object):
    
    @classmethod
    def scrapLink(cls, URL):
        return DataSouper \
            .httpFetcher(URL)
    
    @classmethod
    def souper(cls, URL):
        result = cls.scrapLink(URL)
        return BeautifulSoup(
            result,
            'html.parser')
    
    @classmethod
    def getBoxCourse(cls, URL):
        soupering = cls.souper(URL)
        soupering = soupering \
            .find_all(attrs={
                'id': 'box_cours'})
        if soupering:
            table = soupering[0].table
            return table
        return None
    
    @classmethod
    def makeCurrencyList(cls, URL):
        soupering = cls.getBoxCourse(URL)
        if soupering:
            tr = soupering.find_all('tr')
            factory = [
                item.find_all('td')
                for item in tr
            ][1:]
            factory = [
                {
                    'Devise': x.string.strip(),
                    'Achat': float(y.string.strip().replace(',', '.')),
                    'Vente': float(z.string.strip().replace(',', '.')),
                }
                for (x, y, z) in factory
            ]
            return factory
        return None
    
    @classmethod
    def addRandomDevise(cls, factory):
        a = ["Euro", "Dollar", "yen"]
        if factory:
            for item in factory:
                item.update( {"new_devise":random.choice(a)})
            return factory
        return None

    @classmethod
    def addXofConversion(cls, factory):
        if factory:
            for item in factory:
                if item["new_devise"] == "Euro":
                    item.update( {"XOF_conversion": item["Vente"] * 654.23 })
                elif item["new_devise"] == "Dollar":
                    item.update( {"XOF_conversion": item["Vente"] * 656.50 })
                else:
                    item.update( {"XOF_conversion": item["Vente"] * 4.80 })
            return factory
        return None

    @classmethod
    def addColumnCountryAndFlag(cls, factory, listCountry):
        if factory:
            for item in factory:
                item.update(random.choice(listCountry))
            df = pd.DataFrame(factory)
            return df
        return None

    
    @classmethod
    def main(cls):
        data = CurrencyScrapper.makeCurrencyList(URL)
        result = CurrencyScrapper.addRandomDevise(data)
        myList = CurrencyScrapper.addXofConversion(result)

        jsonCountries = dataCountries.apiGet(lien)
        items = dataCountries.makeList(jsonCountries)

        defList = CurrencyScrapper.addColumnCountryAndFlag(myList, items)

        return defList
    