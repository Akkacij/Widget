from panel.pn_text_currency import PanelTextCurrency
from database.db_currency import DataBaseCurrency
from parsers.par_USD_currency import USDCurrencyParser


class PanelTextCurrencyUSD(PanelTextCurrency):
    def __init__(self, win, name="CurrencyUSD"):
        super().__init__(win=win, name=name, parser=USDCurrencyParser(), database=DataBaseCurrency(name="USD"))
        self.pn_version = "Akkacij 1.0 12.01.2022"
        