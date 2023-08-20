from html_parser import HTMLParser


class CifrusPriceParser(HTMLParser):
    def __init__(self, price_tag="new_price"):
        super().__init__(price_tag)
