import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators
from urls import BASE_URL

class TestStellarBurgersLogin:

    def test_login_from_main_page_success(self, driver):
        driver.get(BASE_URL)
   
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(StellarBurgersLocators.MAIN_LOGIN_ACCOUNT_BUTTON)
        )
        button.click()
        

        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(StellarBurgersLocators.LOGIN_HEADER)
        ).is_displayed()

    def test_login_from_personal_account_button_success(self, driver):
        driver.get(BASE_URL)

        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        button.click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(StellarBurgersLocators.LOGIN_HEADER)
        ).is_displayed()

    def test_login_from_registration_form_success(self, driver):
   
        driver.get(f"{BASE_URL}register")
        
   
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ".//a[@href='/login']"))
        )
        link.click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(StellarBurgersLocators.LOGIN_HEADER)
        ).is_displayed()

    def test_login_from_forgot_password_form_success(self, driver):
  
        driver.get(f"{BASE_URL}forgot-password")
        
       
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(StellarBurgersLocators.FORGOT_PASSWORD_LOGIN_LINK)
        )
        link.click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(StellarBurgersLocators.LOGIN_HEADER)
        ).is_displayed()
        

        
