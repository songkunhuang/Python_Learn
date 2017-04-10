# -*— coding: utf-8 -*-
"""
#1
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\n已经确认的用户有:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#2
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


responses = {}

#标志
polling_active = True

while polling_active:
    name = input("\nWhat is yoru name? ")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == "no":
        polling_active =False

print("\n-- Poll Results --")
for name,response in responses.items():
    print(name + " would like to climb " + response + ".")

"""



























