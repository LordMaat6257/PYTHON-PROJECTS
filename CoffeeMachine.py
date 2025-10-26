MENU = {
  "espresso": {
    "ingredients": {"water": 50, "coffee": 18},
    "cost": 1.5,
  },
  "latte": {
    "ingredients": {"water": 200, "milk": 150, "coffee": 24},
    "cost": 2.5,
  },
  "cappuccino": {
    "ingredients": {"water": 250, "milk": 100, "coffee": 24},
    "cost": 3.0,
  },
}
resources = {
  "water": 300, # ml
  "milk": 200, # ml
  "coffee": 100, # g
  "money": 0.0, # $
}
COIN_VALUES = {
  "quarters": 0.25,
  "dimes": 0.10,
  "nickels": 0.05,
  "pennies": 0.01,
}
def print_report():
  print(f"Water: {resources['water']}ml")
  print(f"Milk: {resources['milk']}ml")
  print(f"Coffee: {resources['coffee']}g")
  print(f"Money: ${round(resources['money'], 2)}")
def is_resources_sufficient(drink_name):
  """Return (True, "") if enough, else (False, reason)."""
  ingredients = MENU[drink_name]["ingredients"]
  for item, required in ingredients.items():
    if resources.get(item, 0) < required:
      return False, f"Sorry there is not enough {item}."
  return True, ""
def process_coins():
  """Prompt the user for coins and return the total inserted as a float."""
  print("Please insert coins.")
  total = 0.0
  for coin_name in ("quarters", "dimes", "nickels", "pennies"):
    while True:
      try:
        count = input(f"How many {coin_name}? ")
        if count.strip() == "":
          count = 0
        count = int(count)
        if count < 0:
          print("Please enter a non-negative integer.")
          continue
        break
      except ValueError:
        print("Please enter a whole number (0, 1, 2, ...).")
    total += count * COIN_VALUES[coin_name]
  return round(total, 2)
def complete_transaction(drink_name, payment):
  cost = MENU[drink_name]["cost"]
  if payment < cost - 1e-9:
    print("Sorry that's not enough money. Money refunded.")
    return False
  resources["money"] += cost
  change = round(payment - cost, 2)
  if change > 0:
    print(f"Here is ${change} dollars in change.")
  return True
def make_coffee(drink_name):
for item, required in MENU[drink_name]["ingredients"].items():
resources[item] -= required
print(f"Here is your {drink_name}. Enjoy!")
