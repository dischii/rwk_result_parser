""" This script is used to download the HTML of the RWK shooting website. """
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

XPATH_LOGIN_AUSWAHL = '/html/body/div/div/form[1]/div/input'
XPATH_ANZEIGEN_HTML = '//*[@id="content"]/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[13]/td/form[2]/input[2]'


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

    driver.find_element(By.XPATH, XPATH_ANZEIGEN_HTML).click()

    driver.switch_to.frame("drucken")
    iframe_soup = BeautifulSoup(driver.page_source, 'html.parser')
    with open("output.html", "w", encoding="utf-8") as file:
        file.write(iframe_soup.prettify())

    driver.switch_to.default_content()

    driver.close()