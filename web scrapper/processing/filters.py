import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    cleaned = re.sub(r'[\s\-\(\)\.]+', '', phone)
    return re.match(r'^\+?[\d]{7,15}$', cleaned) is not None

def apply_filters(cards, config):
    filtered = []
    for card in cards:
        if card.email and config['filters']['validate_email'] and not validate_email(card.email):
            continue
        if card.phone and config['filters']['validate_phone'] and not validate_phone(card.phone):
            continue
        filtered.append(card)
    return filtered
