## Slicing

players = ['charles', 'martina', 'michael', 'florence','eli']
print(players[-3:])
print(players[:-3])
print(players[1:])
print(players[:-1])
print(players[-1:])
print(players[-1])
print(players[0:])
print(players[0::2])

## looping through slice

print(f"please find the list of first 3 players:")
for player_name in players[:3]:
    print(player_name.title())
##4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to
##the end of the program that do the following:
##Print the message The first three items in the list are:. Then use a slice to print the first
##three items from that program’s list.
##Print the message Three items from the middle of the list are:. Then use a slice to print
##three items from the middle of the list.
##Print the message The last three items in the list are:. Then use a slice to print the last
##three items in the list.

fav_food = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

print("The first 3 foods are:")
for food in fav_food[:3]:
    print(food.title())
print("The middle 3 foods are:")
for food in fav_food[1:4]:
    print(food.title())
print("The last 3 foods are:")
for food in fav_food[2:]:
    print(food.title())

##4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
##Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
##Add a new pizza to the original list.
##Add a different pizza to the list friend_pizzas.
##Prove that you have two separate lists. Print the message My favorite pizzas are:, and
##then use a for loop to print the first list. Print the message My friend’s favorite pizzas
##are:, and then use a for loop to print the second list. Make sure each new pizza is
##stored in the appropriate list.

my_pizza_list = ["chicken Pizza","veg Pizza","double Cheese Pizza"]

my_friend_fav_pizza = my_pizza_list[:]

print(my_pizza_list)
print(my_friend_fav_pizza)

my_pizza_list.append("paneer pizza")
my_pizza_list.append("double chilli pizza")
my_friend_fav_pizza.append("mushroom pizza")

print(my_pizza_list)
print(my_friend_fav_pizza)

print("My favourite pizzas are")
for i in my_pizza_list:
    print(i)
print("My friend favourite pizzas are")
for j in my_friend_fav_pizza:
    print(j)
