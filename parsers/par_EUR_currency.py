from parsers.mainparser.сurrency_parser import CurrencyParser


class EURCurrencyParser(CurrencyParser):
    def __init__(self):
        super().__init__('https://myfin.by/bank/kursy_valjut_nbrb/usd', "EUR")
        