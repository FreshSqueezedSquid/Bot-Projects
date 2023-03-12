# Very simple chat bot to take coffee orders
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  temp_option = hot_or_iced()
  drink_type = get_drink_type()
  print(f"Alright, that's a {size}, {temp_option}{drink_type}")
  name = input('Can I get your name please? \n')
  print(f"Thanks, {name}! Your drink will ready shortly.")

def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'Small'
  elif res == 'b':
    return 'Medium'
  elif res == 'c':
    return 'Large'
  else:
    print_message()
    # recursive function call keeps prompting user for correct input type
    return get_size()

def get_drink_type():
  res = input('What kind of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if res == 'a':
    return 'Brewed Coffee'
  elif res == 'b':
    return 'Mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    # recursive function call keeps prompting user for correct input type
    return get_drink_type()
  
def hot_or_iced():
  res = input('Would you like that hot, or over ice? \n[a] Hot \n[b] Iced \n> ')
  if res == 'a':
    return 'Hot'
  elif res == 'b':
    return ice_option()
  else:
    print_message()
    # recursive function call keeps prompting user for correct input type
    return hot_or_iced()

def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  if res == 'a':
    return ' Latte w/2% milk'
  elif res == 'b':
    return 'latte w/Non-fat milk'
  elif res == 'c':
    return 'Late w/Soy milk'
  else:
    print_message()
    # recursive function call keeps prompting user for correct input type
    return order_latte()

def ice_option():
  res = input('Ice cubes or would you like the drinkl blended? \n[a] Ice Cubes \n[b] Blended \n> ')
  if res == 'a':
    return 'Iced'
  if res == 'b':
    return 'Frappe'

def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


# calling bot
coffee_bot()
