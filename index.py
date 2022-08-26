from libraries.csvFile import CsvFactory
from libraries.jsonFile import JsonFactory
from libraries.utils import Utils
from libraries.htmlFile import HtmlFactory
from libraries.concatenate import concatenateList
from libraries.devises import CurrencyScrapper

if __name__ == '__main__':
    print(Utils.divider())
    print(HtmlFactory.main())
    print('\n')
    print(Utils.divider())
    print(CsvFactory.main())
    print('\n')
    print(Utils.divider())
    print(JsonFactory.main())
    print('\n')
    print(concatenateList.concatenate(HtmlFactory.main(), CsvFactory.main(), JsonFactory.main() ))
    print('\n')
    print(CurrencyScrapper.main())
