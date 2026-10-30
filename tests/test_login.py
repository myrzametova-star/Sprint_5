import pytest
from selenium.webdriver.common.by import By
from locators import StellarBurgersLocators

class TestStellarBurgersLogin:


    def test_login_from_main_page_success(self, driver):
        driver.get("https://qa-stellarburgers.education-services.ru/")
        driver.find_element(*StellarBurgersLocators.MAIN_LOGIN_ACCOUNT_BUTTON).click()
        
        assert driver.find_element(*StellarBurgersLocators.LOGIN_HEADER).is_displayed()

  
    def test_login_from_personal_account_button_success(self, driver):
        driver.get("https://qa-stellarburgers.education-services.ru/")
        driver.find_element(*StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        
        assert driver.find_element(*StellarBurgersLocators.LOGIN_HEADER).is_displayed()


    def test_login_from_registration_form_success(self, driver):
        driver.get("https://education-services.ru")
 
        driver.find_element(By.XPATH, ".//a[@href='/login']").click()
        
        assert driver.find_element(*StellarBurgersLocators.LOGIN_HEADER).is_displayed()

   
    def test_login_from_forgot_password_form_success(self, driver):
        driver.get("https://education-services.ru")
        driver.find_element(*StellarBurgersLocators.FORGOT_PASSWORD_LOGIN_LINK).click()
        
        assert driver.find_element(*StellarBurgersLocators.LOGIN_HEADER).is_displayed()