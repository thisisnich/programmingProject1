import json
import os

def save_card_to_file(card_details, filename='cards.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Check if the card number already exists
    card_exists = False
    for i, card in enumerate(data):
        if card['card_number'] == card_details['card_number']:
            data[i] = card_details  # Overwrite existing card
            card_exists = True
            break

    if not card_exists:
        data.append(card_details)  # Add new card

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def get_card_from_file(card_number, filename='cards.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for card in data:
                if card['card_number'] == card_number:
                    return card
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    return None

def list_cards(filename='cards.json'):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [card['card_number'] for card in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Example usage
card1 = {
    "card_number": "1234",
    "name": "Alice",
    "expiry_date": "12/24",
    "cvv": "123"
}

card2 = {
    "card_number": "5678",
    "name": "Bob",
    "expiry_date": "11/23",
    "cvv": "456"
}

card3 = {
    "card_number": "1234",
    "name": "Alice Updated",
    "expiry_date": "12/25",
    "cvv": "789"
}

save_card_to_file(card1)
save_card_to_file(card2)
save_card_to_file(card3)  # This will overwrite the existing card with number "1234"

print("Available cards:", list_cards())
print("Details for card 1234:", get_card_from_file("1234"))
print("Details for card 5678:", get_card_from_file("5678"))
