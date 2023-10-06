# Bot name: Bee
# Bee @ your service

name = input('What is your name?\n')

print('Hi, ' + name + ', I am Bee, and welcome to Coffers Cafe.')

menu = {
    'coffee': 3,
    'burger': 5,
    'sandwich': 4,
    'cappuccino': 4,
    'sausage': 3,
}

order_list = []

while True:
    print('What would you like to order ' + name + '?')
    print('Here is the menu:')
    for item, price in menu.items():
        print(f'{item}: ${price}')

    order = input()
    if order in menu:
        quantity = int(input('How many would you like?\n'))
        order_list.append((order, quantity))
    else:
        print('Sorry, we do not have that item on the menu.')

    another = input('Would you like to order another item? (yes/no)\n')
    if another.lower() != 'yes':
        break

total = sum(price * quantity for order, quantity in order_list for item, price in menu.items() if item == order)
print(f"Thank you, {name}! Here is your order:")

for order, quantity in order_list:
    print(f"{quantity} x {order} = ${menu[order] * quantity}")

print(f'Your total is ${total}.')
print('Have a great time, ' + name + ', and enjoy your meal!')

