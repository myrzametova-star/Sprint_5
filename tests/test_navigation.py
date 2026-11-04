iimport pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import BASE_URL
TABS_DATA = [
    ("Булки"),
    ("Соусы"),
    ("Начинки"),
]

@pytest.mark.parametrize("tab_name", TABS_DATA)
def test_navigation_to_tabs(driver, tab_name):
    """Параметризованный тест для проверки перехода по табам."""
    
    driver.get("https://nomoreparties.co")
    
    tab_element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, f"//*[text()='{tab_name}']"))
    )
    
    tab_element.click()
    
    WebDriverWait(driver, 5).until(
        lambda d: "tab_tab_current" in tab_element.get_attribute("class") or \
                  "tab_tab_current" in tab_element.find_element(By.XPATH, "./..").get_attribute("class")
    )
    
    h2_heading = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, f"//h2[text()='{tab_name}']"))
    )
    
    assert h2_heading.is_displayed(), f"Заголовок {tab_name} не отображается на экране"
    



     
