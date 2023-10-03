#bot name Bee
#Bee @ yur service

name = input('what is yur name?\n')

print('Hi,' + name, 'am Bee and welcome to coffers cafe.')

menu = "coffee, burger, sandwich, capuccino, sausage"

print('what would yu like to order ' + name, menu + '?')

order = input()

price = 8

quantity = input(" How many would yu like?\n")

total = price * int(quantity)

print("well Thank YOU", name, "your total is $" + str(total))
print('Have a blast', name, 'enjoy yur', order + 's.')
