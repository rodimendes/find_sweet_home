from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = "/Users/rodrigocamila/PycharmProjects/chromedriver"
URL_FORMS = "https://docs.google.com/forms/d/e/1FAIpQLSfRvDXXT2f8oiHdjIGoQikEA9YUPcl4XmXiDeF12R_4XN9vPQ/viewform?usp=sf_link"


class FillForm:
    # def __init__(self, driver_path) -> None:
    #     self.driver_forms = webdriver.Chrome(executable_path=driver_path)
    #     time.sleep(3)
    #     self.driver_forms.maximize_window()

    
    def fill_form(self, place, price):
        self.driver_forms = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        time.sleep(3)
        self.driver_forms.maximize_window()
        self.driver_forms.get(url=URL_FORMS)
        time.sleep(5)
        title_advert = self.driver_forms.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        title_advert.send_keys(f"{place}")
        time.sleep(1)
        monthly_value = self.driver_forms.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        monthly_value.send_keys(f"{price}")
        time.sleep(3)
        submit = self.driver_forms.find_element(By.CSS_SELECTOR, "span.exportLabel")
        submit.click()
        time.sleep(1)

# place = FillForm().fill_form("apartamento do rodrigo", "100")