import pandas as pd

def save_to_excel(cards, filename="output.xlsx"):
    df = pd.DataFrame([card.__dict__ for card in cards])
    df.to_excel(filename, index=False)
