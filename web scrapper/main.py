from config.config_loader import load_config
from scraping.base_scraper import setup_session
from scraping.requests_scrapper import scrape_with_requests
from scraping.selenium_scrapper import scrape_with_selenium
from processing.filters import apply_filters
from processing.tagging import apply_tags
from processing.duplication import remove_duplicates
from core.logger import get_logger

logger = get_logger(__name__)

def main():
    config = load_config()
    session = setup_session()
    urls = ["https://example.com"]  # Replace with your target URLs
    categories = list(config['categories'].keys())

    all_cards = []
    for url in urls:
        cards = scrape_with_requests(url, session, config, categories)
        if config['scraping']['use_selenium'] and len(cards) < 5:
            cards.extend(scrape_with_selenium(url, config, categories))
        all_cards.extend(cards)

    all_cards = remove_duplicates(all_cards)
    all_cards = apply_filters(all_cards, config)
    all_cards = apply_tags(all_cards, config)

    logger.info(f"Scraped {len(all_cards)} unique cards.")

if __name__ == "__main__":
    main()
