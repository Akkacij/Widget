from parsers.mainparser.сurrency_parser import CurrencyParser


class USDCurrencyParser(CurrencyParser):
    def __init__(self):
        super().__init__('https://myfin.by/bank/kursy_valjut_nbrb/usd', "USD")
        self.version = "Akkacij 1.0 12.01.2022"
        