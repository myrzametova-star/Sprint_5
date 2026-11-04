python
import pytest
from selenium.webdriver.common.by import By
from tests.locators import StellarBurgersLocators
from tests.helpers import generate_email  # Импортируем хелпер

class TestRegistration:

    def test_open_registration_page(self, driver):
        registration_url = "https://education-services.ru"
        driver.get(registration_url)
        
        name_input = driver.find_element(*StellarBurgersLocators.REG_NAME_INPUT)
        assert name_input.is_displayed()

    def test_successful_registration(self, driver):
        registration_url = "https://education-services.ru"
        driver.get(registration_url)
        
        user_email = generate_email()
        user_password = "password123"

        driver.find_element(*StellarBurgersLocators.REG_NAME_INPUT).send_keys("Анастасия")
        driver.find_element(*StellarBurgersLocators.REG_EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*StellarBurgersLocators.REG_PASSWORD_INPUT).send_keys(user_password)
        
   
        driver.find_element(*StellarBurgersLocators.REG_SUBMIT_BUTTON).click()
        
        login_header = driver.find_element(*StellarBurgersLocators.LOGIN_HEADER)
        assert login_header.is_displayed()

    def test_registration_short_password_error(self, driver):
        registration_url = "https://education-services.ru"
        driver.get(registration_url)
        
        user_email = generate_email()
        short_password = "123" 
        
        driver.find_element(*StellarBurgersLocators.REG_NAME_INPUT).send_keys("Анастасия")
        driver.find_element(*StellarBurgersLocators.REG_EMAIL_INPUT).send_keys(user_email)
        driver.find_element(*StellarBurgersLocators.REG_PASSWORD_INPUT).send_keys(short_password)
        
      
        driver.find_element(*StellarBurgersLocators.REG_SUBMIT_BUTTON).click()
        
        error_message = driver.find_element(*StellarBurgersLocators.REG_PASSWORD_ERROR)
        assert error_message.is_displayed()
    
