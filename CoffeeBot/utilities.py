# using to help unclutter CoffeBot a bit

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_drink_type():
  while True:
    res = input('What kind of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
    if res == 'a':
      return 'Brewed Coffee'
    elif res == 'b':
      return order_mocha()
    elif res == 'c':
      return order_latte()
    # if other char is used, print_message() is returned until either 'a' or 'b' is entered
    print_message()

def order_latte():
  while True:
    res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
    if res == 'a':
      return ' Latte w/2% milk'
    elif res == 'b':
      return 'latte w/Non-fat milk'
    elif res == 'c':
      return 'Late w/Soy milk'
    # if other char is used, print_message() is returned until either 'a' or 'b' is entered
    print_message()

def order_mocha():
  # the while loop remains true until a valid input is given, and subsequernt value returned
  while True:
    res = input('Would you like to try our limited-edition peppermint mocha? \n[a] Sure! \n[b] Maybe next time! \n> ')
    if res == 'a':
      return 'Peppermint Mocha'
    elif res == 'b':
      return 'Mocha'
    # if other char is used, print_message() is returned until either 'a' or 'b' is entered
    print_message()

def ice_option():
  while True:
    res = input('Ice cubes or would you like the drinkl blended? \n[a] Ice Cubes \n[b] Blended \n> ')
    if res == 'a':
      return 'Iced'
    if res == 'b':
      return 'Frappe'
    # if other char is used, print_message() is returned until either 'a' or 'b' is entered
    print_message()

def get_size():
  while True:
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    if res == 'a':
      return 'Small'
    elif res == 'b':
      return 'Medium'
    elif res == 'c':
      return 'Large'
    # if other char is used, print_message() is returned until either 'a' or 'b' is entered
    print_message()

def hot_or_iced():
  while True:
    res = input('Would you like that hot, or over ice? \n[a] Hot \n[b] Iced \n> ')
    if res == 'a':
      return 'Hot'
    elif res == 'b':
      return ice_option()
    # if other char is used, print_message() is returned until either 'a' or 'b' is entered
    print_message()

