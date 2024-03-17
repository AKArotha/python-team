menu = {
   "Espresso": 2.5,
   "Cappuccino": 3.0,
   "Latte": 3.5,
   "Mocha": 4.0,
   "Iced Coffee": 3.5,
   "Tea": 2.0, 
   "Matcha Latte" : 2.0,
   "Green Milk tea" : 1.5,
   "Magarita" : 3.0,
   "Tea": 2.0,
   "Angkor Beer": 2.0,
   "Cambodia Beer": 10.0,
   "Anchor Beer": 30.0,
   "Angkor Puro" : 55.0
}

order = {}

def display_menu():
   print("Menu:")
   for item, price in menu.items():
      print(f"{item}: ${price}")

def add_to_order(item, quantity):
   if item in menu:
      if item in order:
         order[item] += quantity
      else:
         order[item] = quantity
      print(f"{quantity} {item}(s) added to your order.")
   else:
      print("Sorry, that item is not on the menu.")

def view_order():
   total = 0
   if order:
      print("Your order:")
      for item, quantity in order.items():
         print(f"{item}: {quantity}")
         total += menu[item] * quantity
      print(f"Total: ${total}")
   else:
      print("Your order is empty.")

def make_payment():
   total = sum(menu[item] * quantity for item, quantity in order.items())
   print(f"Your total is ${total}. Thank you for your purchase!")
   order.clear()

def cafe_menu():
   while True:
      print("\nWelcome to our cafe!")
      print("1. Display Menu")
      print("2. Add Item to Order")
      print("3. View Order")
      print("4. Make Payment")
      print("5. Exit")

      choice = input("Enter your choice: ")

      if choice == '1':
         display_menu()
      elif choice == '2':
         item = input("Enter item name: ")
         quantity = int(input("Enter quantity: "))
         add_to_order(item, quantity)
      elif choice == '3':
         view_order()
      elif choice == '4':
         make_payment()
      elif choice == '5':
         print("Thank you for visiting our cafe. Have a great day!")
         break
      else:
         print("Invalid choice. Please try again.")

cafe_menu()

