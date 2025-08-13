def remove_duplicates(cards):
    seen = set()
    unique = []
    for card in cards:
        key = (card.email, card.phone)
        if key not in seen:
            seen.add(key)
            unique.append(card)
    return unique
