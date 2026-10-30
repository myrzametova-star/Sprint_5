import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    
    # Неявное ожидание загрузки элементов формы (стандарт Практикума)
    chrome_driver.implicitly_wait(10)
    
    yield chrome_driver
    chrome_driver.quit()