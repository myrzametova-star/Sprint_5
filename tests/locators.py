from selenium.webdriver.common.by import By

class StellarBurgersLocators:
  
    MAIN_LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']")
    FORGOT_PASSWORD_LOGIN_LINK = (By.XPATH, ".//a[@href='/login' and text()='Войти']")
    LOGIN_HEADER = (By.XPATH, ".//h2[text()='Вход']")
 
    REG_NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    REG_EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    REG_PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")
    REG_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    REG_PASSWORD_ERROR = (By.XPATH, ".//p[contains(@class, 'input__error') and text()='Некорректный пароль']")
    REG_LOGIN_LINK = (By.XPATH, ".//a[@href='/login' and text()='Войти']")

    @staticmethod
    def get_tab_locator(tab_name):
        return (By.XPATH, f"//*[text()='{tab_name}']")

    @staticmethod
    def get_tab_heading_locator(tab_name):
        return (By.XPATH, f"//h2[text()='{tab_name}']")
    