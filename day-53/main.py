from types import resolve_bases
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import time
import fill_form

CHROME_DRIVER_PATH = "/Users/rodrigocamila/PycharmProjects/chromedriver"
URL_IMOVEIS = "https://www.imovirtual.com/arrendar/apartamento/braga/?search%5Bfilter_float_price%3Ato%5D=550&search%5Bfilter_enum_rooms_num%5D%5B0%5D=2&search%5Bfilter_enum_rooms_num%5D%5B1%5D=3&search%5Bfilter_enum_rooms_num%5D%5B2%5D=4&search%5Bregion_id%5D=3"


class WhereToLive:
    def __init__(self, driver_path) -> None:
        self.driver = webdriver.Chrome(executable_path=driver_path)
        time.sleep(3)
        self.driver.maximize_window()

    
    def find_place(self, site):
        self.driver.get(url=site)
        time.sleep(5)
        cookie = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie.click()
        time.sleep(3)
        response = requests.get(url=site)
        imo_hp = response.text
        soup = BeautifulSoup(imo_hp, "lxml")
        advertisement = soup.find_all("span", class_="offer-item-title")
        prices = soup.find_all("li", class_="offer-item-price")
        list_advertisement = []
        list_prices = []
        for apartment in advertisement:
            text = apartment.getText()
            list_advertisement.append(text)
        for price in prices:
            text = price.getText()
            list_prices.append(text.strip().split()[0])
        time.sleep(3)
        self.driver.quit()
        return list_advertisement, list_prices
    

place_to_rent = WhereToLive(CHROME_DRIVER_PATH)
list_places = place_to_rent.find_place(URL_IMOVEIS)

for x in range(len(list_places[0])):
    fill_form.FillForm().fill_form(list_places[0][x],list_places[1][x])
# print(list_places[0][0], list_places[1][0])
# to_form = fill_form.FillForm().fill_form(list_places[0][0],list_places[1][0])
# print(to_form)

# TODO Ajustar nomes das variáveis dos apartamentos, como: anuncio, preço e link