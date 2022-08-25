import json
import pandas as pd
from bs4 import BeautifulSoup


BASE_URL = 'DATABASES/data-zIybdmYZoV4QSwgZkFtaB.html'


class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
            file.close()
        return data
    
    @classmethod
    def getTable(cls, data):
        soupering = data \
            .find_all(attrs={
                'id': 'box-data'})
        if soupering:
            table = soupering[0].table
            return table
        return None


    @classmethod
    def makeDataList(cls, table):
        tr = table.find_all('tr')
        factory = [
                item.find_all('td')
                for item in tr
        ][1:]
        factory = [
                {
                    'name': u.string.strip(),
                    'phone': v.string.strip(),
                    'email': w.string.strip(),
                    'address': None,
                    'latlng': x.string.strip(),
                    'salary': y.string.strip(),
                    'age': z.string.strip(),
                }
                for (u, v, w, x, y, z) in factory
        ]
        return factory

    @classmethod
    def main(cls):
        data = cls.openFile()
        table = cls.getTable(data)
        dataList = cls.makeDataList(table)
        return dataList
