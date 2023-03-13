from utilities import get_size, hot_or_iced, ice_option, order_latte, print_message, get_drink_type

def coffee_bot():
  print("Welcome to the cafe!")

  order_drink = 'y'
  drinks = []

  while order_drink == 'y':
    size = get_size()
    temp_option = hot_or_iced()
    drink_type = get_drink_type()
    drink = f"{size}, {temp_option} {drink_type}"
    print(f"Alright, that's a {drink}!")

    while True:
      drinks.append(drink)
      order_drink = input("Would you like to order another drink? \n (y/n) \n>")
      if order_drink in ['y', 'n']:
        break

  print("Okay, so I have:\n ")
  for d in drinks:
    print("\n *", d)

  name = input('Can I get your name please? \n')
  print(f"Thanks, {name}! Your drink will ready shortly.")

# calling bot
coffee_bot()
