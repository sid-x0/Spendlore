import re
from datetime import datetime

def parse_expenses(text):
    pattern = r'(\d+)\s*(?:on|for)\s*([\w\s]+?)(?=,|and|$)'
    matches = re.findall(pattern, text, re.IGNORECASE)

    parsed = []
    today = datetime.today().strftime('%Y-%m-%d')
    for amount, category in matches:
        parsed.append({
            'amount': int(amount),
            'category': category.strip().title(),
            'date': today
        })

    return parsed
