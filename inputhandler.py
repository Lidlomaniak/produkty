from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def enter_plu_code(driver, code):
    try:
        input_field = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.NAME, "plu-number"))
        )
    except TimeoutException:
        try:
            input_field = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, "//input[@data-testid='plu-number-input']"))
            )
        except TimeoutException:
            print("❌ Nie znaleziono pola do wpisania PLU – frontend się zmienił?")
            return False

    input_field.clear()
    input_field.send_keys(code)
    input_field.send_keys(Keys.ENTER)
    return True
