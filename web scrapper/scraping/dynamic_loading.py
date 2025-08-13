import time
from selenium.webdriver.common.by import By

def handle_dynamic_loading(driver):
    load_more_buttons = ['.load-more', '.show-more']
    for selector in load_more_buttons:
        try:
            button = driver.find_element(By.CSS_SELECTOR, selector)
            if button.is_displayed():
                driver.execute_script("arguments[0].click();", button)
                time.sleep(2)
        except:
            continue
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
