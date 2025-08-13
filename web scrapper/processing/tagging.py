def apply_tags(cards, config):
    location_keywords = config['tag_rules']['location_keywords']
    for card in cards:
        tags = []
        address_lower = card.address.lower() if card.address else ""
        for location, keywords in location_keywords.items():
            if any(k in address_lower for k in keywords):
                tags.append(location)
        card.tags = tags
    return cards
