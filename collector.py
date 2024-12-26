""" This script is used to download the HTML of the RWK shooting website. """
import os
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

XPATH_LOGIN_AUSWAHL = '/html/body/div/div/form[1]/div/input'
XPATH_ANZEIGEN_HTML = '//*[@id="content"]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[13]/td/form[2]/input[2]'
XPATH_RUNDEN_ID = '//*[@id="content"]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[8]/td[2]/select'

def download_html():
    """ Downloads the HTML of the RWK shooting website. """
    driver = webdriver.Chrome()
    driver.get('https://www.rwk-shooting.de/drucken/index.php')
    assert "Login" in driver.title

    select_element = driver.find_element(By.NAME, "user")
    select = Select(select_element)
    select.select_by_value("101000")

    driver.find_element(By.XPATH, XPATH_LOGIN_AUSWAHL).click()

    select_element = driver.find_element(By.NAME, "verein_id")
    select = Select(select_element)
    select.select_by_value("SV Wappersdorf:1")

    file_names = []

    # get all rounds
    select_element = driver.find_element(By.XPATH, XPATH_RUNDEN_ID)
    select = Select(select_element)
    cnt_rounds = len(select.options)

    for i in range(1, cnt_rounds):
        select_element = driver.find_element(By.XPATH, XPATH_RUNDEN_ID)
        select = Select(select_element)
        select_options = select.options
        round_value = select_options[i].get_attribute("value")
        select.select_by_value(round_value)

        driver.find_element(By.XPATH, XPATH_ANZEIGEN_HTML).click()

        driver.switch_to.frame("drucken")
        iframe_soup = BeautifulSoup(driver.page_source, 'html.parser')
        os.makedirs('temp', exist_ok=True)
        file_names.append(f"temp/{round_value.replace(':','_').lower()}.html")
        with open(file_names[len(file_names)-1], "w", encoding="utf-8") as file:
            file.write(iframe_soup.prettify())

        driver.switch_to.default_content()

    driver.close()

if __name__ == '__main__':
    download_html()
