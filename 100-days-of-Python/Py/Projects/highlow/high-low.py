from game_data import data
import random

def format_data(account):
    account_name=account["name"]
    account_desc=account["description"]
    account_country=account["country"]
    return (f"{account_name},a {account_desc}, from {account_country} ")

account_a=random.choice(data)
account_b=random.choice(data)
if account_a==account_b:
    account_b=random.choice(data)

