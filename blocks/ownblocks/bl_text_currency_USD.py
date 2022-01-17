from blocks.bl_text_currency import BlockTextCurrency
from database.db_currency import DataBaseCurrency
from parsers.par_USD_currency import USDCurrencyParser


class BlockTextCurrencyUSD(BlockTextCurrency):
    def __init__(self, win, name="CurrencyUSD"):
        super().__init__(win=win, name=name, parser=USDCurrencyParser(), database=DataBaseCurrency(name="USD"))
        self.version = "Akkacij 1.0 12.01.2022"
        