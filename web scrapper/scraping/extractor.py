import re
import json
from bs4 import BeautifulSoup
from core.models import VisitingCard
from core.logger import get_logger

logger = get_logger(__name__)

def extract_cards_from_soup(soup: BeautifulSoup, url: str, categories, config):
    """Run all extraction strategies and return VisitingCard list."""
    cards = []
    strategies = [
        extract_from_structured_data,
        extract_from_contact_sections,
        extract_from_category_specific_selectors,
        extract_from_generic_patterns
    ]
    for strategy in strategies:
        try:
            strategy_cards = strategy(soup, url, categories, config)
            cards.extend(strategy_cards)
        except Exception as e:
            logger.debug(f"Strategy failed: {e}")
    return cards

def extract_from_structured_data(soup, url, categories, config):
    cards = []
    json_scripts = soup.find_all('script', type='application/ld+json')
    for script in json_scripts:
        try:
            data = json.loads(script.string)
            if isinstance(data, list):
                data = data[0]
            if data.get('@type') in ['Person', 'Organization']:
                card = VisitingCard(
                    name=data.get('name', ''),
                    email=data.get('email', ''),
                    phone=data.get('telephone', ''),
                    website=data.get('url', ''),
                    source_url=url,
                    company=data.get('worksFor', {}).get('name', '') if data.get('worksFor') else ''
                )
                cards.append(card)
        except Exception:
            continue
    return cards

def extract_from_contact_sections(soup, url, categories, config):
    cards = []
    contact_sections = soup.find_all(['div', 'section'], class_=re.compile(
        r'(contact|team|staff|members|profiles|directory|cards)', re.I
    ))
    for section in contact_sections:
        contact_items = section.find_all(['div', 'article', 'li'], class_=re.compile(
            r'(card|contact|person|member|profile|item)', re.I
        ))
        for item in contact_items:
            card = extract_card_from_element(item, url)
            if is_valid_card(card, config):
                cards.append(card)
    return cards

def extract_from_category_specific_selectors(soup, url, categories, config):
    cards = []
    for category in categories:
        if category not in config['categories']:
            continue
        cat_conf = config['categories'][category]
        selectors = cat_conf.get('selectors', {})
        for keyword in cat_conf['keywords']:
            for text in soup.find_all(text=re.compile(keyword, re.I)):
                container = text.parent.find_parent(['div', 'section', 'article', 'li'])
                if container:
                    card = VisitingCard(category=category, source_url=url)
                    for field, field_selectors in selectors.items():
                        value = extract_field_value(container, field_selectors, field)
                        setattr(card, field, value)
                    if is_valid_card(card, config):
                        cards.append(card)
    return cards

def extract_from_generic_patterns(soup, url, categories, config):
    cards = []
    selectors = [
        '[href*="mailto:"]',
        '[href*="tel:"]',
        '.vcard', '.h-card', '.contact-info', '.business-card', '.profile-card'
    ]
    processed = set()
    for selector in selectors:
        for element in soup.select(selector):
            card_elem = element.find_parent(['div', 'section', 'article', 'li'])
            if not card_elem or id(card_elem) in processed:
                continue
            processed.add(id(card_elem))
            card = extract_card_from_element(card_elem, url)
            if is_valid_card(card, config):
                cards.append(card)
    return cards

def extract_card_from_element(element, url):
    card = VisitingCard(source_url=url)
    card.name = extract_field_value(element, ['h1', 'h2', 'h3', '.name', '.person-name'], 'name')
    card.company = extract_field_value(element, ['.company', '.organization', '.org'], 'company')
    card.position = extract_field_value(element, ['.position', '.job-title'], 'position')
    card.email = extract_field_value(element, ['[href*="mailto:"]', '.email'], 'email')
    card.phone = extract_field_value(element, ['[href*="tel:"]', '.phone'], 'phone')
    card.website = extract_field_value(element, ['[href^="http"]', '.website'], 'website')
    card.address = extract_field_value(element, ['.address', '.location'], 'address')
    return card

def extract_field_value(element, selectors, field_type):
    for selector in selectors:
        found = element.select_one(selector)
        if found:
            if field_type == 'email' and 'mailto:' in found.get('href', ''):
                return found.get('href').replace('mailto:', '').split('?')[0]
            elif field_type == 'phone' and 'tel:' in found.get('href', ''):
                return found.get('href').replace('tel:', '')
            elif found.get('href'):
                return found.get('href')
            else:
                return found.get_text(strip=True)
    return ''

def is_valid_card(card, config):
    """Validate card using filters config."""
    required = 0
    if card.name: required += 1
    if card.company: required += 1
    if card.email: required += 1
    if card.phone: required += 1
    return required >= config['filters']['min_fields_required']
