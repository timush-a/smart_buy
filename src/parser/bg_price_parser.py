from html_price_parser import HTMLPriceParser


class BGParser(HTMLPriceParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
