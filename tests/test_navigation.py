import pytest
from selenium.webdriver.common.by import By
from locators import StellarBurgersLocators

class TestStellarBurgersNavigation:


    def test_constructor_tabs_navigation(self, driver):
        driver.get("https://qa-stellarburgers.education-services.ru/")
  
        driver.find_element(*StellarBurgersLocators.SAUCES_TAB).click()
        assert "Соусы" in driver.find_element(*StellarBurgersLocators.ACTIVE_TAB).text
        
   
        driver.find_element(*StellarBurgersLocators.FILLINGS_TAB).click()
        assert "Начинки" in driver.find_element(*StellarBurgersLocators.ACTIVE_TAB).text
        
        driver.find_element(*StellarBurgersLocators.BUNS_TAB).click()
        assert "Булки" in driver.find_element(*StellarBurgersLocators.ACTIVE_TAB).text