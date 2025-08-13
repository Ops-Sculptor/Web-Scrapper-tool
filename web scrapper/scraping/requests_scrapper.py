import time
from bs4 import BeautifulSoup
from core.logger import get_logger
from scraping.extractors import extract_cards_from_soup
from scraping.pagination import find_pagination_links

logger = get_logger(__name__)

def scrape_with_requests(url, session, config, categories):
    cards = []
    try:
        response = session.get(url, timeout=config['scraping']['timeout'])
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        cards.extend(extract_cards_from_soup(soup, url, categories, config))

        pagination_links = find_pagination_links(soup, url)
        for page_url in pagination_links[:config['scraping']['max_pages_per_site']]:
            time.sleep(config['scraping']['delay_between_requests'])
            page_resp = session.get(page_url, timeout=config['scraping']['timeout'])
            page_soup = BeautifulSoup(page_resp.content, 'html.parser')
            cards.extend(extract_cards_from_soup(page_soup, page_url, categories, config))
    except Exception as e:
        logger.error(f"Error scraping {url} with requests: {e}")
    return cards
