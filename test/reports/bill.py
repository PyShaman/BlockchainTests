import os
import sys
import textwrap

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import data.clients as clients
import data.products as products
# from ..data.clients import Clients
# from ..data.products import Products


def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class GenerateBill:

    def __init__(self):
        self.client = clients.Clients()
        self.product = products.Products()

    def add_item_to_bill(self, category, subcategory, id_, quantity):
        product = self.product.get_product(category, subcategory, id_)
        return f"{product['nazwa']} {product['jednostka']}*{quantity} --- {product['cena']*quantity}", product['cena'], quantity, product['VAT']
