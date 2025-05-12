import requests
from bs4 import BeautifulSoup
import openpyxl
import re

class Product:
    def __init__(self, name, price, link):
        self.name = name
        self.price = price
        self.link = link
        self.category = self.categorize(price)

    def categorize(self, price_str):
        try:
            value = float(re.sub(r"[^\d,\.]", "", price_str).replace(",", "."))
        except ValueError:
            return "Nav informacijas"
        if value < 500:
            return "Lidz 500 €"
        elif value < 1500:
            return "No 500 € Lidz 1500 €"
        elif value < 3000:
            return "No 1500 € Lidz 3000 €"
        return "3000+ €"

class CategoryNode:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.next = None

class Catalog:
    def __init__(self):
        self.head = None
        for name in ["Lidz 500 €", "No 500 € Lidz 1500 €", "No 1500 € Lidz 3000 €", "3000+ €", "Nav informacijas"]:
            self.add_category(name)

    def add_category(self, name):
        node = CategoryNode(name)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def add_product(self, product):
        current = self.head
        while current:
            if current.name == product.category:
                current.products.append(product)
                return
            current = current.next

    def save_to_excel(self, filename):
        wb = openpyxl.Workbook()
        current = self.head
        while current:
            sheet = wb.create_sheet(title=current.name)
            sheet.append(["Nosaukums", "Cena", "URL"])
            for p in current.products:
                sheet.append([p.name, p.price, p.link])
            current = current.next
        del wb["Sheet"]
        wb.save(filename)

def fetch_products(url):
    r = requests.get(url)
    if r.status_code != 200:
        return []
    soup = BeautifulSoup(r.content, "html.parser")
    items = []
    for block in soup.find_all("div", class_="prod"):
        name = block.find("div", class_="name")
        price = block.find("div", class_="price")
        link = block.find("a", class_="imp")
        if name and price and link:
            p = Product(name.get("title", "").strip(), price.text.strip(), "https://www.dateks.lv" + link["href"])
            items.append(p)
    return items

def main():
    pages = int(input("Cik lapas apskatīt (ieskaitot galveno)? "))
    catalog = Catalog()
    urls = ["https://www.dateks.lv/cenas/portativie-datori"] + [
        f"https://www.dateks.lv/cenas/portativie-datori/pg/{i}" for i in range(1, pages)
    ]
    for url in urls:
        print(f"Apskatu: {url}")
        for prod in fetch_products(url):
            catalog.add_product(prod)
    catalog.save_to_excel("products.xlsx")
    print("Dati saglabāti 'products.xlsx'.")

if __name__ == "__main__":
    main()
