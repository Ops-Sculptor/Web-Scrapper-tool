import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from core.logger import get_logger
from scraping.extractors import extract_cards_from_soup
from scraping.dynamic_loading import handle_dynamic_loading
from fake_useragent import UserAgent

logger = get_logger(__name__)

def setup_selenium_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument(f'--user-agent={UserAgent().random}')
    return webdriver.Chrome(options=chrome_options)

def scrape_with_selenium(url, config, categories):
    cards = []
    try:
        driver = setup_selenium_driver(config['scraping']['headless'])
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        cards.extend(extract_cards_from_soup(soup, url, categories, config))
        handle_dynamic_loading(driver)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        cards.extend(extract_cards_from_soup(soup, url, categories, config))
        driver.quit()
    except Exception as e:
        logger.error(f"Error scraping {url} with selenium: {e}")
    return cards
