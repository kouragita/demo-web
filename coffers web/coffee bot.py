#bot name Bee
#Bee @ yur service
# Define menu items and their prices
menu = {
    "coffee": 5,
    "burger": 10,
    "sandwich": 7,
    "cappuccino": 6,
    "sausage": 8,
}

# Initialize the total cost
total = 0

# Welcome the customer
name = input('What is your name?\n')
print('Hi, ' + name + ', I am Bee, and welcome to Coffers Cafe.')
print('Here is our menu:')

# Display the menu
for item, price in menu.items():
    print(f'{item.capitalize()}: ${price}')

# Ask for orders
while True:
    order = input('What would you like to order from the menu (or type "done" to finish)?\n').lower()

    if order == "done":
        break

    if order not in menu:
        print("Sorry, we don't have that item on our menu.")
        continue

    quantity = int(input(f"How many {order}s would you like?\n"))
    total += menu[order] * quantity

# Display the total cost
print(f"Thank you, {name}! Your total is: ${total}")
print(f"Have a blast, {name}, and enjoy your meal!")

