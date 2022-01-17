from parsers.mainparser.parser import Parser
from bs4 import BeautifulSoup


class CurrencyParser(Parser):
    def __init__(self, url, currency_name="None"):
        super().__init__("{}.CurrencyParser".format(currency_name), url)
        self.version = "Akkacij 1.0 12.01.2022"
        
        self.version = "Akkacij 1.0 11.01.2022"
        
        # self.log = "start working!"
        
    def parsing(self):
        full_page_soup = BeautifulSoup(self.html_page.content, 'html.parser')
        specific_block = full_page_soup.findAll("div", attrs={"class": "cur-rate__cell"})
        if len(specific_block) < 2:
            return False
        first_block = specific_block[0]
        first_block_soup = BeautifulSoup(str(first_block), 'html.parser')
        first_block_data = first_block_soup.findAll("div")

        DFR_ = str(first_block_data[1])[5:15].split(".")
        DFR = "{0}-{1}-{2}".format(DFR_[2], DFR_[1], DFR_[0])
        
        return {"name": self.name,
                "version": self.version,
                "DFR": DFR,
                "VFR": str(first_block_data[4])[16:22], }

    def return_log(self):
        return self.parsing()
    