import json

def save_to_json(cards, filename="output.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump([card.__dict__ for card in cards], f, indent=2, ensure_ascii=False)
