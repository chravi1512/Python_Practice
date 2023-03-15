current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

##current_number = 1
##for i in current_number <= 5:
##    print(i)
##    i += 1

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
# Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Store the response in the dictionary.
    responses[name] = response
# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

##7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
##sandwiches. Then make an empty list called finished_sandwiches. Loop through the list
##of sandwich orders and print a message for each order, such as I made your tuna
##sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all
##the sandwiches have been made, print a message listing each sandwich that was
##made.

sandwich_orders = ['STEAK SANDWICH', 'BROADWAY SANDWICH', 'HAMBURGER', 'FALAFEL SANDWICH', 'EGG SALAD SANDWICH']
finished_sandwiches = []
while sandwich_orders:
    new_sandwich = sandwich_orders.pop()
    print(f"I made your {new_sandwich.title()}")
    finished_sandwiches.append(new_sandwich)
print(f"\nThe following sandwiches are made:")
for i in finished_sandwiches:
     print(i.title())
##print(finished_sandwiches.title())

##7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the
##sandwich 'pastrami' appears in the list at least three times. Add code near the
##beginning of your program to print a message saying the deli has run out of pastrami,
##and then use a while loop to remove all occurrences of 'pastrami' from
##sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['STEAK SANDWICH', 'BROADWAY SANDWICH','Pastrami' , 'HAMBURGER','Pastrami', 'FALAFEL SANDWICH', 'EGG SALAD SANDWICH', 'Pastrami']
finished_sandwiches = []
print("deli has run out of pastrami")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
    finished_sandwiches.append(sandwich_orders)
print(f"\nThe following sandwiches are available for now:")
for j in finished_sandwiches:
     print(j)

##7-10. Dream Vacation: Write a program that polls users about their dream vacation.
##Write a prompt similar to If you could visit one place in the world, where would you go?
##Include a block of code that prints the results of the poll.

vacation_list = {}
