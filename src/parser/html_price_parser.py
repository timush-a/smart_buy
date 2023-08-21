from bs4 import BeautifulSoup


class HTMLPriceParser:
    def __init__(self, element: str, price_tag_class: str):
        self.element = element
        self.price_tag_class = price_tag_class
        self.bs = BeautifulSoup(features="html.parser")

    def _parse(self, text: str) -> str:
        return self.bs.find(self.element, attrs={'class': self.price_tag_class}, text=text)

    @staticmethod
    def _convert_str_to_int(price: str):
        return int(''.join([_ for _ in price if _.isdigit()]))

    def get_price(self, text: str) -> int:
        return self._convert_str_to_int(self._parse(text))
