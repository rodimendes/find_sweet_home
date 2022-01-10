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
URL_IMOVEIS = "https://docs.google.com/forms/d/1mYlez2RVRy7g51x0vnNVDQZOHPQvOUrGxbBNGKWZHQc/edit#responses"


driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(URL_IMOVEIS)
time.sleep(10)