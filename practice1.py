#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would
#you invite? Make a list that includes at least three people you’d like to invite to dinner.
#Then use your list to print a message to each person, inviting them to dinner.
list_invited = ["vin", "ben", "garry", "grify"]
print(f"Hey! {list_invited[1]}, Please come to dinner.")
for i in list_invited[0:2]:
    print(f"Hey! {i}, Please come to dinner.")


##3-5. Changing Guest List: You just heard that one of your guests can’t make the
##dinner, so you need to send out a new set of invitations. You’ll have to think of
##someone else to invite.
##Start with your program from Exercise 3-4. Add a print() call at the end of your
##program, stating the name of the guest who can’t make it.
##Modify your list, replacing the name of the guest who can’t make it with the name of the
##new person you are inviting.
##Print a second set of invitation messages, one for each person who is still in your list.

removed_person = list_invited.remove("grify")
print(removed_person)
list_invited.append("jim")
print(list_invited)
for i in list_invited:
    print(f"Hey! {i}, Please come to dinner.")

##
##3-6. More Guests: You just found a bigger dinner table, so now more space is
##available. Think of three more guests to invite to dinner.
##Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your
##program, informing people that you found a bigger table.
##Use insert() to add one new guest to the beginning of your list.
##Use insert() to add one new guest to the middle of your list.
##Use append() to add one new guest to the end of your list.
##Print a new set of invitation messages, one for each person in your list.

print("Bigger table found!")
list_invited.insert(0,"adam")
list_invited.insert(2,"don")
list_invited.append("marrie")
for i in list_invited:
    print(f"Hey! {i}, Please come to dinner.")


##3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in
##time for the dinner, and now you have space for only two guests.
##Start with your program from Exercise 3-6. Add a new line that prints a message saying
##that you can invite only two people for dinner.
##Use pop() to remove guests from your list one at a time until only two names remain in
##your list. Each time you pop a name from your list, print a message to that person
##letting them know you’re sorry you can’t invite them to dinner.
##Print a message to each of the two people still on your list, letting them know they’re
##still invited.
##Use del to remove the last two names from your list, so you have an empty list. Print
##your list to make sure you actually have an empty list at the end of your program.

print("Sorry! table size for the guest list changed, so removing few from list")
for i in list_invited[0:5]:
    list_invited.pop(0)
print(list_invited)
del list_invited[0]
#del list_invited[1]
#print(list_invited)

##
##3-8. Seeing the World: Think of at least five places in the world you’d
##like to visit. Store the locations in a list. Make sure the list is not
##in alphabetical order. Print your list in its original order. Don’t
##worry about printing the list neatly; just print it as a raw Python
##list. Use sorted() to print your list in alphabetical order without
##modifying the actual list. Show that your list is still in its original
##order by printing it. Use sorted() to print your list in
##reverse-alphabetical order without changing the order of the original
##list. Show that your list is still in its original order by printing it
##again. Use reverse() to change the order of your list. Print the list to
##show that its order has changed. Use reverse() to change the order of
##your list again. Print the list to show it’s back to its original order.
##Use sort() to change your list so it’s stored in alphabetical order.
##Print the list to show that its order has been changed. Use sort() to
##change your list so it’s stored in reverse-alphabetical order. Print the
##list to show that its order has changed.


country_name = ["Germany", "Britan", "India", "America", "Brazil"]
print(country_name)
print(sorted(country_name))
print(country_name)
print(sorted(country_name,reverse=True))
print(country_name)
country_name.sort()
print(country_name)
country_name.reverse()
print(country_name)



